from manimlib import *
import numpy as np
from math import *

class AB(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-7, 7),
            y_range=(-4, 4),
            height=8,
            width=14,
            stroke=1,
        )
        axes.add_coordinate_labels()
        x1, y1, x2, y2 = 0, 0, 5, 0
        v1, v2 = 0.1, 0.1
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        self.play(ShowCreation(axes))
        A = Dot(color=PURPLE_A)
        B = Dot(color=BLUE)
        A.move_to(np.array([x1, y1, 0]))
        B.move_to(np.array([x2, y2, 0]))
        self.add(A, B)
        now = self.time
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, 0]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, 0]))
        )

        while r > 0.01:
            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            x2 -= 0.01 * (x2 - x1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            y2 += 0.01 * (y1 - y2) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            y1 += 0.005
            print(x1, y1, x2, y2)
            r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            self.wait(0.01)
            #r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5



class opening_Title_Sequence(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-7, 7),
            y_range=(-4, 4),
            height=8,
            width=14,
            stroke=1,
        )
        axes.add_coordinate_labels(
            x_values=[-8, 8],
            y_values=[5, -5],
            color=GREY_C,
        )
        self.play(Write(axes))
        tan = axes.get_graph(
            lambda x: math.tan(x),
            x_range=(-8, 8),
            discontinuities=[-1.5*PI-0.1, -1.5*PI+0.1, -0.5*PI, 1.5*PI, 0.5*PI],
            color=BLUE,
        )

        x = -1.5 * PI
        while x <= 1.5*PI:
            linei = DashedLine(np.array([0, 7, 0]), np.array([0, -7, 0]))
            linei.set_stroke(color=PURPLE_A, width=0.5)
            linei.move_to(RIGHT*x)
            self.play(FadeIn(linei))
            x += PI

        #line = DashedLine(np.array([0, -4 ,0]), np.array([0, 4, 0]))
        #line.move_to(LEFT*PI)
        self.play(Write(tan, lag_ratio=0.01, run_time=4))
        tan1 = axes.get_graph(
            lambda x: math.tan(x),
            x_range=(-8, 8),
            discontinuities=[-1.5 * PI - 0.1, -1.5 * PI + 0.1, -0.5 * PI, 1.5 * PI, 0.5 * PI],
            color=BLUE_C,
        )
        tan1.set_stroke(opacity=1.0, width=1)
        #self.play(ReplacementTransform(tan, tan1))

        text = Text(
            "K",
            color=BLUE_D,
            font_size=400,
            blackground_stroke_color=PURPLE_A,
        )
        text1 = Text(
            "iriyan",
            color=BLUE_E,
            font_size=100,
            blackground_stroke_color=PURPLE_A,
        )
        text.move_to(LEFT*2)
        text1.move_to(RIGHT*1.4+DOWN)
        #self.play(ReplacementTransform(tan, tan1, run_time=4), Write(text, lag_ratio=0.01, run_time=5))
        self.play(
            ReplacementTransform(tan.copy(), text, run_time=3),
            ReplacementTransform(tan, tan1, run_time=4)
        )
        self.play(FadeInFromPoint(text1, LEFT*2+DOWN, run_time=2))


class S1(ThreeDScene):
    def construct(self):
        axes = Axes(
            x_range=(-7, 7),
            y_range=(-4, 4),
            height=8,
            width=14,
            stroke=1,
        )
        road_1 = Line(np.array([-6, -1, 0]), np.array([6, -1, 0]), stroke_width=5, stroke_color=BLUE_D)
        road_2 = Line(np.array([-6, 1, 0]), np.array([6, 1, 0]), stroke_width=5, stroke_color=BLUE_D)
        road = VGroup(road_1, road_2)
        B = Dot(
            radius=0.2,
            fill_color=PURPLE_A,
        )
        A = Dot(
            radius=0.2,
            fill_color=TEAL_C,
        )
        A_label = Text("A")
        B_label = Text("B")
        v1_label = Tex("V_{1}=1m/s", font_size=40)
        v2_label = Tex("V_{2}=2m/s", font_size=40)
        always(A_label.next_to, A, UP)
        always(B_label.next_to, B, UP)
        x2, x1 = -4, 1
        B.move_to(np.array([x2, 0, 0]))
        A.move_to(np.array([x1, 0, 0]))
        v2 = Arrow(start=np.array([x2, 0.0, 0.0]), end=np.array([x2+2, 0.0, 0.0]))
        v1 = Arrow(start=np.array([x1, 0.0, 0.0]), end=np.array([x1+1, 0.0, 0.0]))
        always(v2.next_to, B, 0.1*RIGHT)
        always(v1.next_to, A, 0.1*RIGHT)
        always(v2_label.next_to, v2, DOWN)
        always(v1_label.next_to, v1, DOWN)
        text1 = Text(
            """
            直线上有A、B两人, A以V1 = 1m/s的速度向右做匀速直线运动\n
            同时B以V2 = 2m/s的速度大小朝着A所在位置方向运动, \n
            求B追上A的时间 t
            """,
            color=WHITE, font="黑体", font_size=30,
            t2c={"A": TEAL_C, "B": PURPLE_A, "1m/s": ORANGE, "2m/s": ORANGE, "t": ORANGE}
        )
        frame = self.camera.frame
        frame.reorient(phi_degrees=90, theta_degrees=0, gamma_degrees=None)
        self.play(ShowCreation(road), run_time=3)
        #.reorient(phi_degrees=90, theta_degrees=0, gamma_degrees=None)
        # 设置相机位置其中phi是相机与原点连线与z轴正方向夹角。theta是摄像机围绕Z轴旋转的角度
        self.play(
            frame.animate.to_default_state(),
            run_time=3
        )
        #self.add(A, B, A_label, B_label)
        self.play(ShowCreation(VGroup(A, B, A_label, B_label)))
        self.wait()
        mobjects = VGroup(v1, v2)
        self.play(*[GrowFromPoint(mob, mob.get_center() + LEFT * 3) for mob in mobjects])
        self.play(Write(VGroup(v1_label, v2_label), run_time=3))
        text1.move_to(np.array([0, 3, 0]))
        self.play(ShowIncreasingSubsets(text1, run_time=16))
        self.wait(3)
        """
        now = self.time
        A.add_updater(
            lambda a: a.move_to(np.array([1+1*(self.time-now), 0, 0])),
        )
        B.add_updater(
            lambda b: b.move_to(np.array([-4+2*(self.time - now), 0, 0])),
        )
        A_cen = A.get_center()
        B_cen = B.get_center()
        while abs(A_cen[0]-B_cen[0]) > 0.1:
            self.wait(0.1)
            A_cen = A.get_center()
            B_cen = B.get_center()
        """

class S2(Scene):
    def construct(self):
        B = Dot(
            radius=0.2,
            fill_color=PURPLE_A,
        )
        A = Dot(
            radius=0.2,
            fill_color=TEAL_C,
        )
        A_label = Text("A")
        B_label = Text("B")
        v1_label = Tex("V_{1}", font_size=40)
        v2_label = Tex("V_{2}", font_size=40)
        fun1 = Tex("x_{B}-x_{A}=L", font_size=60).move_to(np.array([0, -2.3, 0]))
        always(A_label.next_to, A, UP)
        always(B_label.next_to, B, UP)
        B.move_to(np.array([-4, 0, 0]))
        A.move_to(np.array([1, 0, 0]))
        A_cen = A.get_center()
        B_cen = B.get_center()
        road = Arrow(start=np.array([-7, 0, 0]), end=np.array([7, 0, 0]))
        road.set_color(BLUE_D)
        L = Line(A.get_center(), B.get_center(), stroke_width=2, stroke_color=RED_C)
        L.add_updater(lambda m: m.put_start_and_end_on(A.get_center(), B.get_center()))
        brace = always_redraw(Brace, L, DOWN)
        text, number = label = VGroup(
            Text("L = "),
            DecimalNumber(
                0,
                show_ellipsis=False, #省略号
                num_decimal_places=2,  #小数位数
                include_sign=False,  #是否加符号
            )
        )
        label.arrange(RIGHT)
        l = L.get_width()
        #print(l)
        always(label.next_to, brace, DOWN)
        f_always(number.set_value, L.get_length)

        v2 = Arrow(start=np.array([-4, 0.0, 0.0]), end=np.array([-4 + 2, 0.0, 0.0]))
        v1 = Arrow(start=np.array([1, 0.0, 0.0]), end=np.array([1 + 1, 0.0, 0.0]))
        always(v1_label.next_to, v1, UP)
        always(v2_label.next_to, v2, UP)
        L_label = VGroup(brace, label)
        V = VGroup(v1, v2)

        #self.play(FadeIn(VGroup(A, B)))
        self.play(GrowFromPoint(road, road.get_center() + LEFT * 3, run_time=2))
        self.wait()
        self.add(A, B)
        self.play(FadeIn(VGroup(A_label, B_label)))
        self.wait(2)
        self.add(L)
        self.wait()
        self.play(*[GrowFromPoint(mob, mob.get_center() + UP) for mob in L_label], run_time=2)
        self.wait(2)
        self.play(*[GrowFromPoint(mob, mob.get_center() + LEFT * 3) for mob in V])
        self.play(FadeIn(VGroup(v1_label, v2_label)))
        self.wait(2)
        self.play(Write(fun1, run_time=2))
        self.play(FadeOut(VGroup(V, v1_label, v2_label)))
        self.wait(2)
        now = self.time
        A.add_updater(
            lambda a: a.move_to(np.array([1 + 1 * (self.time - now), 0, 0])),
        )
        B.add_updater(
            lambda b: b.move_to(np.array([-4 + 2 * (self.time - now), 0, 0])),
        )
        while abs(A_cen[0] - B_cen[0]) > 0.1:
            self.wait(0.1)
            #L = Line(A.get_center(), B.get_center(), stroke_width=2, stroke_color=RED_C)
            A_cen = A.get_center()
            B_cen = B.get_center()
        self.play(FadeOut(VGroup(A, B, A_label, B_label, L, L_label)))
        self.wait(2)
        self.play(
            FadeOut(road),
            FadeOut(fun1)
        )
        self.wait()


class S3(Scene):
    def construct(self):
        to_isolate = ["v_{1}", "v_{2}", "t", "=", "\\int", "x_{A}", "x_{B}"]
        lines = VGroup(
            Tex("x_{B} - x_{A} = ", "L", isolate=[*to_isolate]),

            Tex("\\int v_{2}dt - \\int v_{1}dt = ", "L", isolate=[*to_isolate]),

            Tex("v_{2}t - v_{1}t = ", "L", isolate=[*to_isolate]),

            Tex("t = \\frac{L}{v_{2}-v_{1}}", isolate=[*to_isolate]),

        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "x_{A}": TEAL_C,
                "x_{B}": PURPLE_A,
                "v_{1}": TEAL_C,
                "v_{2}": PURPLE_A,
                "t": ORANGE,
            })

        play_kw = {"run_time": 3}
        self.add(lines[0])
        # TransformMatchingTex将源和目标中具有匹配tex字符串的部分对应变换
        # 传入path_arc，使每个部分旋转到它们的最终位置，这种效果对于重新排列一个方程是很好的
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                key_map={
                    "x_{B}": "v_{2}dt",
                    "x_{A}": "v_{1}dt",
                }
            ),
            **play_kw
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(
                lines[2].copy(), lines[3],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait(2)

class S4(Scene):
    def construct(self):
        B = Dot(
            radius=0.2,
            fill_color=PURPLE_A,
        )
        A = Dot(
            radius=0.2,
            fill_color=TEAL_C,
        )
        B.move_to(np.array([-4, 0, 0]))
        A.move_to(np.array([1, 0, 0]))
        A_label = Text("A")
        B_label = Text("B")
        road = Arrow(start=np.array([-7, 0, 0]), end=np.array([3, 0, 0]))
        road.set_color(BLUE_D)
        road2 = Arrow(start=np.array([1, 0, 0]), end=np.array([1, 7, 0]))
        road2.set_color(BLUE_D)
        #self.play(road, A, B, A_label, B_label).animate.shift(IN * 6 + LEFT * 4 + DOWN * 2))
        road2.shift(IN * 6 + LEFT * 4 + DOWN * 2)
        always(A_label.next_to, A, 0.2*RIGHT+0.2*DOWN)
        always(B_label.next_to, B, 0.2*UP)
        v2 = Arrow(start=np.array([-4, 0.0, 0.0]), end=np.array([-4 + 2, 0.0, 0.0]))
        v1 = Arrow(start=np.array([1, 0.0, 0.0]), end=np.array([1 + 1, 0.0, 0.0]))
        v11 = Arrow(start=np.array([1, 0.0, 0.0]), end=np.array([1, 1.0, 0.0]))
        always(v2.next_to, B, RIGHT*0.1)
        always(v1.next_to, A, RIGHT*0.1)
        always(v11.next_to, A, UP*0.1)
        v1_label = Tex("V_{1}", font_size=40)
        v2_label = Tex("V_{2}", font_size=40)
        always(v1_label.next_to, v1, 0.2*UP)
        always(v2_label.next_to, v2, UP*0.2)
        t1 = Text(
            """
            Q1:\n\n
            直线上有A、B两人,\n\n 
            A以V1 = 1m/s的速度\n\n
            向右做匀速直线运动\n\n
            同时B以V2 = 2m/s的速度大小\n\n
            朝着A所在位置方向运动, \n\n
            求B追上A的时间 t
            """,
            color=WHITE, font="黑体", font_size=30,
            t2c={"A": TEAL_C, "B": PURPLE_A, "1m/s": ORANGE, "2m/s": ORANGE, "t": ORANGE}
        ).move_to(np.array([4, 0.5, 0]))
        t2 = Text(
            """
            Q1:\n\n
            直线上有A、B两人,\n\n 
            A以V1 = 1m/s的速度\n\n
            向上做匀速直线运动\n\n
            同时B以V2 = 2m/s的速度大小\n\n
            朝着A所在位置方向运动, \n\n
            求B追上A的时间 t
            """,
            color=WHITE, font="黑体", font_size=30,
            t2c={"A": TEAL_C, "B": PURPLE_A, "1m/s": ORANGE, "2m/s": ORANGE, "t": ORANGE, "向上": RED_B}
        ).move_to(np.array([4, 0.5, 0]))
        #always(v1_label.next_to, v1, UP)
        v1_label.move_to(np.array([1, 1, 0]))
        always(v2_label.next_to, v2, UP)
        self.play(
            GrowFromPoint(road, road.get_center() + LEFT*3, run_time=2),
        )
        self.wait()
        self.play(FadeIn(VGroup(A, B, A_label, B_label), run_time=3))
        self.wait()
        self.play(VGroup(road, A, B, A_label, B_label).animate.shift(IN*6+LEFT*2))
        self.wait(2)
        self.play(ShowIncreasingSubsets(t1, run_time=16, rate_func=linear))
        self.wait(2)
        self.play(Write(VGroup(v2, v2_label)))
        self.wait(2)
        source = Text("向右做匀速直线运动", color=PURPLE_A, font="黑体", font_size=40).move_to(np.array([-3, 2, 0]))
        target = Text("朝着A运动", color=TEAL_C, font="黑体", font_size=40).move_to(np.array([-3, 2, 0]))
        self.play()
        self.wait(2)
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.wait(2)
        self.play(
            Flash(B.get_center(), color=YELLOW, flash_radius=0.5),
            Write(source, run_time=3),
        )
        self.wait(2)
        self.play(
            Flash(A.get_center(), color=YELLOW, flash_radius=0.5),
            #TransformMatchingShapes(source, target, **kw)
            ReplacementTransform(source, target)
        )
        self.wait(2)
        self.play(
            Write(v1, run_time=2),
            FadeOut(target)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(v1, v11),
            TransformMatchingShapes(t1, t2, **kw)
        )
        self.wait(2)
        self.play(VGroup(road, A, B, A_label, B_label, v2, v2_label, v11).animate.shift(LEFT*2+DOWN*2))
        self.wait(2)
        self.play(GrowFromPoint(road2, road2.get_center() + DOWN*3, run_time=2))
        self.wait(2)

        """
        road1 = Arrow(start=np.array([-7, 0, 0]), end=np.array([3, 0, 0]))
        road1.set_color(BLUE_D)
        road2 = Arrow(start=np.array([1, 0, 0]), end=np.array([1, 7, 0]))
        road2.set_color(BLUE_D)
        road = VGroup(road1, road2)
        self.play(GrowFromPoint(road2, road2.get_center() + 2*DOWN, run_time=2))
        self.play(VGroup(road, A, B, A_label, B_label).animate.shift(IN*6+LEFT*4+DOWN*2))
        """

class S5(Scene):
    def construct(self):
        def pointr(M, N):
            return ((M[0] - N[0]) ** 2 + (M[1] - N[1]) ** 2 + (M[2] - N[2]) ** 2) ** 0.5

        road1 = Arrow(start=np.array([7, 0, 0]), end=np.array([-5, 0, 0]))
        road1.set_color(BLUE_D)
        road2 = Arrow(start=np.array([0, 0, 0]), end=np.array([0, 7, 0]))
        road2.set_color(BLUE_D)
        road = VGroup(road1, road2)
        B = Dot(
            radius=0.2,
            fill_color=PURPLE_A,
        )
        A = Dot(
            radius=0.2,
            fill_color=TEAL_C,
        )
        B.move_to(np.array([5, 0, 0]))
        A.move_to(np.array([0, 0, 0]))
        A_label = Text("A")
        B_label = Text("B")
        always(A_label.next_to, A, 0.2*LEFT+0.2*DOWN)
        always(B_label.next_to, B, 0.2*RIGHT)
        t2 = Text(
            """
            Q1:\n\n
            直线上有A、B两人,\n\n 
            A以V1 = 1m/s的速度\n\n
            向上做匀速直线运动\n\n
            同时B以V2 = 2m/s的速度大小\n\n
            朝着A所在位置方向运动, \n\n
            求B追上A的时间 t
            """,
            color=WHITE, font="黑体", font_size=30,
            t2c={"A": TEAL_C, "B": PURPLE_A, "1m/s": ORANGE, "2m/s": ORANGE, "t": ORANGE, "向上": RED_B}
        ).move_to(np.array([4, 0.5, 0]))

        to_isolate = ["v_{1}", "v_{2}", "t", "=", "A", "B", "L"]
        ana = VGroup(
            Text("解决方法", color=WHITE, font="黑体", font_size=50),

            Text(
                "找出A与B的位移关系",
                color=WHITE, font="黑体", font_size=40,
                t2c={"A": TEAL_C, "B": PURPLE_A}
            ),

            Tex("v_{1}t - v_{2}t = L ", isolate=[*to_isolate]),

            Text("不适用", color=RED_C, font="黑体", font_size=40),

        ).arrange(DOWN, buff=LARGE_BUFF)
        ana.shift(RIGHT*3.5)
        #ana.arrange(DOWN, buff=LARGE_BUFF) move_to(np.array([3, 2, 0]))
        ana[2].set_color_by_tex_to_color_map({
            "v_{1}": TEAL_C,
            "v_{2}": PURPLE_A,
            "t": ORANGE,
        })
        play_kw = {"run_time": 3}

        All = VGroup(road, A, B, A_label, B_label)
        self.play(FadeIn(All, run_time=2))
        self.wait(2)
        self.play(All.animate.shift(IN*6+DOWN*2+LEFT*7))
        self.wait(2)
        self.play(FadeIn(t2, run_time=2))
        self.wait(3)
        self.play(FadeOut(t2))
        self.wait()
        self.add(ana[0])
        self.wait(2)
        for i in range(3):
            self.play(ReplacementTransform(ana[i].copy(), ana[i+1], run_time=2))
            self.wait(2)
        #self.embed()

        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])
        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        #now = self.time
        #print((A.get_center()-B.get_center())*0.2/pointr(A.get_center(), B.get_center()))
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )
        vec = []
        cou = 0
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        while pointr(A.get_center(), B.get_center()) > 0.01:
            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += 0.005
            x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        self.wait(2)

        self.play(FadeOut(ana))
        """
        #记得删
        A.clear_updaters()
        B.clear_updaters()
        self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
        self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
        self.play(All.animate.shift(OUT * 10 + RIGHT * 4))
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])
        #删结束
        """

        One_Time = 100
        while One_Time > 11:
            A.clear_updaters()
            B.clear_updaters()
            self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
            self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
            if One_Time == 100:
                self.play(All.animate.shift(OUT*10+RIGHT*4))
            A0, B0 = [], []
            for i in range(0, 3):
                A0.append(A.get_center()[i])
                B0.append(B.get_center()[i])
            self.wait(2)
            x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
            x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
            A.add_updater(
                lambda a: a.move_to(np.array([x1, y1, z1]))
            )
            B.add_updater(
                lambda b: b.move_to(np.array([x2, y2, z2]))
            )
            vec1, vec2 = [], []
            cou = 0
            a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
            x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
            while pointr(A.get_center(), B.get_center()) > 0.01:
                cou += 1
                if cou % One_Time == 0:
                    v0 = Arrow(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
                    va = Arrow(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
                    a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
                    x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
                    vec2.append(v0)
                    vec1.append(va)
                    self.play(FadeIn(VGroup(vec2[-1], vec1[-1])))

                x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
                y1 += 0.005
                x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
                y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
                self.wait(0.01)
            v0 = Arrow(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
            va = Arrow(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
            a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
            x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
            vec2.append(v0)
            vec1.append(va)
            self.play(FadeIn(VGroup(vec2[-1], vec1[-1])))
            One_Time = int(One_Time/2)
            self.wait(2)
            for vec0 in vec1:
                self.remove(vec0)
            for vec0 in vec2:
                self.remove(vec0)

        A.clear_updaters()
        B.clear_updaters()

        self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
        self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])

        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )
        l1, l2 = [], []
        cou = 0
        a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        while pointr(A.get_center(), B.get_center()) > 0.01:
            cou += 1
            if cou % 2 == 0:
                l0 = Line(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
                la = Line(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
                a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
                x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
                l2.append(l0)
                l1.append(la)
                #self.play(FadeIn(VGroup(l2[-1], l1[-1])))
                self.add(l2[-1], l1[-1])

            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += 0.005
            x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        l0 = Line(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
        la = Line(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
        a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        l2.append(l0)
        l1.append(la)
        #self.play(FadeIn(VGroup(l2[-1], l1[-1])))
        self.add(l2[-1], l1[-1])
        self.wait(2)

        A.clear_updaters()
        B.clear_updaters()
        self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
        self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])
        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )

        cou = 0
        while pointr(A.get_center(), B.get_center()) > 0.01:
            cou += 1
            if cou % 2 == 0 and cou >= 200 and cou <= 500:
                if cou != 200:
                    self.remove(lin, ve, vd, dl)
                l = Line(start=B.get_center(), end=A.get_center())
                l.set_color(RED_A)
                l.scale(10)
                lin = l
                C = A.get_center() + UP * 1.5
                k = (A.get_center()[1] - B.get_center()[1]) / (A.get_center()[0] - B.get_center()[0])
                xa, ya, xc, yc = A.get_center()[0], A.get_center()[1], C[0], C[1]
                xd = (yc - ya + xc / k + k * xa) / (k + 1 / k)
                yd = k * (xd - xa) + ya
                ve = Arrow(start=A.get_center(), end=C, buff=0.0)
                ve.set_color(GREEN_C)
                vd = Arrow(start=A.get_center(), end=np.array([xd, yd, B.get_center()[2]]), buff=0.0)
                vd.set_color(YELLOW_E)
                dl = DashedLine(start=C, end=np.array([xd, yd, B.get_center()[2]]))
                # self.play(FadeIn(VGroup(l2[-1], l1[-1])))
                if cou == 200:
                    self.play(FadeIn(lin))
                    self.play(FadeIn(VGroup(ve, vd, dl)))
                else:
                    self.add(lin)
                    self.add(ve, vd, dl)
                    if cou == 400:
                        self.wait(3)
                        """
                        C = A.get_center() + UP * 1.5
                        k = (A.get_center()[1]-B.get_center()[1])/(A.get_center()[0]-B.get_center()[0])
                        xa, ya, xc, yc = A.get_center()[0], A.get_center()[1], C[0], C[1]
                        xd = (yc - ya + xc/k + k*xa) / (k + 1/k)
                        yd = k * (xd - xa) + ya
                        ve = Arrow(start=A.get_center(), end=C, buff=0.0)
                        ve.set_color(GREEN_C)
                        vd = Arrow(start=A.get_center(), end=np.array([xd, yd, B.get_center()[2]]), buff=0.0)
                        vd.set_color(YELLOW_E)
                        dl = DashedLine(start=C, end=np.array([xd, yd, B.get_center()[2]]))
                        
                        #(xd, yd)为垂足
                        self.play(FadeIn(ve))
                        self.wait(2)
                        self.play(FadeIn(dl))
                        self.wait(2)
                        self.play(FadeIn(vd))
                        self.wait(2)
                        #self.embed()
                        """
            if cou == 501:
                self.play(FadeOut(VGroup(lin, ve, vd, dl)))
            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += 0.005
            x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        self.wait(2)

class S6(Scene):
    def construct(self):

        vb = Tex("V_{2}", "=", "\\frac{dx}{dt}")
        vb.set_color_by_tex_to_color_map({
            "V_{2}": PURPLE_A,
        })
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(

            Text(
                "B --> A",
                color=WHITE, font="黑体", font_size=40,
                t2c={"A": TEAL_C, "B": PURPLE_A}
            ),

            Text("突破口？", color=WHITE, font="黑体", font_size=50),

            Text("B的运动轨迹？", color=WHITE, font="黑体", font_size=40, t2c={"B": PURPLE_A, "轨迹": ORANGE}),

            Text("是否能用关于x与y的方程描述？", color=WHITE, font="黑体", font_size=40, t2c={"x": BLUE_C, "y": GREEN_C}),

            Text("不可行 ×", color=RED_C, font="黑体", font_size=40),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)

        same = VGroup(
            Text("同类型", color=ORANGE, font="黑体", font_size=50),
            Text("相似之处——>考虑本质", color=RED_A, font="黑体", font_size=40)
        )
        same.arrange(DOWN, buff=LARGE_BUFF)

        play_kw = {"run_time": 2}
        self.add(lines[0])
        self.wait(2)
        for i in range(4):
            self.play(ReplacementTransform(lines[i].copy(), lines[i+1], **play_kw))
            self.wait(2)
        self.play(FadeOut(lines))
        self.wait(2)
        self.play(FadeIn(vb, **play_kw))
        self.wait(2)
        self.play(FadeOut(vb))
        self.wait(2)
        self.add(same[0])
        self.wait(2)
        self.play(ReplacementTransform(same[0].copy(), same[1], **play_kw))
        self.wait(2)

class S7(Scene):
    def construct(self):
        def pointr(M, N):
            return ((M[0] - N[0]) ** 2 + (M[1] - N[1]) ** 2 + (M[2] - N[2]) ** 2) ** 0.5

        road1 = Arrow(start=np.array([7, 0, 0]), end=np.array([-5, 0, 0]))
        road1.set_color(BLUE_D)
        road2 = Arrow(start=np.array([0, 0, 0]), end=np.array([0, 7, 0]))
        road2.set_color(BLUE_D)
        road = VGroup(road1, road2)
        B = Dot(
            radius=0.2,
            fill_color=PURPLE_A,
        )
        A = Dot(
            radius=0.2,
            fill_color=TEAL_C,
        )
        B.move_to(np.array([5, 0, 0]))
        A.move_to(np.array([0, 0, 0]))
        A_label = Text("A")
        B_label = Text("B")
        always(A_label.next_to, A, 0.2*LEFT+0.2*DOWN)
        always(B_label.next_to, B, 0.2*RIGHT)

        All = VGroup(road, A, B, A_label, B_label)
        self.play(FadeIn(All, run_time=2))
        self.wait(2)
        self.play(All.animate.shift(IN * 6 + DOWN * 2 + LEFT * 7))
        self.wait(2)
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])
        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        # now = self.time
        # print((A.get_center()-B.get_center())*0.2/pointr(A.get_center(), B.get_center()))
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )
        vec = []
        cou = 0
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        while pointr(A.get_center(), B.get_center()) > 0.01:
            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += 0.005
            x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        self.wait(2)

        A.clear_updaters()
        B.clear_updaters()
        self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
        self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
        self.play(All.animate.shift(OUT * 10 + RIGHT * 4))
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])

        A.clear_updaters()
        B.clear_updaters()

        self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
        self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])

        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )
        l1, l2 = [], []
        cou = 0
        a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        while pointr(A.get_center(), B.get_center()) > 0.01:
            cou += 1
            if cou % 2 == 0:
                l0 = Line(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
                la = Line(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
                a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
                x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
                l2.append(l0)
                l1.append(la)
                # self.play(FadeIn(VGroup(l2[-1], l1[-1])))
                self.add(l2[-1], l1[-1])

            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += 0.005
            x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        l0 = Line(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
        la = Line(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
        a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        l2.append(l0)
        l1.append(la)
        # self.play(FadeIn(VGroup(l2[-1], l1[-1])))
        self.add(l2[-1], l1[-1])
        self.wait(2)

        A.clear_updaters()
        B.clear_updaters()
        self.play(A.animate.move_to(np.array([A0[0], A0[1], A0[2]])))
        self.play(B.animate.move_to(np.array([B0[0], B0[1], B0[2]])))
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])
        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )

        cou = 0
        while pointr(A.get_center(), B.get_center()) > 0.01:
            cou += 1
            if cou % 2 == 0 and cou >= 100 and cou <= 500:
                for line in l1:
                    self.remove(line)
                for line in l2:
                    self.remove(line)
                if cou != 100:
                    self.remove(lin, vd)
                l = Line(start=B.get_center(), end=A.get_center())
                l.set_color(RED_A)
                l.scale(10)
                lin = l
                C = A.get_center() + UP * 1.5
                k = (A.get_center()[1] - B.get_center()[1]) / (A.get_center()[0] - B.get_center()[0])
                xa, ya, xc, yc = A.get_center()[0], A.get_center()[1], C[0], C[1]
                xd = (yc - ya + xc / k + k * xa) / (k + 1 / k)
                yd = k * (xd - xa) + ya
                ve = Arrow(start=A.get_center(), end=C, buff=0.0)
                ve.set_color(GREEN_C)
                vd = Arrow(start=A.get_center(), end=np.array([xd, yd, B.get_center()[2]]), buff=0.0)
                vd.set_color(YELLOW_E)
                dl = DashedLine(start=C, end=np.array([xd, yd, B.get_center()[2]]))
                # self.play(FadeIn(VGroup(l2[-1], l1[-1])))
                if cou == 100:
                    self.play(FadeIn(lin))
                    self.play(FadeIn(vd))
                else:
                    self.add(lin)
                    self.add(vd)
                    if cou == 400:
                        self.wait(3)

            if cou == 501:
                self.play(FadeOut(VGroup(lin, vd)))
            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += 0.005
            x2 += 0.01 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += 0.01 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        self.wait(2)

class S8(Scene):
    def construct(self):
        play_kw = {"run_time": 2}
        to_t2c = {"A": TEAL_C, "B": PURPLE_A, "方向": ORANGE, "V1": TEAL_C, "V2": PURPLE_A}
        t1 = VGroup(

            Text("A主动", color=WHITE, font="黑体", font_size=50, t2c=to_t2c),

            Text("B预测", color=WHITE, font="黑体", font_size=50, t2c=to_t2c),

            Text("B的速度方向", color=WHITE, font="黑体", font_size=50, t2c=to_t2c),

        )
        to_isolate = ["V'", "theta", "V_{1}"]
        t2 = Text(
            """
            B在其运动方向上的速度在时间上的累积\n
            减去A在B的运动方向上的(分)速度关于时间的累积\n
            等于最开始A在B的方向上A与B的直线距离
            """,
            color=WHITE, font="黑体", font_size=35,
            t2c=to_t2c
        )
        t3 = VGroup(

            Tex("V'", "=", " \\sin ", " \\theta ", " \\cdot ", "V_{1}", " \\dots ( 1 )"),

            Tex(" \\int ", "V_{2}", "dt", "-", " \\int ", "V'", "dt", "=", "L", " \\dots ( \\ast )"),

            Text("V2沿y轴正方向上的分速度Vy:", color=WHITE, font="黑体", font_size=35, t2c=to_t2c),

            Tex(" \\frac{ V_{y} }{ V_{2} } ", "=", " \\sin ", " \\theta ", " \\dots ( 2 )"),

        )
        t4 = VGroup(
            Text("而Vy又满足,A在y轴上走过的路程:", color=WHITE, font="黑体", font_size=35, t2c=to_t2c),

            Tex(" \\int ", " V_{1} ", " dt ", "=", " \\int ", " V_{y} ", " dt ", " \\dots ( 3 )"),

            Tex("V'", "=", " \\frac{ V_{y} }{ V_{2} } ", " \\cdot ", " V_{1} "),

            Text("带入(*)式得,", color=WHITE, font="黑体", font_size=35, t2c=to_t2c),

        )
        t5 = VGroup(
            #Text("而Vy又满足,A在y轴上走过的路程:", color=WHITE, font="黑体", font_size=35, t2c=to_t2c),

            Tex(
                " \\int ", " V_{2} ", " dt ", "-", " \\int ", " \\frac{ V_{y} }{ V_{2} } ",
                " \\cdot ", " V_{1} ", "dt", "=", "L"
            ),

            Tex(
                " V_{2} ", " \\cdot ", " t ", "-", " \\frac{ V_{1} }{ V_{2} } ",
                " \\cdot ", " \\int ", " V_{y} ", " dt ", "=", "L"
            ),

            Tex(" \\int ", " V_{y} ", " dt ", "=", " \\int ", " V_{1} ", " dt ", "=", "V_{1}", " \\cdot ", "t"),

            Tex("V_{2}", " \\cdot ", "t", "-", " \\frac{ V_{1} }{ V_{2} } ", " \\cdot ", " V_{1} ", "t", "=", "L"),

        )
        t6 = Tex("t", "=", " \\frac{ L }{ V_{2} - \\frac{ V_{1} ^{2} }{ V_{2} } } ")
        t1.arrange(DOWN, buff=LARGE_BUFF)
        #t2.arrange(DOWN, buff=LARGE_BUFF)
        t3.arrange(DOWN, buff=LARGE_BUFF)
        t4.arrange(DOWN, buff=LARGE_BUFF)
        t5.arrange(DOWN, buff=LARGE_BUFF)
        m, n = -1, -1
        for t3s in t3:
            m += 1
            if m == 2:
                continue
            t3s.set_color_by_tex_to_color_map({
                "V'": GOLD_A,
                "theta": BLUE_C,
                "V_{1}": TEAL_C,
                "V_{2}": PURPLE_A,
                "L": YELLOW_B
            })
        for t4s in t4:
            n += 1
            if n == 0 or n == 3:
                continue
            t4s.set_color_by_tex_to_color_map({
                "V'": GOLD_A,
                "theta": BLUE_C,
                "V_{1}": TEAL_C,
                "V_{2}": PURPLE_A,
                "L": YELLOW_B
            })
        for t5s in t5:
            t5s.set_color_by_tex_to_color_map({
                "V'": GOLD_A,
                "theta": BLUE_C,
                "V_{1}": TEAL_C,
                "V_{2}": PURPLE_A,
                "L": YELLOW_B
            })
        t6.set_color_by_tex_to_color_map({
            "V'": GOLD_A,
            "theta": BLUE_C,
            "V_{1}": TEAL_C,
            "V_{2}": PURPLE_A,
            "L": YELLOW_B
        })
        """
        self.play(Write(t2, run_time=10))
        self.wait(2)
        
        self.play(FadeIn(t1[0], **play_kw))
        self.wait(2)
        self.play(ReplacementTransform(t1[0].copy(), t1[1], **play_kw))
        self.wait(2)
        self.play(ReplacementTransform(t1[1].copy(), t1[2], **play_kw))
        self.wait(2)
        self.play(FadeOut(t1, **play_kw))
        self.wait(2)
        self.play(FadeIn(t2[0], **play_kw))
        self.wait(2)
        """
        self.play(FadeIn(t3[0], **play_kw))
        self.wait(2)
        for i in range(3):
            self.play(ReplacementTransform(t3[i].copy(), t3[i+1], **play_kw))
            self.wait(2)
        self.play(FadeOut(t3))
        self.wait(2)
        self.play(FadeIn(t4[0], **play_kw))
        for i in range(3):
            self.play(ReplacementTransform(t4[i].copy(), t4[i + 1], **play_kw))
            self.wait(2)
        self.play(FadeOut(t4))
        self.wait(2)
        self.play(FadeIn(t5[0], **play_kw))
        for i in range(3):
            self.play(ReplacementTransform(t5[i].copy(), t5[i + 1], **play_kw))
            self.wait(2)
        self.play(FadeOut(t5))
        self.wait(2)
        self.play(FadeIn(t6, **play_kw))
        self.wait(2)


class test_graph(Scene):
    def construct(self):
        def pointr(M, N):
            return ((M[0] - N[0]) ** 2 + (M[1] - N[1]) ** 2 + (M[2] - N[2]) ** 2) ** 0.5
        axes = Axes(
            [-7, 7], [-4, 4],
            height=8,
            width=14
        )
        self.add(axes)
        B = Dot(
            radius=0.2,
            fill_color=PURPLE_A,
        )
        A = Dot(
            radius=0.2,
            fill_color=TEAL_C,
        )

        # 改变参数
        L = 4
        dv1, dv2 = 0.005, 0.015

        B.move_to(np.array([L, 0, 0]))
        A.move_to(np.array([0, 0, 0]))
        A_label = Text("A")
        B_label = Text("B")
        always(A_label.next_to, A, 0.2 * LEFT + 0.2 * DOWN)
        always(B_label.next_to, B, 0.2 * RIGHT)
        A0, B0 = [], []
        for i in range(0, 3):
            A0.append(A.get_center()[i])
            B0.append(B.get_center()[i])
        self.wait(2)
        x1, y1, z1 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x2, y2, z2 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        A.add_updater(
            lambda a: a.move_to(np.array([x1, y1, z1]))
        )
        B.add_updater(
            lambda b: b.move_to(np.array([x2, y2, z2]))
        )
        self.add(A, B, A_label, B_label)
        l1, l2 = [], []
        cou = 0
        a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        while pointr(A.get_center(), B.get_center()) > 0.01:
            cou += 1
            if cou % 2 == 0:
                l0 = Line(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
                la = Line(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
                a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
                x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
                l2.append(l0)
                l1.append(la)
                # self.play(FadeIn(VGroup(l2[-1], l1[-1])))
                self.add(l2[-1], l1[-1])

            x1, y1, x2, y2 = A.get_center()[0], A.get_center()[1], B.get_center()[0], B.get_center()[1]
            y1 += dv1
            x2 += dv2 * (x1 - x2) / pointr(A.get_center(), B.get_center())
            y2 += dv2 * (y1 - y2) / pointr(A.get_center(), B.get_center())
            self.wait(0.01)
        l0 = Line(start=np.array([a0, a1, a2]), end=A.get_center(), buff=0.0)
        la = Line(start=np.array([x0, y0, z0]), end=B.get_center(), buff=0.0)
        a0, a1, a2 = A.get_center()[0], A.get_center()[1], A.get_center()[2]
        x0, y0, z0 = B.get_center()[0], B.get_center()[1], B.get_center()[2]
        l2.append(l0)
        l1.append(la)
        self.add(l2[-1], l1[-1])
        self.wait(2)

        q = dv1/dv2  # q = v1/v2
        l = L
        c1 = -1 * l / (2 * (1 - q))
        c2 = l / (2 * (1 + q))
        c3 = q * l / (1 - q ** 2)
        fun = axes.get_graph(
            lambda x: c1 * (x / l) ** (1 - q) + c2 * (x / l) ** (1 + q) + c3,
            x_range=[0.01, l-0.01],
            color=BLUE
        )
        self.play(FadeIn(fun))
        """
        结论：当v1=1m/s, v2=2m/s, l=5时，两图线重合
            当v1=1m/s, v2=3m/s, l=5时，两图线重合
            当v1=1m/s, v2=3m/s, l=4时，两图线重合
            综上所述，基本确定所求方程为B的运动轨迹方程
        """


class UpdatersExample(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, 1)

        brace = always_redraw(Brace, square, UP)

        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=True,
            )
        )
        label.arrange(RIGHT)

        always(label.next_to, brace, UP)
        f_always(number.set_value, square.get_width)

        self.add(square, brace, label)

        self.play(
            square.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.wait()
        self.play(
            square.animate.set_width(2),
            run_time=3
        )
        self.wait()
        #square.set_width(1)
        now = self.time
        w0 = square.get_width()
        square.add_updater(
            lambda m: m.set_width(w0 * math.sin(self.time - now)+2.1),
            #注意不能是负数
        )
        self.wait(4 * PI)


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
