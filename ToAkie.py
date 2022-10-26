from manimlib import *
import numpy as np
from math import *
from sympy import solve
from sympy.abc import a, b, c, d, u, l, r, e, f, g, h
import random


class test(Scene):
    def construct(self):
        """
        img = ImageMobject(
            "D:\\manim\\manim-master\\assets\\raster_images\\maple.png",
            height=2
        )
        #mob.move_to(np.array([0, 0, 0]))
        #self.play(FadeIn(img))
        img.move_to(np.array([0, 4, 0]))
        img.rotate(90 * DEGREES, axis=LEFT)
        self.add(img)
        now = self.time
        img.add_updater(
            lambda m: m.move_to(np.array([0, 4 - 0.6*(self.time-now), 0])),

        )
        img.add_updater(
            lambda n: n.rotate(cos(self.time - now) * DEGREES * 0.5, axis=LEFT)
        )
        self.wait(15)
        """
        circle = Circle(
            arc_center=np.array([3, 3, 0]),
            radius=2.0,
            stroke_width=3.0,
            stroke_color=RED_C,
            fill_color=BLUE,
            fill_opacity=0.0
        )
        axes = Axes(
            height=8,
            width=14,
            x_range=(-7, 7),
            y_range=(-4, 4)
        )
        axes.add_coordinate_labels()
        lines = VGroup(
            Tex("\\sqrt{x}")
        )
        lines.add(Tex("y"))
        self.play(FadeIn(lines[1]))
        self.embed()


class Lag_Int_Poly(Scene):
    def construct(self):
        P = []
        P.append((0, 0))
        n, minx, maxx, dx = 0, 0, 0, 0.001
        def jisuan(x):
            s = 0
            for i in range(1, n+1):
                I = P[i][1]
                for j in range(1, n+1):
                    if i == j:
                        continue
                    I *= (x - P[j][0]) / (P[i][0] - P[j][0])
                s += I
            return s
        def wucha(x1, x2, x, lx, ly):
            l = ly - jisuan(lx)
            if x <= lx:
                dy = (x - x1) / (lx - x1) * l
            elif x > lx:
                dy = (x2 - x) / (x2 - lx) * l
            return jisuan(x)+dy

        axes = Axes(
            height=8,
            width=14
        )
        axes.add_coordinate_labels()
        self.add(axes)
        n = int(input("输入点的个数："))
        for i in range(1, n+1):
            print("第{}组数据：".format(i))
            x, y = int(input()), int(input())
            if i == 1:
                minx = x
                maxx = x
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            P.append((x, y))
        lx, ly = int(input()), int(input())
        xi = minx
        while xi <= maxx:
            yi = jisuan(xi)
            dot = Dot(radius=0.01).move_to(np.array([xi, yi, 0]))
            self.add(dot)
            xi += dx
        xi = minx
        while xi <= maxx:
            yi = wucha(minx, maxx, xi, lx, ly)
            dot = Dot(radius=0.01, color=BLUE).move_to(np.array([xi, yi, 0]))
            self.add(dot)
            xi += dx

class Lag_Poly(Scene):
    def construct(self):
        axes = Axes(
            height=8,
            width=14
        )
        axes.add_coordinate_labels()
        self.play(FadeIn(axes))
        xy = []
        for i in range(1, 4):
            print("第i组数据：", format(i))
            xi = float(input("数据x："))
            yi = float(input("数据y："))
            xy.append((xi, yi))
        x1, x2, x3 = xy[0][0], xy[1][0], xy[2][0]
        y1, y2, y3 = xy[0][1], xy[1][1], xy[2][1]
        fun1 = axes.get_graph(
            lambda x: y1 * (x - x2) * (x - x3) / ((x1 - x2) * (x1 - x3)) + y2 * (x - x1) * (x - x3) / ((x2 - x1) * (x2 - x3)) + y3 * (x - x1) * (x - x2) / ((x3 - x1) * (x3 - x2))
        )
        self.play(Write(fun1))



#一下为非测试也就是正式部分
global cout, era_cout, era_base, data_base, M_xy, x_mid, y_mid
global cam_x, cam_y, cam_z
cam_x, cam_y, cam_z = 0, 0, 0  #特写cam_z=0, 全局cam_z=80并且rotate PI / 2
cout, era_cout = 0, 0
x_mid, y_mid = 0.0, 0.0
era_base, data_base, M_xy = [], [], [1000, -1000, 1000, -1000]  #x_min,x_max,y_min,y_max

def OnRead(str, dx=0, dy=0):
    #文件名，拼接移动x(默认为0)，拼接移动y(默认为0)
    global cout, era_cout, era_base, data_base, M_xy
    file = open(str, 'r')
    line_cout = 0
    pin = []
    while 1:
        line_cout += 1
        line = file.readline()
        if not line:
            break
        pass
        if line_cout == 1:
            data0 = line.split(' ')
            for i in range(len(data0)):
                if i > 1:
                    pin.append(int(data0[i]))
            if pin and dx != 0 and dy != 0:
                dx = dx - pin[0]
                dy = dy - pin[1]
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
                x0, y0 = int(data0[i-1]) + dx, int(data0[i]) + dy  #拼接点移动
                x, y = 0.05 * x0, -0.05 * y0  #进行坐标系转化
                p = (x, y)
                if x < M_xy[0]:
                    M_xy[0] = x
                if x > M_xy[1]:
                    M_xy[1] = x
                if y < M_xy[2]:
                    M_xy[2] = y
                if y > M_xy[3]:
                    M_xy[3] = y
                data_base[-1].append(p)
                if data0[0] == 3:
                    era_base[-1].append(p)
        cout += 1
    file.close()
    return pin


class draw_pic(Scene):
    global funs, fun_cout
    funs = VGroup()
    fun_cout = 0
    def Paint(self, frame):
        global data_base, era_base, cout, era_cout, x_mid, y_mid
        global cam_x, cam_y, cam_z
        global funs, fun_cout
        def my_line(M, N):
            global M_xy
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
                    A * u + B * M_xy[3] + C, A * d + B * M_xy[2] + C,
                    A * M_xy[0] * B * l + C, A * M_xy[1] + B * r + C
                ],
                [u, d, l, r]
            )
            U, D, L, R = udlr[u], udlr[d], udlr[l], udlr[r]
            points = []  # 两个边界点
            if U >= M_xy[0] and U <= M_xy[1]:
                points.append((U, M_xy[3]))
            if D >= M_xy[0] and D <= M_xy[1]:
                points.append((D, M_xy[2]))
            if L >= M_xy[2] and L <= M_xy[3]:
                points.append((M_xy[0], L))
            if R >= M_xy[2] and R <= M_xy[3]:
                points.append((M_xy[1], R))
            line1 = Line(
                np.array([points[0][0], points[0][1], 0]), np.array([points[1][0], points[1][1], 0])
            )
            line1.set_color(RED)
            self.add(line1)
            line2 = Line(
                np.array([M[0], M[1], 0]), np.array([N[0], N[1], 0])
            )
            line2.set_color(BLUE)
            self.add(line2)

        def my_x_spline(A, B, C):
            global cam_x, cam_y, cam_z
            global funs, fun_cout
            x1, y1, x2, y2, x3, y3 = A[0], A[1], B[0], B[1], C[0], C[1]
            ya, yb = y2 + 0.05, y2 - 0.05
            abcd = solve(
                [
                    a * x1 ** 3 + b * x1 ** 2 + c * x1 + d - y1,
                    a * x2 ** 3 + b * x2 ** 2 + c * x2 + d - ya,
                    a * x3 ** 3 + b * x3 ** 2 + c * x3 + d - y3,
                    3 * a * x2 ** 2 + 2 * b * x2 + c - (y1 - y3) / (x1 - x3)
                ],
                [a, b, c, d]
            )
            efgh = solve(
                [
                    e * x1 ** 3 + f * x1 ** 2 + g * x1 + h - y1,
                    e * x2 ** 3 + f * x2 ** 2 + g * x2 + h - yb,
                    e * x3 ** 3 + f * x3 ** 2 + g * x3 + h - y3,
                    3 * e * x2 ** 2 + 2 * f * x2 + g - (y1 - y3) / (x1 - x3)
                ],
                [e, f, g, h]
            )
            a1, a2, a3, a4 = abcd[a], abcd[b], abcd[c], abcd[d]
            b1, b2, b3, b4 = efgh[e], efgh[f], efgh[g], efgh[h]
            start, end = min(x1, x2, x3), max(x1, x2, x3)
            dx = 0.1
            xp, xq = start, start + dx
            while xq <= end:
                yp = a1 * xp ** 3 + a2 * xp ** 2 + a3 * xp + a4
                yq = a1 * xq ** 3 + a2 * xq ** 2 + a3 * xq + a4
                ym = b1 * xp ** 3 + b2 * xp ** 2 + b3 * xp + b4
                yn = b1 * xq ** 3 + b2 * xq ** 2 + b3 * xq + b4
                line1 = Line(
                    np.array([xp, yp, 0]), np.array([xq, yq, 0])
                )
                line2 = Line(
                    np.array([xp, ym, 0]), np.array([xq, yn, 0])
                )

                if xp == start:
                    ai = [a1, a2, a3, a4]
                    bi = [b1, b2, b3, b4]
                    to_isolate = ["y", "x"]
                    fun_begin = " \\sqrt{ "
                    fun_end = " }"
                    f1_x, f2_x = " (y ", " (y "
                    for i in range(4):
                        cishu = 3 - i
                        a_i = int(-1 * ai[i] * 100) / 100
                        if a_i < 0:
                            aii = str(a_i)
                            f1_x = f1_x + aii
                        if a_i >= 0:
                            aii = "+" + str(a_i)
                            f1_x = f1_x + aii
                        if cishu == 1:
                            f1_x = f1_x + " \\cdot x "
                        if cishu > 1:
                            f1_x = f1_x + " \\cdot x^{ " + str(cishu) + " } "
                    f1_x = f1_x + " ) "
                    for i in range(4):
                        cishu = 3 - i
                        b_i = int(int(-1 * bi[i] * 100) / 100)
                        if b_i < 0:
                            bii = str(b_i)
                            f2_x = f2_x + bii
                        if b_i >= 0:
                            bii = "+" + str(b_i)
                            f2_x = f2_x + bii
                        if cishu == 1:
                            f2_x = f2_x + " \\cdot x "
                        if cishu > 1:
                            f2_x = f2_x + " \\cdot x^{ " + str(cishu) + " } "
                    f2_x = f2_x + " ) "
                    #fun_s = "f_{ " + str(fun_cout) + " } (x,y): " + fun_begin + f1_x + " \\cdot " + f2_x +fun_end
                    fun_s = "f_{ " + str(fun_cout) + " } (x,y): " + f1_x + " \\cdot " + f2_x
                    fun = Tex(fun_s, isolate=[*to_isolate])
                    fun.set_color(BLUE)
                    funs.add(fun)
                    fun_cout += 1
                    funs[fun_cout-1].set_color_by_tex_to_color_map({
                        "x": RED_A,
                        "y": TEAL,
                    })
                    if fun_cout == 1:
                        self.play(Write(funs[fun_cout-1]))
                    if fun_cout > 1:
                        self.play(
                            ReplacementTransform(
                                funs[fun_cout-2], funs[fun_cout-1],
                            )
                        )
                    """
                    #作图过程取消注释
                    frame.clear_updaters()
                    cam_x, cam_y = xq, (yq + yn) / 2
                    self.play(frame.animate.move_to(np.array([cam_x, cam_y, cam_z])))
                    frame.add_updater(
                        lambda m: m.move_to(np.array([cam_x, cam_y, cam_z]))
                    )
                    """

                """
                #作图过程取消注释
                cam_x, cam_y = xq, (yq + yn) / 2
                line1.set_color(BLUE)
                line2.set_color(BLUE)
                self.add(line1)
                self.add(line2)
                """
                xp += dx
                xq += dx
                self.wait(0.05)

        def my_y_spline(A, B, C):
            global funs, fun_cout
            global cam_x, cam_y, cam_z
            x1, y1, x2, y2, x3, y3 = A[0], A[1], B[0], B[1], C[0], C[1]
            xa, xb = x2 + 0.05, x2 - 0.05
            abcd = solve(
                [
                    a * y1 ** 3 + b * y1 ** 2 + c * y1 + d - x1,
                    a * y2 ** 3 + b * y2 ** 2 + c * y2 + d - xa,
                    a * y3 ** 3 + b * y3 ** 2 + c * y3 + d - x3,
                    3 * a * y2 ** 2 + 2 * b * y2 + c - (x1 - x3) / (y1 - y3)
                ],
                [a, b, c, d]
            )
            efgh = solve(
                [
                    e * y1 ** 3 + f * y1 ** 2 + g * y1 + h - x1,
                    e * y2 ** 3 + f * y2 ** 2 + g * y2 + h - xb,
                    e * y3 ** 3 + f * y3 ** 2 + g * y3 + h - x3,
                    3 * e * y2 ** 2 + 2 * f * y2 + g - (x1 - x3) / (y1 - y3)
                ],
                [e, f, g, h]
            )
            a1, a2, a3, a4 = abcd[a], abcd[b], abcd[c], abcd[d]
            b1, b2, b3, b4 = efgh[e], efgh[f], efgh[g], efgh[h]
            start, end = min(y1, y2, y3), max(y1, y2, y3)
            dy = 0.1
            yp, yq = start, start + dy
            while yq <= end:
                xp = a1 * yp ** 3 + a2 * yp ** 2 + a3 * yp + a4
                xq = a1 * yq ** 3 + a2 * yq ** 2 + a3 * yq + a4
                xm = b1 * yp ** 3 + b2 * yp ** 2 + b3 * yp + b4
                xn = b1 * yq ** 3 + b2 * yq ** 2 + b3 * yq + b4
                line1 = Line(
                    np.array([xp, yp, 0]), np.array([xq, yq, 0])
                )
                line2 = Line(
                    np.array([xm, yp, 0]), np.array([xn, yq, 0])
                )

                if yp == start:
                    ai = [a1, a2, a3, a4]
                    bi = [b1, b2, b3, b4]
                    to_isolate = ["y", "x"]
                    fun_begin = "\\sqrt{ "
                    fun_end = " }"
                    f1_y, f2_y = " (x ", " (x "
                    for i in range(4):
                        cishu = 3 - i
                        a_i = int(-1 * ai[i] * 100) / 100
                        if a_i < 0:
                            aii = str(a_i)
                            f1_y = f1_y + aii
                        if a_i >= 0:
                            aii = "+" + str(a_i)
                            f1_y = f1_y + aii
                        if cishu == 1:
                            f1_y = f1_y + " \\cdot y "
                        if cishu > 1:
                            f1_y = f1_y + " \\cdot y^{ " + str(cishu) + " } "
                    f1_y = f1_y + " ) "
                    for i in range(4):
                        cishu = 3 - i
                        b_i = int(-1 * bi[i] * 100) / 100
                        if b_i < 0:
                            bii = str(b_i)
                            f2_y = f2_y + bii
                        if b_i >= 0:
                            bii = "+" + str(b_i)
                            f2_y = f2_y + bii
                        if cishu == 1:
                            f2_y = f2_y + " \\cdot y "
                        if cishu > 1:
                            f2_y = f2_y + " \\cdot y^{ " + str(cishu) + " } "
                    f2_y = f2_y + " ) "
                    #fun_s ="f_{" + str(fun_cout) + "} (x,y): " + fun_begin + f1_y + " \\cdot " + f2_y + fun_end
                    fun_s = "f_{" + str(fun_cout) + "} (x,y): " + f1_y + " \\cdot " + f2_y
                    fun = Tex(fun_s, isolate=[*to_isolate])
                    fun.set_color(BLUE)
                    funs.add(fun)
                    fun_cout += 1
                    funs[fun_cout - 1].set_color_by_tex_to_color_map({
                        "x": PURPLE_A,
                        "y": RED_A,
                    })
                    if fun_cout == 1:
                        self.play(Write(funs[fun_cout - 1]))
                    if fun_cout > 1:
                        self.play(
                            ReplacementTransform(
                                funs[fun_cout - 2], funs[fun_cout - 1],
                            )
                        )
                    """
                    #作图过程取消注释
                    frame.clear_updaters()
                    cam_x, cam_y = (xq + xn) / 2, yq
                    self.play(frame.animate.move_to(np.array([cam_x, cam_y, cam_z])))
                    frame.add_updater(
                        lambda m: m.move_to(np.array([cam_x, cam_y, cam_z]))
                    )
                    """

                """
                #作图过程取消注释
                cam_x, cam_y = (xq + xn) / 2, yq
                line1.set_color(BLUE)
                line2.set_color(BLUE)
                self.add(line1)
                self.add(line2)
                """
                yp += dy
                yq += dy
                self.wait(0.05)

        cou = 0
        while cou < cout:
            i = cou
            if data_base[i][0] == 1:
                my_line(data_base[i][1], data_base[i][2])

            elif data_base[i][0] == 2:
                R = (
                        (data_base[i][1][0] - data_base[i][2][0]) ** 2 +
                        (data_base[i][1][1] - data_base[i][2][1]) ** 2
                    ) ** 0.5
                circle = Circle(
                    arc_center=np.array([data_base[i][1][0], data_base[i][1][1], 0]),
                    radius=R,
                    stroke_width=2.0,
                    stroke_color=BLUE,
                    fill_color=BLACK,
                    fill_opacity=0.0
                )
                self.add(circle)

            elif data_base[i][0] == 4:
                my_x_spline(data_base[i][1], (data_base[i][2][0], data_base[i][2][1]), data_base[i][3])

            elif data_base[i][0] == 5:
                my_y_spline(data_base[i][1], (data_base[i][2][0], data_base[i][2][1]), data_base[i][3])

            cou += 1

        for i in range(era_cout):
            if era_base[i][0] == 1:
                R = ((era_base[i][1][0] - era_base[i][2][0]) ** 2 + (
                        era_base[i][1][1] - era_base[i][2][1]) ** 2) ** 0.5
                circle = Circle(
                    arc_center=np.array([data_base[i][1][0], data_base[i][1][1], 0]),
                    radius=R,
                    stroke_width=2.0,
                    stroke_color=RED_C,
                    fill_color=BLACK,
                    fill_opacity=0.9
                )
                self.add(circle)


    def test_Paint(self):
        global cout, era_cout, era_base, data_base
        for i in range(cout):
            for j in range(len(data_base[i])):
                if j == 0:
                    continue
                dot = Dot(colour=BLUE).move_to(
                    np.array([data_base[i][j][0], data_base[i][j][1], 0])
                )
                self.add(dot)

    def construct(self):
        #前置工作
        global funs, fun_cout
        global cout, era_cout, era_base, data_base, x_mid, y_mid
        global cam_x, cam_y, cam_z
        self.pin1 = [0, 0]
        self.pin1 = OnRead("Readfile1.txt", self.pin1[0], self.pin1[1])
        OnRead("Readfile2.txt", self.pin1[0], self.pin1[1])

        #动画部分
        x_mid, y_mid = (M_xy[0] + M_xy[1]) / 2, (M_xy[2] + M_xy[3]) / 2   #16.225, -35.2
        cam_x, cam_y = x_mid, y_mid
        frame = self.camera.frame
        self.play(frame.animate.rotate(PI / 6))
        #self.play(frame.animate.move_to(np.array([cam_x, cam_y, cam_z]))) #作图过程取消注释
        #self.play(frame.animate.rotate(PI / 2))  #全局视图取消注释
        """
        #全局视图取消注释
        screen = Rectangle(
            height=8,
            width=14,
            opacity=0.0,
            stroke_color=RED_C,
            stroke_width=20
        ).move_to(np.array([0, 0, 0]))
        screen.add_updater(
            lambda n: n.move_to(np.array([cam_x, cam_y, 0]))
        )
        self.add(screen)
        """
        self.play(frame.animate.shift(OUT*13))
        self.Paint(frame)  #跟随函数(全局视图变量为screen，局部特写为frame)
        self.wait(2)
        #self.play(FadeOut(funs[-1]))
        #self.play(FadeOut(screen)) #全局视图取消注释
        #self.wait(3)

        #self.embed()


class S1(Scene):
    def construct(self):
        axes = Axes(
            height=8,
            width=14,
            x_range=(-7, 7),
            y_range=(-4, 4)
        )
        axes.add_coordinate_labels()
        t1 = VGroup(
            #Text("V2沿y轴正方向上的分速度Vy:", color=WHITE, font="黑体", font_size=35, t2c=to_t2c)
            Text("应用画图", color=WHITE, font="黑体", font_size=40, t2c={"画图": ORANGE}),

            Text("问题转换", color=WHITE, font="黑体", font_size=40),
        )

        t2 = Text(
            """
            找到一个通用方法，构造出一个方程\n
            尽可能地去拟合不规则图线
            """,
            color=WHITE, font="黑体", font_size=40,
            t2c={"通用": RED_B, "方程": BLUE, "图线": TEAL_C}
        )
        t3 = VGroup(

            Text("直线", font="黑体", font_size=40),

            Tex("A \\cdot x + B \\cdot y + C = 0", color=BLUE),

            Text("弧线和多余部分？", color=WHITE, font="黑体", font_size=40, t2c={"弧线": BLUE, "多余": TEAL_C})
        )
        t1.arrange(DOWN, buff=LARGE_BUFF)
        t3.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(t1[0]))
        self.wait(2)
        self.play(ReplacementTransform(t1[0].copy(), t1[1]))
        self.wait(2)
        #self.play(FadeOut(t1))
        self.play(ReplacementTransform(t1, t2))
        self.wait(2)
        self.play(ReplacementTransform(t2, t3[0]))
        self.wait(2)
        for i in range(2):
            self.play(ReplacementTransform(t3[i].copy(), t3[i+1]))
            self.wait(2)
        self.play(FadeOut(t3))
        self.wait()
        self.play(Write(axes))
        self.wait()
        frame = self.camera.frame
        self.play(frame.animate.shift(UP * 2))
        x1, x2, x3 = -3, 1, 3
        y1, y2, y3 = 1, 3.5, 2.5
        A = Dot(point=np.array([x1, y1, 0]), color=RED)
        B = Dot(point=np.array([x2, y2, 0]), color=RED)
        C = Dot(point=np.array([x3, y3, 0]), color=RED)
        A_label = Tex("A(x_1, y_1 )")
        B_label = Tex("B(x_2, y_2 )")
        C_label = Tex("C(x_3, y_3 )")
        always(A_label.next_to, A, UP)
        always(B_label.next_to, B, UP)
        always(C_label.next_to, C, UP)
        self.wait()
        self.play(
            ShowCreation(A),
            FadeIn(A_label)
        )
        self.play(
            ShowCreation(B),
            FadeIn(B_label)
        )
        self.play(
            ShowCreation(C),
            FadeIn(C_label)
        )
        self.wait(2)
        self.play(FadeOut(VGroup(A_label, B_label, C_label)))
        self.wait(2)
        line = Line(np.array([x1, y1, 0]), np.array([x3, y3, 0]), buff=-2.0, color=BLUE)
        self.play(ShowCreation(line))
        self.wait(2)
        self.play(line.animate.shift(UP * 1.5))
        self.wait(2)
        self.play(FadeOut(line))
        self.wait(2)
        abcd = solve(
            [
                a * x1 ** 3 + b * x1 ** 2 + c * x1 + d - y1,
                a * x2 ** 3 + b * x2 ** 2 + c * x2 + d - y2,
                a * x3 ** 3 + b * x3 ** 2 + c * x3 + d - y3,
                3 * a * x2 ** 2 + 2 * b * x2 + c - (y1 - y3) / (x1 - x3)
            ],
            [a, b, c, d]
        )
        #print(abcd)
        fun = axes.get_graph(
            lambda x: abcd[a] * x ** 3 + abcd[b] * x ** 2 + abcd[c] * x + abcd[d],
            color=BLUE
        )
        self.play(ShowCreation(fun))
        fun_tex = Tex("y = a x^3 + b x^2 + cx + d").move_to(np.array([0, 4.5, 0]))
        self.wait(2)
        self.play(GrowFromEdge(fun_tex, DOWN))
        self.wait(2)
        self.play(FadeOut(fun_tex))
        B1 = Dot(point=B.get_center() + UP * 0.5, color=ORANGE)
        B1_label = Tex("B_1 (x_2, y_2 + \\lambda )")
        always(B1_label.next_to, B1, UP)
        B2 = Dot(point=B.get_center() + DOWN * 0.5, color=ORANGE)
        B2_label = Tex("B_2 (x_2, y_2 - \\lambda )")
        always(B2_label.next_to, B2, DOWN)
        self.play(
            FadeIn(B1),
            FadeIn(B1_label)
        )
        self.play(
            FadeIn(B2),
            FadeIn(B2_label)
        )
        self.wait(2)
        self.play(FadeOut(VGroup(B1_label, B2_label)))
        self.wait(2)
        abcd = solve(
            [
                a * x1 ** 3 + b * x1 ** 2 + c * x1 + d - y1,
                a * x2 ** 3 + b * x2 ** 2 + c * x2 + d - y2 - 0.5,
                a * x3 ** 3 + b * x3 ** 2 + c * x3 + d - y3,
                3 * a * x2 ** 2 + 2 * b * x2 + c - (y1 - y3) / (x1 - x3)
            ],
            [a, b, c, d]
        )
        fun1 = axes.get_graph(
            lambda x: abcd[a] * x ** 3 + abcd[b] * x ** 2 + abcd[c] * x + abcd[d],
            color=PURPLE_A
        )
        abcd = solve(
            [
                a * x1 ** 3 + b * x1 ** 2 + c * x1 + d - y1,
                a * x2 ** 3 + b * x2 ** 2 + c * x2 + d - y2 + 0.5,
                a * x3 ** 3 + b * x3 ** 2 + c * x3 + d - y3,
                3 * a * x2 ** 2 + 2 * b * x2 + c - (y1 - y3) / (x1 - x3)
            ],
            [a, b, c, d]
        )
        fun2 = axes.get_graph(
            lambda x: abcd[a] * x ** 3 + abcd[b] * x ** 2 + abcd[c] * x + abcd[d],
            color=PURPLE_A
        )
        self.play(ShowCreation(VGroup(fun1, fun2), run_time=2))
        self.wait(2)
        Fun_tex = Tex(
            """
            ( y - a_1 \\cdot x^3 - a_2 \\cdot x^2 - a_3 \\cdot x - a_4 ) \\cdot 
            ( y - b_1 \\cdot x^3 - b_2 \\cdot x^2 - b_3 \\cdot x - b_4 ) = 0
            """
        ).move_to(np.array([0, 5.5, -5]))
        self.play(GrowFromEdge(Fun_tex, DOWN))
        self.wait(2)
        self.play(FadeOut(Fun_tex))
        self.wait(2)
        dl1 = DashedLine(A.get_center()+UP*5, A.get_center()+DOWN*5, color=TEAL_B, dash_length=0.3)
        dl2 = DashedLine(C.get_center()+UP*5, C.get_center()+DOWN*5, color=TEAL_B, dash_length=0.3)
        self.play(ShowCreation(VGroup(dl1, dl2), run_time=2))
        self.wait(2)


class S2(Scene):
    def construct(self):
        t1 = VGroup(
            TexText(
                """
                if $ f_{k}(x,y) $ is determined by three points \n
                $A(x_1 ,y_1),B(x_2,y_2),C(x_3,y_3)$ (x1<x2<x3)\n
                What is the function showing the middle part of the curve?
                """,
            ),
            #若笔触弧线 由三个关键点 控制 求只显示中间“笔触”部分($ x \in (x1,x2) $)的图线方程.

            Text(
                "联想到数轴上有关”距离“的性质",
                color=GREY_A, font="黑体", font_size=40,
                t2c={"数轴": PURPLE_A, "距离": ORANGE})
        )
        t1.arrange(DOWN, buff=LARGE_BUFF)
        self.play(FadeIn(t1[0]))
        self.wait(2)
        self.play(GrowFromEdge(t1[1], UP))
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)
        aro = Arrow(np.array([-6.5, 0, 0]), np.array([6.5, 0, 0]), width=0.2)
        aro.set_color(BLUE)
        self.play(GrowArrow(aro))
        self.wait(2)
        A = Dot(np.array([-2, 0, 0]), radius=0.2, color=TEAL_C)
        A_label = Tex("A(a,0)").move_to(A.get_center()+UP)
        B = Dot(np.array([2, 0, 0]), radius=0.2, color=PURPLE_A)
        B_label = Tex("B(b,0)").move_to(B.get_center()+UP)
        self.play(ShowCreation(A), GrowFromEdge(A_label, DOWN))
        self.play(ShowCreation(B), GrowFromEdge(B_label, DOWN))
        self.wait(2)
        C = Dot(radius=0.2, fill_color=RED_B)
        C.move_to(np.array([-6, 0, 0]))
        C_label = Tex("C(x,0)")
        always(C_label.next_to, C, UP)
        self.add(C)
        self.play(FadeIn(VGroup(C_label)))
        self.wait(2)
        self.play(FadeOut(VGroup(A_label, B_label, C_label)))
        self.wait(2)
        la = Line(C.get_center(), A.get_center(), color=GREEN_C)
        la.add_updater(
            lambda m: m.put_start_and_end_on(C.get_center(), A.get_center())
        )
        lb = Line(C.get_center(), B.get_center(), color=GOLD_A)
        lb.add_updater(
            lambda n: n.put_start_and_end_on(C.get_center(), B.get_center())
        )
        self.add(la, lb)
        brace1 = always_redraw(Brace, la, DOWN)
        text1, number1 = label1 = VGroup(
            Tex("L_A = "),
            DecimalNumber(
                0,
                show_ellipsis=False,  # 省略号
                num_decimal_places=2,  # 小数位数
                include_sign=False,  # 是否加符号
            )
        ).set_width(1)
        label1.arrange(RIGHT)
        always(label1.next_to, brace1, DOWN)
        f_always(number1.set_value, la.get_length)
        brace2 = always_redraw(Brace, lb, UP)
        text2, number2 = label2 = VGroup(
            Tex("L_B = "),
            DecimalNumber(
                0,
                show_ellipsis=False,  # 省略号
                num_decimal_places=2,  # 小数位数
                include_sign=False,  # 是否加符号
            )
        ).set_width(1)
        label2.arrange(RIGHT)
        always(label2.next_to, brace2, UP)
        f_always(number2.set_value, lb.get_length)
        text, number = label = VGroup(
            Tex(
                """
                \\left | \\left | x - a \\right | - \\left | x - b \\right | \\right | = 
                \\left | L_A - L_B \\right | = 
                """
            ),
            DecimalNumber(
                0,
                show_ellipsis=False,  # 省略号
                num_decimal_places=2,  # 小数位数
                include_sign=False,  # 是否加符号
            )
        )
        label.arrange(RIGHT)
        l = Line(A.get_center()+DOWN*11, DOWN*11+A.get_center()+LEFT*(abs(la.get_length()-lb.get_length())))
        l.add_updater(
            lambda m: l.set_length(abs(la.get_length()-lb.get_length()))
        )
        self.add(l)
        f_always(number.set_value, l.get_length)
        label.move_to(np.array([0, -2, 0]))
        self.play(FadeIn(VGroup(label1, brace1, label2, brace2), run_time=2))
        self.wait(2)
        self.play(GrowFromEdge(label, UP))
        self.wait(2)
        now = self.time
        self.play(self.camera.frame.animate.shift(OUT * 3))
        self.wait(2)
        C.add_updater(
            lambda a: a.move_to(np.array([-6 + 0.5 * (self.time - now), 0, 0])),
        )
        while abs(C.get_center()[0]-6.5) > 0.1:
            self.wait(0.1)
        self.wait(2)


class S3(Scene):
    def construct(self):
        to_isolate = ["x", "y"]
        t1 = VGroup(
            TexText(
                """
                If we need to limit the X domain($ D_x $) of the curve\n
                Then it can be approximately expressed by the function:
                """
            ),

            Tex(
                """
                g_k (x,y) = 
                ( \\left | \\left | x - x_1 \\right | - \\left | x - x_3 \\right | \\right | - 
                \\left | x_1 - x_3 \\right | ) \\cdot f_k (x,y) 
                + \\frac{ \\varepsilon (x) }{ (x-x1) \\cdot (x-x3) }
                """,
                color=BLUE
            ),

            Tex(
                """
                \\frac{ \\varepsilon (x) }{
                ( \\left | \\left | x - x_1 \\right | - \\left | x - x_3 \\right | \\right | - 
                \\left | x_1 - x_3 \\right | ) \\cdot (x-x1) \\cdot (x-x3) }
                \\ll f_k (x,y)
                """,
                color=BLUE
            ),

            TexText(
                """
                Specially,$ \\varepsilon (x) $ can be converted to a minimal quantity $ \\varepsilon $
                """
            )
        ).arrange(DOWN, buff=LARGE_BUFF)
        t2 = TexText(
            """
            So the whole curved can be expressed by the function:
            """
        )
        t3 = Tex(" \\prod_{ k = 1 }^{ n } g_k (x,y) = 0  ")
        t3 = VGroup(t2, t3).arrange(DOWN, buff=LARGE_BUFF)
        for i in range(4):
            if i == 0 or i == 3:
                continue
            t1[i].set_color_by_tex_to_color_map({
                "x": TEAL_C,
                "y": BLUE,
            })
        play_kw = {"run_time": 2}
        self.play(self.camera.frame.animate.shift(OUT*3))
        self.play(FadeIn(t1[0]), **play_kw)
        self.wait(2)
        for i in range(1, 4):
            self.play(Write(t1[i]), **play_kw)
            self.wait(2)
        self.play(FadeOut(t1))
        self.wait(2)
        self.play(Write(t3[0]), **play_kw)
        self.wait(2)
        self.play(Write(t3[1]), **play_kw)
        self.wait(2)


class S0(Scene):
    def construct(self):
        t1 = VGroup(
            Text("滑稽不堪", color=GREY_A, font="黑体", font_size=40,
                t2c={"滑": BLUE_A, "稽": BLUE_B, "不": BLUE_C, "堪": BLUE_D}),

            Text("?", color=RED_C, font="黑体", font_size=40)
        ).arrange(RIGHT, buff=LARGE_BUFF)
        self.play(
            GrowFromEdge(t1[0], RIGHT),
            GrowFromEdge(t1[1], LEFT)
        )
        self.wait(2)
        self.play(Uncreate(t1))
        self.wait(2)
        axes = Axes(
            height=8,
            width=14,
            x_range=(-7, 7),
            y_range=(-4, 4)
        )
        axes.add_coordinate_labels()
        circle1 = Circle(
            radius=1.5,
            stroke_color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.9
        ).move_to(np.array([-3, 1, 0]))
        sj = Polygon(
            np.array([0, 0, 0]),
            np.array([3, 0, 0]),
            np.array([2, 3, 0])
        ).set_fill(color=RED_B, opacity=0.9)
        squre = Square(side_length=2.0).move_to(np.array([0, -2, 0]))
        squre.set_fill(color=GOLD_B, opacity=0.9)
        self.play(Write(axes))
        self.wait(2)
        group = VGroup(circle1, sj, squre)
        for mem in group:
            self.play(DrawBorderThenFill(mem))
        self.wait(2)
        circle2 = Circle(
            radius=2.0,
            stroke_color=RED_C,
            fill_color=BLACK,
            fill_opacity=0.0
        ).move_to(np.array([-1, 0, 0]))
        circle = Circle(
            radius=2.0,
            stroke_color=RED_C,
            fill_color=BLACK,
            fill_opacity=1.0
        ).move_to(np.array([-1, 0, 0]))
        self.play(ShowCreation(circle2))
        self.wait(2)
        fun1 = Tex("\\sqrt{ ( x + 1 )^2 + y^2 - 4 } = 0").move_to(np.array([0, 3, 0]))
        fun1.set_color(BLUE_C)
        self.play(GrowFromEdge(fun1, DOWN))
        self.wait(2)
        self.play(ReplacementTransform(circle2, circle))
        self.wait(2)
        fun2 = Tex("x^2 + y^2 \\ge 4").move_to(np.array([0, -0.5, 0]))
        fun2.set_color(PURPLE_A)
        self.play(Write(fun2))
        self.wait(2)

class S4(Scene):
    def construct(self):
        t1 = Text("Preparation is already done")
        t2 = Text("Try to draw something", height=1)
        self.play(Write(t1, run_time=3))
        self.wait(2)
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(t1, t2, **kw))
        self.wait(2)



