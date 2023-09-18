import string

from post_1__long_matrix_multiplication_chain import MatrixMultiplicationChain_2
from utils import (
    create_A,
    create_A_dagger,
    create_connecting_horizontal_line,
    create_connecting_vertical_line,
    get_greek_letter_names,
)

from manim import *


class DrawAs(Scene):
    NUM_AS = 5
    DISTANCE_BETWEEN_AS = 2

    def construct(self):
        self.As = [create_A("$ A_{%s} $" % (i + 1)) for i in range(self.NUM_AS)]
        self.A_daggers = [
            create_A_dagger("$ A^\\dagger_{%s} $" % (i + 1)) for i in range(self.NUM_AS)
        ]

        for index, distance in enumerate(self.get_x_locations()):
            self.As[index].shift(distance * RIGHT, UP)
            self.A_daggers[index].shift(distance * RIGHT, DOWN)

        for A, A_dagger in zip(self.As, self.A_daggers):
            self.play(Create(A), Create(A_dagger), run_time=0.3)

        self.wait(1)

        self.get_connecting_lines()

        self.play(Create(self.left_line), run_time=0.3)
        for index in range(self.NUM_AS - 1):
            self.play(Create(self.spin_lines[index]), run_time=0.3)
            self.play(
                Create(self.top_lines[index]),
                Create(self.bottom_lines[index]),
                run_time=0.2,
            )
        self.play(Create(self.spin_lines[-1]), run_time=0.3)

        self.wait(1)

        self.get_leg_names()

        self.play(Create(self.left_leg_name), run_time=0.3)
        for leg_name in self.spin_leg_names:
            self.play(Create(leg_name), run_time=0.3)
        for top_leg_name, bottom_leg_name in zip(
            self.top_leg_names, self.borrom_leg_names
        ):
            self.play(Create(top_leg_name), Create(bottom_leg_name), run_time=0.3)

        self.wait(1)

    def get_x_locations(self):
        distances = np.arange(self.NUM_AS)
        # center
        distances = (
            distances - distances.mean()
        )  # not using `-=` since the object is int and the result is float
        # space
        distances = distances * self.DISTANCE_BETWEEN_AS
        return distances

    def get_connecting_lines(self):
        def _get_left_leg(A):
            return A.submobjects[1]

        def _get_right_leg(A):
            return A.submobjects[2]

        def _connect_As_horizontal(A_left, A_right):
            return create_connecting_horizontal_line(
                _get_right_leg(A_left), _get_left_leg(A_right)
            )

        self.left_line = Line(
            _get_left_leg(self.As[0]).get_left(),
            _get_left_leg(self.A_daggers[0]).get_left(),
        )

        self.spin_lines = [
            create_connecting_vertical_line(A, A_dagger)
            for A, A_dagger in zip(self.As, self.A_daggers)
        ]
        self.top_lines = [
            _connect_As_horizontal(self.As[i], self.As[i + 1])
            for i in range(self.NUM_AS - 1)
        ]
        self.bottom_lines = [
            _connect_As_horizontal(self.A_daggers[i], self.A_daggers[i + 1])
            for i in range(self.NUM_AS - 1)
        ]

        self.lines = (
            [self.left_line] + self.spin_lines + self.top_lines + self.bottom_lines
        )
        return self.lines

    def get_leg_names(self):
        def _get_center(*mobjects):
            return sum(i.get_center() for i in mobjects) / len(mobjects)

        self.left_leg_name = Tex("$ \\alpha $")
        self.left_leg_name.move_to(_get_center(self.As[0], self.A_daggers[0]))
        self.left_leg_name.shift(LEFT)

        def _create_spin_leg(index, A, A_dagger):
            leg_name = Tex("$\\sigma_{%s}$" % (index + 1))
            leg_name.move_to(_get_center(A, A_dagger))
            leg_name.shift(0.5 * RIGHT)
            return leg_name

        self.spin_leg_names = [
            _create_spin_leg(index, A, A_dagger)
            for index, (A, A_dagger) in enumerate(zip(self.As, self.A_daggers))
        ]

        virtual_leg_names = get_greek_letter_names()[1 : self.NUM_AS + 1]

        def _create_virtual_leg(index, A):
            leg_name = Tex("$\\%s$" % virtual_leg_names[index].lower())
            leg_name.move_to(_get_center(A))
            leg_name.shift(self.DISTANCE_BETWEEN_AS / 2 * RIGHT)
            leg_name.shift(0.5 * UP)
            return leg_name

        self.top_leg_names = [
            _create_virtual_leg(index, A) for index, A in enumerate(self.As)
        ]

        def _create_virtual_leg_dagger(index, A_dagger):
            leg_name = Tex("$\\%s'$" % virtual_leg_names[index].lower())
            leg_name.move_to(_get_center(A_dagger))
            leg_name.shift(self.DISTANCE_BETWEEN_AS / 2 * RIGHT)
            leg_name.shift(0.5 * DOWN)
            return leg_name

        self.borrom_leg_names = [
            _create_virtual_leg_dagger(index, A_dagger)
            for index, A_dagger in enumerate(self.A_daggers)
        ]


class CloseZipperGrowing(DrawAs):
    def construct(self):
        pass


class CloseZipperCentered(DrawAs):
    def construct(self):
        pass
