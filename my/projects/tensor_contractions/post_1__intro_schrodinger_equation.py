from utils import (
    PhysicsTex,
    create_connecting_horizontal_line,
    create_matrix_horizontal,
    create_vector_left,
)

from manim import *


class SchrodingerEquationInTNN(Scene):
    def construct(self):
        self.add_left_side()

        equal = Tex("$=$")
        equal.shift(1.1 * DOWN)
        self.add(equal)

        self.add_right_side()

    def add_left_side(self):
        psi_left = create_vector_left("dot")
        psi_left.shift(LEFT + 1.1 * DOWN)

        dot = Dot()
        dot.move_to(psi_left.submobjects[0].get_center() + 0.5 * UP)

        self.add(psi_left, dot)

    def add_right_side(self):
        H = create_matrix_horizontal()
        H.shift(RIGHT + 1.1 * DOWN)

        psi_right = create_vector_left("dot")
        psi_right.move_to(H.get_center() + RIGHT)

        contraction_line = create_connecting_horizontal_line(H, psi_right)

        self.add(H, psi_right, contraction_line)


class ChangeEquation(SchrodingerEquationInTNN):
    def construct(self):
        from_text = Text("From this:")
        from_text.shift(2.1 * UP + 2 * LEFT)

        equation = PhysicsTex(
            "$i \\hbar \\frac{d}{dt} \\ket{\\psi} = \\hat{H} \\ket{\\psi}$"
        )
        equation.shift(UP)

        to_text = Text("To this:")
        to_text.align_to(from_text, LEFT)

        self.add(from_text, equation, to_text)

        super().construct()
