import string

from utils import (
    create_body,
    create_connecting_horizontal_line,
    create_left_leg,
    create_matrix_horizontal,
    create_right_leg,
    create_surrounding_horizontal_rectangle,
    create_vector_left,
    create_vector_right,
    get_greek_letter_names,
    spacing_horizontal,
)

from manim import *


class MatrixMultiplicationChain(Scene):
    NUM_MATRICES: int

    def construct(self):
        matrices = self.create_matrices()
        names = self.create_names()
        leg_names = self.create_leg_names()
        dot_product_lines = self.create_dot_product_lines()

        # Text: We can lay down a few matrices
        for matrix in matrices:
            self.play(Create(matrix), run_time=0.35)

        self.wait(1)

        # Text: And we can name them
        for name in names:
            self.play(Create(name), run_time=0.25)

        self.wait(1)

        # Text: As well as naming their legs
        for leg_name in leg_names:
            self.play(Create(leg_name), run_time=0.25)

        self.wait(1)

        # Text: And, we can construct them
        for dot_product_line in dot_product_lines:
            self.play(Create(dot_product_line), run_time=0.25)

        self.wait(1)

        # Text: Which is a diagrammatic way of representing the following equation
        equation = self.build_equation()
        equation.shift(2 * DOWN)
        self.play(Create(equation), run_time=2)

        self.wait(1)

    def _get_matrices_names(self):
        return list(string.ascii_uppercase[: self.NUM_MATRICES])

    def _get_legs_names(self):
        greek_letter_names = get_greek_letter_names()[: self.NUM_MATRICES + 1]
        greek_letters = ["\\" + c.lower() for c in greek_letter_names]
        return greek_letters

    def create_matrices(self):
        matrices = []
        for pos in self.get_positions():
            matrix = create_matrix_horizontal()
            matrix.move_to(pos)
            matrices.append(matrix)

        self.matrices = matrices
        return matrices

    def create_names(self):
        names = []
        for matrix, name in zip(self.matrices, self._get_matrices_names()):
            matrix_name = Tex("$%s$" % name)
            matrix_name.move_to(matrix.get_center() + UP)
            names.append(matrix_name)

        self.names = names
        return names

    def create_leg_names(self):
        positions = self.get_positions()
        names = self._get_legs_names()

        leg_names = []

        # handle the first
        leg_name = Tex("$%s$" % names[0])
        leg_name.move_to(positions[0] + 1.25 * LEFT + DOWN)
        leg_names.append(leg_name)

        # handle the middle
        for index in range(len(positions) - 1):
            pos = (positions[index] + positions[index + 1]) / 2

            leg_name = Tex("$%s$" % names[index + 1])
            leg_name.move_to(pos + DOWN)
            leg_names.append(leg_name)

        # handle the last
        leg_name = Tex("$%s$" % names[-1])
        leg_name.move_to(positions[-1] + 1.25 * RIGHT + DOWN)
        leg_names.append(leg_name)

        self.leg_names = leg_names
        return leg_names

    def create_dot_product_lines(self):
        dot_product_lines = []

        for index in range(len(self.matrices) - 1):
            dot_product_lines.append(
                create_connecting_horizontal_line(
                    self.matrices[index], self.matrices[index + 1]
                )
            )

        self.dot_product_lines = dot_product_lines
        return dot_product_lines

    def build_equation(self):
        names = self._get_matrices_names()
        leg_names = self._get_legs_names()

        names_to_sum = leg_names[1:-1]
        # string_sum = "\\sum_{%s}" % (" , ".join(names_to_sum))
        string_sum = " ".join("\\sum_{%s}" % name for name in names_to_sum)

        string_matrices = " ".join(
            "{}_{{{} , {}}}".format(
                names[index], leg_names[index], leg_names[index + 1]
            )
            for index in range(len(names))
        )

        string_equation = f"${string_sum} {string_matrices}$"
        print(string_equation)
        return Tex(string_equation)


class MatrixMultiplicationChain_2(MatrixMultiplicationChain):
    NUM_MATRICES = 2

    def get_positions(self):
        return [
            LEFT,
            RIGHT,
        ]


class MatrixMultiplicationChain_4(MatrixMultiplicationChain):
    NUM_MATRICES = 4

    def get_positions(self):
        return [
            3 * LEFT,
            LEFT,
            RIGHT,
            3 * RIGHT,
        ]
