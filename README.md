# MathematicsRoom
some mathematic problem using computer to help
# One equation (equation drawer)

You can see the video generated by these programmes On Bilibili.

**https://www.bilibili.com/video/BV1PR4y1H7NU/**

This is a project which provides users with an interactive window to freely draw the graphics composed of functions


这里提供的Readfile.txt 中的数据是视频BV1z44y1s7fT中的部分绘图数据（另一部分已经被处理过了所以搬不过来了

 include "wxPython", "opencv2", "sympy" 
 
 可以用中文吗（行那还是用中文写吧 

首先

以上的包需要自行安装(line 4)

然后是使用部分

首先在与main.py同级文件夹放一张“不大不小”的 picture.jpg 不要太小不然按钮会挤在一起，太大窗口 会撑不下 。

再运行main.py

你会发现有两个窗口，一个窗口是菜单和picture对应的图片(窗口1)，另一个窗口是绘制窗(窗口2)，用来临摹

窗口1有7个按钮(其实是6个，因为“下一步”按钮是假的qwq，感觉没啥用就没写，所以请“上一步”前“三思而后行”)

控件功能介绍：

“上一步”：字面意思，按下之后请将鼠标在窗口2上晃一下（不然不会刷新

“下一步”：刚刚说了，假的

“直线工具line”：用来绘制直线，红色部分是你不希望表示的区域(多余的部分)，黑色部分是你希望它表示的部分(如果不知道是什么意思的可以看我以前的视频BV1N44y1y7ro

“圆工具circle”：字面意思，用来画圆

“圆外显示工具era”：用来剔除画出圆内的定义域，是“三个工具之一”(如果不知道是什么意思的可以看我以前的视频BV1N44y1y7ro

“三点插值曲线x_spline”：用来画出视频BV1z44y1s7fT中所说的以x为自变量的“笔触弧线”（注意是以x为自变量！所以请别用它来画太“竖”的弧线

“三点插值曲线y_spline”：用来画出视频BV1z44y1s7fT中所说的以y为自变量的“笔触弧线”（注意是以x为自变量！所以请别用它来画太“横”的弧线

“滑动条”：用来调节窗口2的不透明度，越向下越不透明



菜单功能介绍：(窗口1左上角的file)

“Open”：打开同文件夹下名为 “Readfile.txt” 的文件，根据其中的 绘图数据 读取绘图

“Out”：将当前窗口2上的 绘图数据 保存在同文件夹中名为“Outfile.txt” 的文件(自带有最多绘制3笔一次自动保存的功能，具体细节参考main.py)

“About”：字面意思

“Exit”：字面意思

【注：“Out”之后可以将“Outfile.txt”中的内容复制到“Readfile.txt”然后“Open”就可以继续之前的进度绘制或是查看 绘图数据 所表示的图形】

【窗口2的刷新是以鼠标移动为准的，所以若干了什么发现没动静，请试图用鼠标在窗口2上滑一滑】
