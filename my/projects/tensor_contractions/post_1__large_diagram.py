import string

from post_1__long_matrix_multiplication_chain import MatrixMultiplicationChain_2
from utils import (
    create_body,
    create_body_with_name_inside,
    create_connecting_line,
    create_diagonal_leg,
    create_down_leg,
    create_left_leg,
    create_right_leg,
    create_up_leg,
)

from manim import *


class LargeDiagram(Scene):
    def construct(self):
        # Text: Let's look at a diagram with 4 tensors
        #       A, B, C, and D
        bodies = self.create_bodies()
        for body in bodies:
            self.play(Create(body), run_time=0.35)

        self.wait(1)

        # Text: And we can let
        #       A be a rank-3 tensor
        #       B be a rank-1 tensor (vector)
        #       C be a rank-2 tensor (matrix)
        #       D also be a rank-2 tensor (matrix)
        legs = self.grow_legs()
        for name in self._get_names():
            self.play(*[Create(leg) for leg in legs[name]], run_time=0.5)
            self.wait(0.2)

        self.wait(1)

        # Text: And we can name the legs:
        leg_names = self.create_leg_names()
        for leg_name in leg_names:
            self.play(Create(leg_name), run_time=0.3)

        self.wait(1)

        # Text: And then,
        #       contract them
        contraction_lines = self.contract_legs()
        for line in contraction_lines:
            self.play(Create(line), run_time=0.3)

        self.wait(1)

        # Text: Which is a diagramatic way to write the following equation:
        equation = self.get_equation()
        self.play(Create(equation), run_time=1.25)

        self.wait(1)

        # Text: what? how?
        #       leg's give it colors!
        self.set_colors()

        self.wait(1.5)

    def _get_directions(self):
        return [
            LEFT + UP,
            RIGHT + UP,
            LEFT + DOWN,
            RIGHT + DOWN,
        ]

    def _get_names(self):
        return ["A", "B", "C", "D"]

    def _get_leg_names(self):
        return [i.lower() for i in get_greek_letter_names()[:4]]

    def create_bodies(self):
        self.bodies = [
            create_body_with_name_inside("$%s$" % name).shift(direction)
            for name, direction in zip(self._get_names(), self._get_directions())
        ]
        return self.bodies

    def create_names(self):
        self.names = [
            Tex("$%s$" % name).shift(direction * 1.8)
            for name, direction in zip(self._get_names(), self._get_directions())
        ]
        return self.names

    def grow_legs(self):
        self.legs = {}

        self.legs["A"] = [
            create_right_leg(self.bodies[0]),
            create_down_leg(self.bodies[0]),
            create_diagonal_leg(self.bodies[0], DOWN + RIGHT),
        ]
        self.legs["B"] = [
            create_left_leg(self.bodies[1]),
        ]
        self.legs["C"] = [
            create_up_leg(self.bodies[2]),
            create_right_leg(self.bodies[2]),
        ]
        self.legs["D"] = [
            create_left_leg(self.bodies[3]),
            create_diagonal_leg(self.bodies[3], UP + LEFT),
        ]

        return self.legs

    def create_leg_names(self):
        A, B, C, D = self.bodies

        self.leg_A_B = Tex("$\\alpha$")
        A_B_center = (A.get_center() + B.get_center()) / 2
        self.leg_A_B.move_to(A_B_center + 0.5 * UP)

        self.leg_A_C = Tex("$\\beta$")
        A_C_center = (A.get_center() + C.get_center()) / 2
        self.leg_A_C.move_to(A_C_center + 0.5 * LEFT)

        self.leg_A_D = Tex("$\\gamma$")
        A_D_center = (A.get_center() + D.get_center()) / 2
        self.leg_A_D.move_to(A_D_center + 0.5 * (RIGHT + UP) / np.sqrt(2))

        self.leg_C_D = Tex("$\\delta$")
        C_D_center = (C.get_center() + D.get_center()) / 2
        self.leg_C_D.move_to(C_D_center + 0.5 * DOWN)

        self.leg_names = [
            self.leg_A_B,
            self.leg_A_C,
            self.leg_A_D,
            self.leg_C_D,
        ]
        return self.leg_names

    def contract_legs(self):
        A, B, C, D = self.bodies

        line_A_B = create_connecting_line(RIGHT, self.legs["A"][0], self.legs["B"][0])
        line_A_C = create_connecting_line(DOWN, self.legs["A"][1], self.legs["C"][0])
        line_A_D = create_connecting_line(
            RIGHT + DOWN, self.legs["A"][2], self.legs["D"][1]
        )
        line_C_D = create_connecting_line(RIGHT, self.legs["C"][1], self.legs["D"][0])

        self.contraction_lines = [
            line_A_B,
            line_A_C,
            line_C_D,
            line_A_D,
        ]
        return self.contraction_lines

    def get_equation(self):
        self.equation_strings = [
            "$ \\sum_\\alpha $ ",
            "$ \\sum_\\beta $ ",
            "$ \\sum_\\gamma $ ",
            "$ \\sum_\\delta $ ",
            "$ A $ ",
            "$ _\\alpha $ ",
            "$ _\\beta $ ",
            "$ _\\gamma $ ",
            "$ B $ ",
            "$ _\\alpha $ ",
            "$ C $ ",
            "$ _\\beta $ ",
            "$ _\\delta $ ",
            "$ D $ ",
            "$ _\\delta $ ",
            "$ _\\gamma $ ",
        ]
        self.equation = Tex(*self.equation_strings)

        self.equation.shift(2.5 * DOWN)
        return self.equation

    def set_colors(self):
        self.old_objs = old_objs = {
            "A-B": (
                self.contraction_lines[0],
                self.legs["A"][0],
                self.legs["B"][0],
                self.leg_A_B,
                self.equation.submobjects[0],
                self.equation.submobjects[5],
                self.equation.submobjects[9],
            ),
            "A-C": (
                self.contraction_lines[1],
                self.legs["A"][1],
                self.legs["C"][0],
                self.leg_A_C,
                self.equation.submobjects[1],
                self.equation.submobjects[6],
                self.equation.submobjects[11],
            ),
            "A-D": (
                self.contraction_lines[3],
                self.legs["A"][2],
                self.legs["D"][1],
                self.leg_A_D,
                self.equation.submobjects[2],
                self.equation.submobjects[7],
                self.equation.submobjects[15],
            ),
            "C-D": (
                self.contraction_lines[2],
                self.legs["C"][1],
                self.legs["D"][0],
                self.leg_C_D,
                self.equation.submobjects[3],
                self.equation.submobjects[12],
                self.equation.submobjects[14],
            ),
        }
        colors = {
            "A-B": RED,
            "A-C": BLUE,
            "A-D": GREEN,
            "C-D": PURPLE,
        }
        self.new_objs = new_objs = {}

        for key in old_objs:
            new_objs[key] = []

            for old_obj in old_objs[key]:
                new_obj = old_obj.copy()
                new_obj.set_color(colors[key])
                new_objs[key].append(new_obj)

            self.play(
                *(
                    Transform(old_obj, new_obj)
                    for old_obj, new_obj in zip(old_objs[key], new_objs[key])
                ),
                run_time=0.6,
            )


class LargeDiagramContracted(LargeDiagram):
    def construct(self):
        self.add_previous_parts()
        self._fix_bodies()
        self._fix_legs()

        self.wait(1)

        self.contract_A_B()

        self.wait(1)

        self.contract_C_D()

        self.wait(1)

        self.contract_all()

        self.wait(1)

    def add_previous_parts(self):
        bodies = self.create_bodies()
        legs = self.grow_legs()
        leg_names = self.create_leg_names()
        contraction_lines = self.contract_legs()
        equation = self.get_equation()

        self.color_previous_parts()

        self.add(
            *bodies,
            *legs["A"],
            *legs["B"],
            *legs["C"],
            *legs["D"],
            *leg_names,
            *contraction_lines,
            equation,
        )

    def color_previous_parts(self):
        objs = {
            "A-B": (
                self.contraction_lines[0],
                self.legs["A"][0],
                self.legs["B"][0],
                self.leg_A_B,
                self.equation.submobjects[0],
                self.equation.submobjects[5],
                self.equation.submobjects[9],
            ),
            "A-C": (
                self.contraction_lines[1],
                self.legs["A"][1],
                self.legs["C"][0],
                self.leg_A_C,
                self.equation.submobjects[1],
                self.equation.submobjects[6],
                self.equation.submobjects[11],
            ),
            "A-D": (
                self.contraction_lines[3],
                self.legs["A"][2],
                self.legs["D"][1],
                self.leg_A_D,
                self.equation.submobjects[2],
                self.equation.submobjects[7],
                self.equation.submobjects[15],
            ),
            "C-D": (
                self.contraction_lines[2],
                self.legs["C"][1],
                self.legs["D"][0],
                self.leg_C_D,
                self.equation.submobjects[3],
                self.equation.submobjects[12],
                self.equation.submobjects[14],
            ),
        }
        colors = {
            "A-B": RED,
            "A-C": BLUE,
            "A-D": GREEN,
            "C-D": PURPLE,
        }

        for key in objs:
            for old_obj in objs[key]:
                old_obj.set_color(colors[key])

    def _fix_bodies(self):
        self.A, self.B, self.C, self.D = self.bodies

        self.A_body, self.A_name = self.A.submobjects
        self.B_body, self.B_name = self.B.submobjects
        self.C_body, self.C_name = self.C.submobjects
        self.D_body, self.D_name = self.D.submobjects

        self.remove(self.A, self.B, self.C, self.D)
        self.add(
            self.A_body,
            self.A_name,
            self.B_body,
            self.B_name,
            self.C_body,
            self.C_name,
            self.D_body,
            self.D_name,
        )

    def _fix_legs(self):
        gamma_lines = (
            self.contraction_lines[3],
            self.legs["A"][2],
            self.legs["D"][1],
        )
        self.gamma_leg = Line(
            start=self.A_body.get_corner(RIGHT + DOWN),
            end=self.D_body.get_corner(LEFT + UP),
        )
        self.gamma_leg.set_color(gamma_lines[0].get_color())

        beta_lines = (
            self.contraction_lines[1],
            self.legs["A"][1],
            self.legs["C"][0],
        )
        self.beta_leg = Line(
            start=self.A_body.get_bottom(),
            end=self.C_body.get_top(),
        )
        self.beta_leg.set_color(beta_lines[0].get_color())

        self.remove(*beta_lines, *gamma_lines)
        self.add(self.beta_leg, self.gamma_leg)

    def contract_A_B(self):
        new_AB_body = Rectangle(
            height=self.A_body.side_length,
            width=self.A_body.side_length * 1.5,
            fill_opacity=1.0,
        )
        new_AB_body.set_color(self.A_body.get_color())
        new_AB_body.align_to(self.A_body, LEFT + UP)

        self.AB_body = VMobject()
        self.AB_body.add(self.A_body, self.B_body)

        new_B_name = self.B_name.copy()
        new_B_name.next_to(self.A_name, RIGHT, buff=0)

        new_gamma_leg = Line(
            start=new_AB_body.get_corner(RIGHT + DOWN),
            end=self.D_body.get_corner(LEFT + UP),
        )
        new_gamma_leg.set_color(self.gamma_leg.get_color())

        for obj in (new_AB_body, self.A_body, self.B_body):
            obj.set_z_index(1)
        for obj in (self.A_name, self.B_name, new_B_name):
            obj.set_z_index(2)

        new_AB_tex = Tex("$ (AB) $")
        new_AB_tex.align_to(self.equation.submobjects[4], LEFT + DOWN)
        self.AB_tex = VMobject()
        self.AB_tex.add(
            self.equation.submobjects[4],  # A
            self.equation.submobjects[8],  # B
        )

        A_B_connections = [
            self.legs["A"][0],
            *self.legs["B"],
            self.leg_A_B,
            self.contraction_lines[0],
            self.equation.submobjects[0],  # sum alpha
            self.equation.submobjects[5],  # _alpha of A
            self.equation.submobjects[9],  # _alpha of B
        ]

        self.play(
            Transform(self.AB_body, new_AB_body),
            Transform(self.A_name, self.A_name),
            Transform(self.B_name, new_B_name),
            Transform(self.gamma_leg, new_gamma_leg),
            Transform(self.AB_tex, new_AB_tex),
            *(FadeOut(i) for i in A_B_connections),
            run_time=2,
        )

        self.new_AB_tex = new_AB_tex

        # self.B_name = new_B_name
        # self.gamma_leg = new_gamma_leg

    def contract_C_D(self):
        new_CD_body = Rectangle(
            height=self.C_body.side_length,
            width=self.C_body.side_length * 1.5,
            fill_opacity=1.0,
        )
        new_CD_body.set_color(self.C_body.get_color())
        new_CD_body.align_to(self.C_body, LEFT + UP)

        self.CD_body = VMobject()
        self.CD_body.add(self.C_body, self.D_body)

        new_D_name = self.D_name.copy()
        new_D_name.next_to(self.C_name, RIGHT, buff=0)

        new_gamma_leg = Line(
            start=self.AB_body.get_corner(RIGHT + DOWN),
            end=new_CD_body.get_corner(RIGHT + UP),
        )
        new_gamma_leg.set_color(self.gamma_leg.get_color())

        for obj in (new_CD_body, self.C_body, self.D_body):
            obj.set_z_index(1)
        for obj in (self.C_name, self.D_name, new_D_name):
            obj.set_z_index(2)

        new_CD_tex = Tex("$ (CD) $")
        new_CD_tex.align_to(self.equation.submobjects[10], RIGHT + DOWN)
        self.CD_tex = VMobject()
        self.CD_tex.add(
            self.equation.submobjects[10],  # C
            self.equation.submobjects[13],  # D
        )
        sub_gamma_tex = self.equation.submobjects[15]  # _gamma of D
        new_sub_gamma_tex = sub_gamma_tex.copy()  # _gamma of D
        new_sub_gamma_tex.move_to(self.equation.submobjects[12])  # _delta of C

        C_D_connections = [
            self.legs["C"][1],
            self.legs["D"][0],
            self.leg_C_D,
            self.contraction_lines[2],
            self.equation.submobjects[3],  # sum delta
            self.equation.submobjects[12],  # _delta of C
            self.equation.submobjects[14],  # _delta of D
        ]

        new_leg_A_D = self.leg_A_D.copy()
        new_leg_A_D.move_to(new_gamma_leg)
        new_leg_A_D.shift(0.5 * RIGHT)

        self.play(
            Transform(self.CD_body, new_CD_body),  # join the bodies
            Transform(self.C_name, self.C_name),  # update the name z-position
            Transform(self.D_name, new_D_name),  # move `D` near `C`
            Transform(self.gamma_leg, new_gamma_leg),  # move the name of the gamma leg
            Transform(self.leg_A_D, new_leg_A_D),  # move the gamma leg
            Transform(self.CD_tex, new_CD_tex),  # change the equation to have `(CD)`
            Transform(sub_gamma_tex, new_sub_gamma_tex),  # move the lone index
            *(FadeOut(i) for i in C_D_connections),
            run_time=2,
        )

        self.new_CD_tex = new_CD_tex
        self.new_sub_gamma_tex = new_sub_gamma_tex
        # self.D_name = new_D_name
        # self.gamma_leg = new_gamma_leg

    def contract_all(self):
        new_body = Rectangle(
            height=np.linalg.norm(self.AB_body.get_top() - self.CD_body.get_bottom()),
            width=self.CD_body.width,
            fill_opacity=1.0,
        )
        new_body.set_color(self.AB_body.get_color())
        new_body.align_to(self.AB_body, LEFT + UP)

        self.all_bodies = VMobject()
        self.all_bodies.add(self.AB_body, self.CD_body)

        what_to_remove = (
            self.gamma_leg,
            self.beta_leg,
            self.A_name,
            self.B_name,
            self.C_name,
            self.D_name,
            self.leg_A_C,
            self.leg_A_D,
        )

        new_equation = Text("Result")
        new_equation.move_to(self.equation)

        self.equation.submobjects.pop(14)  # _delta of D
        self.equation.submobjects.pop(13)  # D
        self.equation.submobjects.pop(12)  # _delta of C
        # self.equation.submobjects.pop(10) # C
        self.equation.submobjects.pop(9)  # _alpha of B
        self.equation.submobjects.pop(8)  # B
        self.equation.submobjects.pop(5)  # _alpha of A
        # self.equation.submobjects.pop(4) # A
        self.equation.submobjects.pop(3)  # sum delta
        self.equation.submobjects.pop(0)  # sum alpha

        self.play(
            Transform(self.all_bodies, new_body),
            Transform(self.equation, new_equation),
            *(FadeOut(i) for i in what_to_remove),
            run_time=2,
        )

        new_small_body = create_body()
        new_small_body.move_to(new_body)

        self.play(Transform(self.all_bodies, new_small_body), run_time=1)
