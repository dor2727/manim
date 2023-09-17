import string

from post_1__long_matrix_multiplication_chain import MatrixMultiplicationChain_2
from utils import create_matrix_horizontal

from manim import *


class SingleMatrixTrace(Scene):
    def construct(self):
        # Test: If we have a matrix
        #       with 2 legs
        matrix = create_matrix_horizontal()
        self.play(Create(matrix), run_time=0.35)

        self.wait(1)

        # Test: We can name it
        matrix_name = Tex("$ M $")
        matrix_name.move_to(matrix.get_center() + DOWN)
        self.play(Create(matrix_name), run_time=0.25)

        self.wait(1)

        # Test: And, if we connect it's legs
        connecting_line = self.create_connecting_legs_into_trace(matrix)
        self.play(Create(connecting_line), run_time=1.25)

        self.wait(1)

        # Test: Which is like giving both legs the same name
        left_leg_name = Tex("$ \\alpha $")
        left_leg_name.move_to(matrix.get_center() + 0.5 * UP + 1.45 * LEFT)

        right_leg_name = Tex("$ \\alpha $")
        right_leg_name.move_to(matrix.get_center() + 0.5 * UP + 1.45 * RIGHT)

        self.play(Create(left_leg_name), Create(right_leg_name), run_time=0.25)

        self.wait(1)

    def create_connecting_legs_into_trace(self, matrix):
        left_edge = matrix.get_left()
        right_edge = matrix.get_right()

        left_most = left_edge + 0.5 * LEFT
        right_most = right_edge + 0.5 * RIGHT
        height = 1.5

        points = [
            left_edge,
            left_most,
            left_most + height * UP,
            right_most + height * UP,
            right_most,
            right_edge,
        ]
        lines = [Line(points[i], points[i + 1]) for i in range(len(points) - 1)]

        super_line = VMobject()
        super_line.add(*lines)

        return super_line


class TwoMatrixTrace(MatrixMultiplicationChain_2):
    def construct(self):
        # Text: Here again, we have 2 matrices
        #       this time with the same name
        #       And we wish to take their trace.
        #       Thus, first, we contract them
        super().construct()

        self.wait(1)

        # Text: And then connect the outer lines together
        connecting_line = self.create_connecting_legs_into_trace(
            self.matrices[0].get_left(), self.matrices[-1].get_right()
        )
        self.play(Create(connecting_line), run_time=1.25)

        self.wait(1)

        # Text: Which, as it is written now, has a problem
        #       since we connected alpha to gamma
        #       Thus, we needed, earlier, to name the last leg as alpha as well
        last_leg = self.leg_names[-1]
        first_leg_name = self._get_legs_names()[0]
        renamed_last_leg = Tex("$%s$" % first_leg_name)
        renamed_last_leg.move_to(last_leg.get_center())
        self.play(Transform(last_leg, renamed_last_leg), run_time=1.25)

        self.wait(1)

        # Text: as well as changing the equation
        new_equation = self.build_new_equation()
        new_equation.move_to(self.equation.get_center())
        self.play(Transform(self.equation, new_equation), run_time=1.25)

        self.wait(1)

    def _get_matrices_names(self):
        return ["M"] * self.NUM_MATRICES

    def create_connecting_legs_into_trace(self, left_edge, right_edge):
        left_most = left_edge + 0.5 * LEFT
        right_most = right_edge + 0.5 * RIGHT
        height = 1.75

        points = [
            left_edge,
            left_most,
            left_most + height * UP,
            right_most + height * UP,
            right_most,
            right_edge,
        ]
        lines = [Line(points[i], points[i + 1]) for i in range(len(points) - 1)]

        super_line = VMobject()
        super_line.add(*lines)

        return super_line

    def build_new_equation(self):
        names = self._get_matrices_names()
        leg_names = self._get_legs_names()

        leg_names[-1] = leg_names[0]

        # this is the line of change
        #   from [1:-1] to [:-1]
        names_to_sum = leg_names[:-1]
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


class TwoVerticalMatrixTrace(Scene):
    def construct(self):
        matrix_up = create_matrix_horizontal()
        matrix_up.shift(UP)

        matrix_down = create_matrix_horizontal()
        matrix_down.shift(DOWN)

        # Text: Let's take, again, the same matrix twice
        #       only this time we'll draw them vertically
        self.play(Create(matrix_up), run_time=0.35)
        self.play(Create(matrix_down), run_time=0.35)

        self.wait(1)

        right_center = (matrix_up.get_right() + matrix_down.get_right()) / 2
        right_radius = np.linalg.norm(matrix_up.get_right() - right_center)

        right_arc = Arc(
            radius=right_radius, start_angle=PI / 2, angle=-PI, arc_center=right_center
        )

        left_center = (matrix_up.get_left() + matrix_down.get_left()) / 2
        left_radius = np.linalg.norm(matrix_up.get_left() - left_center)

        left_arc = Arc(
            radius=left_radius, start_angle=PI / 2, angle=PI, arc_center=left_center
        )

        self.play(Create(right_arc), Create(left_arc), run_time=0.35)

        self.wait(1)
