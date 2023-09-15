import string

from post_1__long_matrix_multiplication_chain import MatrixMultiplicationChain_2
from utils import (
    create_body,
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
        bodies = self.create_bodies()
        for body in bodies:
            self.play(Create(body), run_time=0.35)

        self.wait(1)

        # Text: And name them
        names = self.create_names()
        for name in names:
            self.play(Create(name), run_time=0.35)

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

    def _get_directions(self):
        return [
            LEFT + UP,
            RIGHT + UP,
            LEFT + DOWN,
            RIGHT + DOWN,
        ]

    def _get_names(self):
        return ["A", "B", "C", "D"]

    def create_bodies(self):
        self.bodies = [
            create_body().shift(direction) for direction in self._get_directions()
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
