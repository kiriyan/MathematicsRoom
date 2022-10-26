import math
import numpy as np
from manimlib import *

#背景色 -c LightYellow (255, 255, 224)

class example1(Scene):

    def construct(self):

        axes = Axes(
            x_range=(0, 7),
            y_range=(0, 7),
            height=6,
            width=6,
            axis_config={
                "stroke_color": BLACK,
                "stroke_width": 4,
            },
            y_axis_config={
                "include_tip": True,
            }
        )
        axes.add_coordinate_labels(
            x_values=[3, 4, 5],
            y_values=[4, 5, 6],
            color=BLACK
        )

        self.play(Write(axes, lag_ratio=0.01, run_time=2))
        dot1 = Dot(color=RED)
        dot1.move_to(axes.c2p(4, 5))
        dot2 = Dot(color=RED)
        dot2.move_to(axes.c2p(5, 6))
        dot3 = Dot(color=RED)
        dot3.move_to(axes.c2p(4, 6))
        dot4 = Dot(color=RED)
        dot4.move_to(axes.c2p(5, 5))
        #self.play(dot.animate.move_to(axes.c2p(3, 2)))
        h1_line = always_redraw(lambda: axes.get_h_line(dot1.get_left()))
        #h1_line.set_stroke(BLUE_E, width=4)
        v1_line = always_redraw(lambda: axes.get_v_line(dot1.get_bottom()))
        h2_line = always_redraw(lambda: axes.get_h_line(dot2.get_left()))
        v2_line = always_redraw(lambda: axes.get_v_line(dot2.get_bottom()))
        h3_line = always_redraw(lambda: axes.get_h_line(dot3.get_left()))
        v3_line = always_redraw(lambda: axes.get_v_line(dot3.get_bottom()))
        h4_line = always_redraw(lambda: axes.get_h_line(dot4.get_left()))
        v4_line = always_redraw(lambda: axes.get_v_line(dot4.get_bottom()))
        self.play(FadeIn(dot1, scale=0.05))
        self.play(FadeIn(dot2, scale=0.05))
        self.play(FadeIn(dot3, scale=0.05))
        self.play(FadeIn(dot4, scale=0.05))
        hv_line = VGroup(h1_line, v1_line, h2_line, v2_line, h3_line, v3_line, h4_line, v4_line)
        hv_line.set_stroke(BLUE_E, width=4)
        self.play(Write(hv_line, lag_ratio=0.01, run_time=4))
        fun1 = axes.get_graph(
            lambda x: x,
            color=RED,
        )
        fun2 = axes.get_graph(
            lambda x: x + 0.5,
            color=RED,
        )
        self.wait()
        self.play(ShowCreation(fun1))
        self.wait()
        self.play(ReplacementTransform(fun1, fun2))
        self.wait()
        dot5 = Dot(color=RED)
        dot5.move_to(axes.c2p(4.5, 5))
        dot6 = Dot(color=RED)
        dot6.move_to(axes.c2p(5, 5.5))
        self.play(FadeIn(dot5, scale=0.05))
        self.play(FadeIn(dot6, scale=0.05))

    def xline(m, n, k):
        linexx.clear()
        pd = 1
        dire = k / abs(k)
        x1 = float(m)
        x2 = float(m + dire * 0.3)
        if abs(k) > 1:
            pd = 0
            y0 = (n + dire * 0.4)
            x0 = float(m + (y0 - n) / k)
            linex1 = axes.get_graph(
                lambda x: k * (x - m) + n,
                x_range=(min(m, m + dire * 7), max(m, m + dire * 7)),
                color=ORANGE,
            )
            self.play(FadeIn(linex1))
        for i in range(0, 14):
            linexx.append(1)
            if pd == 1:
                linexx[i] = axes.get_graph(
                    lambda x: k * (x - m) + n,
                    x_range=(min(x1, x2), max(x1, x2)),
                    color=ORANGE,
                )
                x1 += dire * 0.5
                x2 += dire * 0.5
            if pd == 0:
                linexx[i] = axes.get_graph(
                    lambda x: -1 / k * (x - x0) + y0,
                    x_range=(x0 - 0.15, x0 + 0.15),
                    color=ORANGE,
                )
                y0 += dire * 0.5
                x0 = m + (y0 - n) / k
                linexx[i].set_stroke(BLACK, width=10)
            self.add(linexx[i])

class example2(Scene):

    def construct(self):

        axes = Axes(
            x_range=(0, 7),
            y_range=(0, 7),
            height=6,
            width=6,
            axis_config={
                "stroke_color": BLACK,
                "stroke_width": 4,
            },
            y_axis_config={
                "include_tip": True,
            }
        )
        axes.add_coordinate_labels(
            x_values=[4, 5, 6],
            y_values=[4, 5, 6],
            color=BLACK
        )

        self.play(Write(axes, lag_ratio=0.01, run_time=2))
        dot1 = Dot(color=RED)
        dot1.move_to(axes.c2p(5, 5))
        dot2 = Dot(color=RED)
        dot2.move_to(axes.c2p(5, 6))
        dot3 = Dot(color=RED)
        dot3.move_to(axes.c2p(6, 5))
        dot4 = Dot(color=RED)
        dot4.move_to(axes.c2p(6, 6))
        #self.play(dot.animate.move_to(axes.c2p(3, 2)))
        h1_line = always_redraw(lambda: axes.get_h_line(dot1.get_left()))
        #h1_line.set_stroke(BLUE_E, width=4)
        v1_line = always_redraw(lambda: axes.get_v_line(dot1.get_bottom()))
        h2_line = always_redraw(lambda: axes.get_h_line(dot2.get_left()))
        v2_line = always_redraw(lambda: axes.get_v_line(dot2.get_bottom()))
        h3_line = always_redraw(lambda: axes.get_h_line(dot3.get_left()))
        v3_line = always_redraw(lambda: axes.get_v_line(dot3.get_bottom()))
        h4_line = always_redraw(lambda: axes.get_h_line(dot4.get_left()))
        v4_line = always_redraw(lambda: axes.get_v_line(dot4.get_bottom()))
        self.play(FadeIn(dot1, scale=0.05))
        self.play(FadeIn(dot2, scale=0.05))
        self.play(FadeIn(dot3, scale=0.05))
        self.play(FadeIn(dot4, scale=0.05))
        hv_line = VGroup(h1_line, v1_line, h2_line, v2_line, h3_line, v3_line, h4_line, v4_line)
        hv_line.set_stroke(BLUE_E, width=4)
        self.play(Write(hv_line, lag_ratio=0.01, run_time=4))
        fun1 = axes.get_graph(
            lambda x: x,
            color=RED,
        )
        fun2 = axes.get_graph(
            lambda x: x + 0.5,
            color=RED,
        )
        fun3 = axes.get_graph(
            lambda x: x - 0.5,
            color=RED,
        )
        fun = VGroup(fun2, fun3)
        self.wait()
        self.play(ShowCreation(fun1))
        self.wait()
        self.play(ReplacementTransform(fun1, fun))
        self.wait()
        dot5 = Dot(color=RED)
        dot5.move_to(axes.c2p(5, 5.5))
        dot6 = Dot(color=RED)
        dot6.move_to(axes.c2p(5.5, 6))
        dot7 = Dot(color=RED)
        dot7.move_to(axes.c2p(5.5, 5))
        dot8 = Dot(color=RED)
        dot8.move_to(axes.c2p(6, 5.5))
        self.play(FadeIn(dot5, scale=0.05))
        self.play(FadeIn(dot6, scale=0.05))
        self.play(FadeIn(dot7, scale=0.05))
        self.play(FadeIn(dot8, scale=0.05))


class example0(Scene):
    def construct(self):
        axis = NumberLine(
            x_min=3, x_max=7,
            include_ticks=True,
            include_tip=True,
            include_numbers=True,
            unit_size=2,
            color=BLACK
        )
        axis.add_numbers(
            font_size=45,
            color=BLACK,
        )
        self.play(Write(axis, lag_ratio=0.01, run_time=2))
        self.wait()

class example3(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-1, 5),
            y_range=(-1, 5),
            height=6,
            width=6,
            axis_config={
                "stroke_color": BLACK,
                "stroke_width": 4,
            },
            y_axis_config={
                "include_tip": True,
            }
        )
        axes.add_coordinate_labels(
            x_values=[1, 2, 3],
            y_values=[1, 2, 3],
            color=BLACK
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=2))
        dot1 = Dot(color=RED)
        dot1.move_to(axes.c2p(0, 1))
        dot2 = Dot(color=RED)
        dot2.move_to(axes.c2p(1, 1))
        dot3 = Dot(color=RED)
        dot3.move_to(axes.c2p(1, 3))
        dot4 = Dot(color=RED)
        dot4.move_to(axes.c2p(0, 3))
        # self.play(dot.animate.move_to(axes.c2p(3, 2)))
        h1_line = always_redraw(lambda: axes.get_h_line(dot1.get_left()))
        # h1_line.set_stroke(BLUE_E, width=4)
        v1_line = always_redraw(lambda: axes.get_v_line(dot1.get_bottom()))
        h2_line = always_redraw(lambda: axes.get_h_line(dot2.get_left()))
        v2_line = always_redraw(lambda: axes.get_v_line(dot2.get_bottom()))
        h3_line = always_redraw(lambda: axes.get_h_line(dot3.get_left()))
        v3_line = always_redraw(lambda: axes.get_v_line(dot3.get_bottom()))
        h4_line = always_redraw(lambda: axes.get_h_line(dot4.get_left()))
        v4_line = always_redraw(lambda: axes.get_v_line(dot4.get_bottom()))
        self.play(FadeIn(dot1, scale=0.05))
        self.play(FadeIn(dot2, scale=0.05))
        self.play(FadeIn(dot3, scale=0.05))
        self.play(FadeIn(dot4, scale=0.05))
        hv_line = VGroup(h1_line, v1_line, h2_line, v2_line, h3_line, v3_line, h4_line, v4_line)
        hv_line.set_stroke(BLUE_E, width=4)
        self.play(Write(hv_line, lag_ratio=0.01, run_time=4))
        fun = axes.get_graph(
            lambda x: -1 * x + 7 / 4,
            color=RED,
        )
        self.play(ShowCreation(fun))
        self.wait()
        A = Dot(color=RED)
        B = Dot(color=RED)
        A.move_to(axes.c2p(0, 7/4))
        B.move_to(axes.c2p(1, 0.75))
        self.play(FadeIn(A, scale=0.05))
        self.play(FadeIn(B, scale=0.05))
        self.wait(3)


class text1(Scene):
    def construct(self):
        text = Text("小明与小红不相干", font="黑体", font_size=70, color=BLACK)
        difference = Text(
            """
            即小明与小红所到达的时间不受相互影响\n
            尝试使用二维坐标系解决问题
            """,
            font="黑体", font_size=24,
            color=BLACK,
            # t2c是一个由 文本-颜色 键值对组成的字典
            t2c={"小明": BLUE, "小红": BLUE, "不受": ORANGE, "二维": ORANGE}
        )
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeIn(difference, UP))
        self.wait(3)

class text2(Scene):
    def construct(self):
        t1 = Text(
            """
            设小明会到达的时间为x,小红会到达的时间为y \n
            则x属于[4,5]，y属于[5,6] \n
            由题意得,|x-y|<=0.5,又因为x<y \n
            所以,y-x<=0.5
            """,
            font = "黑体", font_size = 40,
            color = BLACK,
            t2c={"小明": BLUE, "小红": BLUE, "[4,5]": ORANGE, "[5,6]": ORANGE}
        )
        #self.wait(2)
        self.play(Write(t1, lag_ratio=0.01, run_time=5))
        self.wait(3)

class answer1(Scene):
    def construct(self):
        t1 = Text(
            """
            实验的全部结果构成的区域为:S黄 = 1 × 1= 1\n
            事件A构成的区域为:S蓝 = 0.5 × 0.5 × 0.5 = 0.125 \n
            P(A) = S蓝 / S黄 = 0.125 \n
            所以,小明与小红相遇的概率为八分之一
            """,
            font="黑体", font_size=40,
            color=BLACK,
            t2c={"S黄": ORANGE, "S蓝": BLUE}
        )
        self.play(FadeIn(t1, lag_ratio=0.01, run_time=10))
        self.wait(3)


class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # 将多个参数传递给Tex，这些参数看起来被连接在一起作为一个表达式
            # 但整个mobject的每个submobject为其中的一个字符串
            # 例如，下面的Tex物件将有5个子物件，对应于表达式[A^2，+，B^2，=，C^2]
            Tex("A^2", "+", "B^2", "=", "C^2"),
            # 这里同理
            Tex("A^2", "=", "C^2", "-", "B^2"),
            # 或者，你可以传入关键字参数isolate，其中包含一个字符串列表
            # 这些字符串应该作为它们自己的子物件存在
            # 因此，下面的一行相当于它下面注释掉的一行
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # TransformMatchingTex将源和目标中具有匹配tex字符串的部分对应变换
        # 传入path_arc，使每个部分旋转到它们的最终位置，这种效果对于重新排列一个方程是很好的
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # …这看起来很好，但由于在lines[2]中没有匹配"C^2"或"B^2"的tex，这些子物件会淡出
        # 而C和B两个子物件会淡入，如果我们希望C^2转到C，而B^2转到B，我们可以用key_map来指定
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # 也许我们想把^2上的指数转换成根号。目前，lines[2]将表达式A^2视为一个单元
        # 因此我们可能会需要创建同一line的新版本，该line仅分隔出A
        # 这样，当TransformMatchingTex将所有匹配的部分对应时，唯一的不匹配将是来自new_line2的"^2"
        # 和来自最终行的"\sqrt"之间的不匹配。通过传入transform_missmatches=True，它会将此"^2"转换为"\sqrt"
        new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # 或者，如果您不想故意分解tex字符串，您可以使用TransformMatchingShapes
        # 它将尝试将源mobject的所有部分与目标的部分对齐，而不考虑每个部分中的子对象层次结构
        # 根据这些部分是否具有相同的形状（尽其所能）来自动匹配变换
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()


class lasta(Scene):
    def construct(self):
        t1 = Text(
            """
            在区间(0,1)与(1,3)中各随机取一个数， \n
            则两数之和大于四分之七的概率为多少？
            """,
            font="黑体", font_size=30,
            color=BLACK,
            t2c={"各随机": ORANGE, "四分之七": BLUE}
        ).shift(LEFT)
        ans = Text(
            """
            设事件A为 “取出的两数之和大于四分之七” \n
            S总 = 1 × 3 = 3 \n
            S三角形 = 0.75 × 0.75 × 0.5 = 0.28125\n
            S(A) = S总 - S三角形 \n
                    = 3 - 0.28125 = 2.71875\n
            所以两人相遇概率: \n
                    P(A) = S(A) / S总 = 0.90625 \n
            所以，两人第二次相遇的概率为三十二分之二十九
            """,
            font="黑体", font_size=30,
            color=BLACK,
            t2c={"S三角形": BLUE, "S总": ORANGE}
        ).shift(LEFT)
       # VGroup(t1, t2).arrange(DOWN, buff=1)
        self.play(Write(ans, lag_ratio=0.01, run_time=7))
        self.wait(3)

class Kiriyan(Scene):
    def construct(self):
        text = Text("Kiriyan", font="黑体", font_size=70, color=BLUE)
        self.play(Write(text, lag_ratio=0.01, run_time=5))
        self.wait(2)