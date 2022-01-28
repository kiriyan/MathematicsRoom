import wx
import cv2
import time
from sympy import *
from sympy.abc import a, b, c, d, u, l, r
import threading

global cout, size, draw_mode, pre_step, data_base, temp, era_base, era_cout
#当前总共的步骤(撤销会减少)，图片大小(方法)，绘图模式选择，步骤数，数据库([draw_mode, point1, point2])，图片路径，橡皮擦数据
global switch_open, refresh_mode
refresh_mode = 1 #刷新模式
switch_open = False #是否选择了openfile
global img_size, win2_trans  #图片大小(int)，绘图窗口的透明度
win2_trans = 400
cout, draw_mode, pre_step = 0, 0, 0
data_base, era_base = [], [] #era也需在data中储存 对于每个era_base 有(橡皮类型，参考点1，参考点2，....，参考点n)
era_cout = 0

def Outfile():
    global img_size
    data = open("Outfile.txt", 'w')
    print(img_size[0], end=' ', file=data)  # width
    print(img_size[1], end='\n', file=data)  # height
    for i in range(cout):
        for j in range(len(data_base[i])):
            if j == 0:
                print(data_base[i][j], end=' ', file=data)
                continue
            print(data_base[i][j][0], end=' ', file=data)
            if j == len(data_base[i]) - 1:
                print(data_base[i][j][1], end='\n', file=data)
            else:
                print(data_base[i][j][1], end=' ', file=data)
    data.close()

class Frame(wx.Frame):
    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition,
                 title='one equation'):
        global temp, img_size, size
        temp = image.ConvertToBitmap()
        size = temp.GetWidth() + 115, temp.GetHeight() + 100
        wx.Frame.__init__(self, parent, id, title, pos, size)
        panel = wx.Panel(self)

        self.sld = wx.Slider(panel, value=400, minValue=300, maxValue=500,
                             pos=(temp.GetWidth() + 2, int(img_size[0]/3)),
                             style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.sld.Bind(wx.EVT_SLIDER, self.OnSliderScroll)

        self.CreateStatusBar()
        # Setting up the menu.
        filemenu = wx.Menu()
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        # Setting up the button.
        self.line = wx.ToggleButton(panel, -1, "直线工具line", pos=(temp.GetWidth()+1, 20), size=(100, 20))
        self.line.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle1)
        self.circle = wx.ToggleButton(panel, -1, "圆工具circle", pos=(temp.GetWidth()+1, 45), size=(100, 20))
        self.circle.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle2)
        self.era = wx.ToggleButton(panel, -1, "圆外显示工具era", pos=(temp.GetWidth()+1, 70), size=(100, 20))
        self.era.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle3)
        self.sp3line = wx.ToggleButton(panel, -1, "三点插值曲线x_spline", pos=(temp.GetWidth() + 1, 95), size=(100, 20))
        self.sp3line.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle4)
        self.spl = wx.ToggleButton(panel, -1, "三点插值曲线y_spline", pos=(temp.GetWidth() + 1, 120), size=(100, 20))
        self.spl.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle5)
        self.pre = wx.Button(panel, -1, "上一步", pos=(temp.GetWidth()+1, 1), size=(35, 15))
        self.pre.Bind(wx.EVT_BUTTON, self.OnPre)
        self.pre = wx.Button(panel, -1, "下一步", pos=(temp.GetWidth() + 41, 1), size=(35, 15))
        self.pre.Bind(wx.EVT_BUTTON, self.OnNex)
        self.Centre()
        """
        self.Show()
        self.Fit()
        """
        #垂直大小测定器
        #vbox.Add(self.line, 0, wx.EXPAND | wx.ALIGN_CENTER)


        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        memuRead = filemenu.Append(wx.ID_FILE1, "&Open", "open the file called Readfile")
        menuOut = filemenu.Append(wx.ID_FILE, "O&ut", "print out in the file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "Ab&out", " Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exi&t", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnRead, memuRead)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOut, menuOut)


    def OnRead(self, e):
        global cout, era_cout, era_base, data_base, pre_step, switch_open
        cout, era_cout, pre_step = 0, 0, 0
        era_base, data_base = [], []
        file = open("Readfile.txt", 'r')
        cout, line_cout = 0, 0
        while 1:
            line_cout += 1
            line = file.readline()
            if not line:
                break
            pass
            if line_cout == 1:
                continue
            data0 = line.split(' ')
            data_base.append([int(data0[0])])
            if data0[0] == 3:
                era_base.append([1])
                era_cout += 1
            for i in range(len(data0)):
                if i == 0:
                    continue
                if i % 2 == 0:
                    P = (int(data0[i-1]), int(data0[i]))
                    data_base[-1].append(P)
                    if data0[0] == 3:
                        era_base[-1].append(P)
            cout += 1
            print(data_base[-1])

        file.close()
        switch_open = True
        dlg = wx.MessageDialog(self, "Read", "open the file called Readfile", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnOut(self, e):
        Outfile()
        dlg = wx.MessageDialog(self, "Finished", "print out in the file named Outfile", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self, "A small Drawboard", "About Sample Drawboard", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.


    def OnSliderScroll(self, e):
        global win2_trans
        win2_trans = self.sld.GetValue()


    def OnToggle1(self, event):
        state = event.GetEventObject().GetValue()
        global cout, draw_mode
        if state:
            #模式一为直线模式
            if draw_mode == 0:
                draw_mode = 1
                print("line_on")
                event.GetEventObject().SetLabel("取消直线line")

        elif draw_mode == 1:
            #取消模式
            draw_mode = 0
            print("line_off")
            event.GetEventObject().SetLabel("直线工具line")


    def OnToggle2(self, event):
        state = event.GetEventObject().GetValue()
        global cout, draw_mode
        if state:
            if draw_mode == 0:
                #模式二为圆模式
                draw_mode = 2
                print("circle_on")
                event.GetEventObject().SetLabel("取消圆circle")

        elif draw_mode == 2:
            #取消模式
            draw_mode = 0
            print("circle_off")
            event.GetEventObject().SetLabel("圆工具circle")


    def OnToggle3(self, event):
        state = event.GetEventObject().GetValue()
        global cout, draw_mode
        if state:
            if draw_mode == 0:
                #模式三为橡皮擦模式
                draw_mode = 3
                print("era_on")
                event.GetEventObject().SetLabel("取消圆外显示工具era")

        elif draw_mode == 3:
            #取消模式
            draw_mode = 0
            print("era_off")
            event.GetEventObject().SetLabel("圆外显示工具era")

    def OnToggle4(self, event):
        state = event.GetEventObject().GetValue()
        global cout, draw_mode
        if state:
            if draw_mode == 0:
                #模式四为三次样条插值曲线模式
                draw_mode = 4
                print("x_Spline_on")
                event.GetEventObject().SetLabel("取消三点插值曲线x_spline")

        elif draw_mode == 4:
            # 取消模式
            draw_mode = 0
            print("x_Spline_off")
            event.GetEventObject().SetLabel("三点插值曲线x_spline")

    def OnToggle5(self, event):
        state = event.GetEventObject().GetValue()
        global cout, draw_mode
        if state:
            if draw_mode == 0:
                #模式五为三次样条插值曲线模式
                draw_mode = 5
                print("y_Spline_on")
                event.GetEventObject().SetLabel("取消三点插值曲线y_spline")

        elif draw_mode == 5:
            # 取消模式
            draw_mode = 0
            print("y_Spline_off")
            event.GetEventObject().SetLabel("三点插值曲线y_spline")


    def OnPre(self, event):
        global cout, era_cout, pre_step, refresh_mode
        if data_base:
            if data_base[-1][0] == 3:
                era_base.pop()
                era_cout -= 1
            data_base.pop()
            cout -= 1
            pre_step += 1
            refresh_mode = 2

    def OnNex(self, event):
        global cout, era_cout


class Frame2(wx.Frame):
    global size, draw_mode, temp
    global era_cout, pre_step
    def __init__(self, title):
        global win2_trans
        super(Frame2, self).__init__(parent=None, title=title, size=size)
        #self.SetTransparent(400)  # 设置透明
        self.SetTransparent(win2_trans)

        self.Centre()
        self.Show()

        print("Frame2_on")
        self.status = 0
        self.DownPos = (0, 0)
        self.MovePos = (0, 0)
        self.Sl3p = []
        self.pre = pre_step
        self.line_cout = 0
        self.cir_cout = 0
        self.erase_cout = 0
        self.yslp = 0

        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.OnMove)
        #self.Bind(wx.EVT_PAINT, self.OnPaint)


    def Paint(self):
        global data_base, era_base, refresh_mode
        if self.pre != pre_step:
            self.pre = pre_step
        if cout > 30:
            Outfile()
        else:
            if cout % 3 == 0:
                Outfile()
        # 自动保存
        dc = wx.ClientDC(self)
        # brush = wx.Brush(wx.Colour(255, 255, 255))
        brush = wx.Brush(wx.TRANSPARENT_BRUSH)
        # dc.SetBackground(brush)
        brush2 = wx.Brush(wx.GREY_BRUSH)
        dc.SetBrush(brush)

        if refresh_mode == 2:
            dc.Clear()

        pen1 = wx.Pen(wx.Colour(0, 0, 0), 2)
        pen2 = wx.Pen(wx.Colour(255, 0, 0))
        pen3 = wx.Pen()  # 描点，给插值瞄准
        pen3.SetStyle(wx.PENSTYLE_DOT)
        dc.SetPen(pen1)
        """
        points = [[100, 200], [150, 100], [300, 200], [135, 179]]
        dc.DrawSpline(points)
        dc.DrawSpline(100, 200, 150, 100, 300, 200)
        #三次样条插值曲线
        """

        def my_line(M, N):
            global img_size
            x1, y1, x2, y2 = M[0], M[1], N[0], N[1]
            abc = solve(
                [
                    a - 3,
                    a * x1 + b * y1 + c, a * x2 + b * y2 + c
                ],
                [a, b, c]
            )
            A, B, C = abc[a], abc[b], abc[c]
            udlr = solve(
                [
                    A * u + C, A * d + B * img_size[0] + C,
                    B * l + C, A * img_size[1] + B * r + C
                ],
                [u, d, l, r]
            )
            U, D, L, R = udlr[u], udlr[d], udlr[l], udlr[r]
            #print(udlr)
            points = []  # 两个边界点
            if U >= 0 and U <= img_size[1]:
                points.append((int(U), 0))
                #print(1)
            if D >= 0 and D <= img_size[1]:
                points.append((int(D), img_size[0]))
                #print(2)
            if L >= 0 and L <= img_size[0]:
                points.append((0, int(L)))
                #print(3)
            if R >= 0 and R <= img_size[0]:
                points.append((img_size[1], int(R)))
                #print(4)
            pen = wx.Pen(wx.RED, 1, wx.LONG_DASH)
            dc.SetBrush(brush)
            dc.SetPen(pen)
            dc.DrawLine(points[0], points[1])
            dc.SetPen(pen1)
            dc.DrawLine(M, N)

        def my_x_spline(A, B, C):
            x1, y1, x2, y2, x3, y3 = A[0], A[1], B[0], B[1], C[0], C[1]
            abcd = solve(
                [
                    a * x1 ** 3 + b * x1 ** 2 + c * x1 + d - y1,
                    a * x2 ** 3 + b * x2 ** 2 + c * x2 + d - y2,
                    a * x3 ** 3 + b * x3 ** 2 + c * x3 + d - y3,
                    3 * a * x2 ** 2 + 2 * b * x2 + c - (y1 - y3) / (x1 - x3)
                ],
                [a, b, c, d]
            )
            #print(len(abcd))
            #print("abcd = ", abcd)
            a1, a2, a3, a4 = abcd[a], abcd[b], abcd[c], abcd[d]
            start, end = min(x1, x2, x3), max(x1, x2, x3)
            dx = 5
            xp, xq = int(start), int(start + dx)
            while xq <= end:
                dc.SetBrush(brush)
                dc.SetPen(pen1)
                yp = int(a1 * xp ** 3 + a2 * xp ** 2 + a3 * xp + a4)
                yq = int(a1 * xq ** 3 + a2 * xq ** 2 + a3 * xq + a4)
                dc.DrawLine((xp, yp), (xq, yq))
                xp += dx
                xq += dx

        def my_y_spline(A, B, C):
            y1, x1, y2, x2, y3, x3 = A[0], A[1], B[0], B[1], C[0], C[1]
            abcd = solve(
                [
                    a * x1 ** 3 + b * x1 ** 2 + c * x1 + d - y1,
                    a * x2 ** 3 + b * x2 ** 2 + c * x2 + d - y2,
                    a * x3 ** 3 + b * x3 ** 2 + c * x3 + d - y3,
                    3 * a * x2 ** 2 + 2 * b * x2 + c - (y1 - y3) / (x1 - x3)
                ],
                [a, b, c, d]
            )
            #print(len(abcd))
            #print("abcd = ", abcd)
            a1, a2, a3, a4 = abcd[a], abcd[b], abcd[c], abcd[d]
            start, end = min(x1, x2, x3), max(x1, x2, x3)
            dx = 2
            xp, xq = int(start), int(start + dx)
            while xq <= end:
                dc.SetBrush(brush)
                dc.SetPen(pen1)
                yp = int(a1 * xp ** 3 + a2 * xp ** 2 + a3 * xp + a4)
                yq = int(a1 * xq ** 3 + a2 * xq ** 2 + a3 * xq + a4)
                dc.DrawLine((yp, xp), (yq, xq))
                xp += dx
                xq += dx

        cou = 0
        if refresh_mode == 1:
            cou = cout - 1
        while cou < cout:
            # print(data_base[i])
            i = cou
            if data_base[i][0] == 1:
                if len(data_base[i]) == 2:
                    dc.DrawCircle(data_base[i][1], 1)
                if len(data_base[i]) == 3:
                    my_line(data_base[i][1], data_base[i][2])

            elif data_base[i][0] == 2:
                dc.SetBrush(brush)
                dc.SetPen(pen1)
                if len(data_base[i]) == 2:
                    dc.DrawCircle(data_base[i][1], 1)
                if len(data_base[i]) == 3:
                    R = (
                                (data_base[i][1][0] - data_base[i][2][0]) ** 2 +
                                (data_base[i][1][1] - data_base[i][2][1]) ** 2
                        ) ** 0.5
                    dc.DrawCircle(data_base[i][1], int(R))

            elif data_base[i][0] == 4:
                dc.SetBrush(brush)
                dc.SetPen(pen1)
                if len(data_base[i]) < 4:
                    for j in range(len(data_base[i])):
                        if j == 0:
                            continue
                        dc.DrawCircle(data_base[i][j], 1)
                elif len(data_base[i]) == 4:
                    my_x_spline(data_base[i][1], (data_base[i][2][0], data_base[i][2][1] + 1), data_base[i][3])
                    my_x_spline(data_base[i][1], (data_base[i][2][0], data_base[i][2][1] - 1), data_base[i][3])

            elif data_base[i][0] == 5:
                dc.SetBrush(brush)
                dc.SetPen(pen1)
                if len(data_base[i]) < 4:
                    for j in range(len(data_base[i])):
                        if j == 0:
                            continue
                        dc.DrawCircle(data_base[i][j], 1)
                elif len(data_base[i]) == 4:
                    my_y_spline(data_base[i][1], (data_base[i][2][0], data_base[i][2][1] + 1), data_base[i][3])
                    my_y_spline(data_base[i][1], (data_base[i][2][0], data_base[i][2][1] - 1), data_base[i][3])

            elif data_base[i][0] == 3 and self.erase_cout == 1:
                dc.SetBrush(brush)
                dc.SetPen(pen1)
                dc.DrawCircle(data_base[i][1], 1)

            cou += 1

        for i in range(era_cout):
            if era_base[i][0] == 1:
                # print("era_draw")
                dc.SetBrush(brush2)
                dc.SetPen(pen2)
                # set_pen2()
                R = ((era_base[i][1][0] - era_base[i][2][0]) ** 2 + (
                        era_base[i][1][1] - era_base[i][2][1]) ** 2) ** 0.5
                dc.DrawCircle(era_base[i][1], int(R))
        if refresh_mode == 2:
            refresh_mode = 1



    def on_left_down(self, event):
        #if draw_mode == 1:
        print("Downpos:", event.GetPosition())
        if draw_mode != 0:
            self.status = 1
            self.DownPos = event.GetPosition()
            if draw_mode == 1 and self.line_cout < 2:
                self.line_cout += 1
            if draw_mode == 2 and self.cir_cout < 2:
                self.cir_cout += 1
            if draw_mode == 3 and self.erase_cout < 2:
                self.erase_cout += 1
            if draw_mode == 4 and len(self.Sl3p) < 3:
                self.Sl3p.append(self.DownPos)
            if draw_mode == 5 and self.yslp < 3:
                self.yslp += 1


    def on_left_up(self, event):
        global cout, era_cout
        #if draw_mode == 1:
        if draw_mode != 0:
            self.status = 0
            #line_points[line_cout] = (self.DownPos, self.MovePos)
            if draw_mode == 1:
                if self.line_cout == 1:
                    data_base.append([1, self.DownPos])
                    cout += 1
                elif self.line_cout == 2:
                    data_base[cout-1].append(self.DownPos)
                    self.line_cout = 0

            elif draw_mode == 2:
                if self.cir_cout == 1:
                    data_base.append([2, self.DownPos])
                    cout += 1
                elif self.cir_cout == 2:
                    data_base[cout-1].append(self.DownPos)
                    self.cir_cout = 0

            elif draw_mode == 3:
                if self.erase_cout == 1:
                    data_base.append([3, self.DownPos])
                    cout += 1
                elif self.erase_cout == 2:
                    data_base[cout - 1].append(self.DownPos)
                    era_base.append([1, data_base[cout - 1][1], data_base[cout - 1][2]])
                    era_cout += 1
                    self.erase_cout = 0

            elif draw_mode == 4:
                if len(self.Sl3p) == 1:
                    data_base.append([4, self.Sl3p[0]])
                    cout += 1
                elif len(self.Sl3p) == 2:
                    data_base[cout-1].append(self.Sl3p[1])
                elif len(self.Sl3p) == 3:
                    data_base[cout-1].append(self.Sl3p[2])
                    self.Sl3p.clear()

            elif draw_mode == 5:
                if self.yslp == 1:
                    data_base.append([5, self.DownPos])
                    cout += 1
                elif self.yslp == 2:
                    data_base[cout-1].append(self.DownPos)
                elif self.yslp == 3:
                    data_base[cout-1].append(self.DownPos)
                    self.yslp = 0
            #print(self.DownPos)
            self.Paint()
            #self.Refresh()

    def OnMove(self, event):
        global switch_open, refresh_mode
        if draw_mode != 0:
            self.MovePos = event.GetPosition()
        if pre_step != self.pre:
            #self.Refresh()
            self.Paint()
        if switch_open:
            switch_open = False
            #self.Refresh()
            refresh_mode = 2
            self.Paint()
        self.SetTransparent(win2_trans)

class App(wx.App):
    """Application class."""

    def OnInit(self):
        global img_size
        image = wx.Image('picture.jpg', wx.BITMAP_TYPE_JPEG)
        img = cv2.imread('picture.jpg')
        img_size = img.shape
        # 将图片放入同一个文件夹 参数为文件名
        self.frame = Frame(image)
        self.frame2 = Frame2('Board')
        self.frame.Show()
        #self.frame2.Show(False)
        return True


def main():
    app = App()
    #frame2 = Frame2(None, 'sssss')
    step = 0
    board = [(0, 0)]
    app.MainLoop()


if __name__ == '__main__':
    main()