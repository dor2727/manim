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
        # self.equation_string = "$ \\sum_\\alpha \\sum_\\beta \\sum_\\gamma \\sum_\\delta A_{\\alpha \\beta \\gamma} B_\\alpha C_{\\beta \\delta} D_{\\delta \\gamma} $"
        # self.equation = Tex(self.equation_string)

        # self.equation_strings = [
        #     "$ ",
        #     "\\sum_\\alpha ",
        #     "\\sum_\\beta ",
        #     "\\sum_\\gamma ",
        #     "\\sum_\\delta ",
        #     "A_{ ",
        #     "\\alpha ",
        #     "\\beta ",
        #     "\\gamma ",
        #     "} ",
        #     "B_{ ",
        #     "\\alpha ",
        #     "} ",
        #     "C_{ ",
        #     "\\beta ",
        #     "\\delta ",
        #     "} ",
        #     "D_{ ",
        #     "\\delta ",
        #     "\\gamma ",
        #     "} ",
        #     "$ ",
        # ]
        # self.equation = Tex(*self.equation_strings)

        self.equation_strings = [
            "",
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

        # self.equation_string = "$ \\sum_\\alpha \\sum_\\beta \\sum_\\gamma \\sum_\\delta A_{\\alpha \\beta \\gamma} B_\\alpha C_{\\beta \\delta} D_{\\delta \\gamma} $"
        # self.equation = Tex(self.equation_string, tex_to_color_map={
        #     "\\sum_\\alpha": RED,
        #     "\\alpha": RED,
        #     "\\sum_\\beta": BLUE,
        #     "\\beta": BLUE,
        #     "\\sum_\\gamma": GREEN,
        #     "\\gamma": GREEN,
        #     "\\sum_\\delta": PURPLE,
        #     "\\delta": PURPLE,
        # })
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
                run_time=0.6
            )
