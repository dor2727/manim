from manim import *

from .consts import *

class LeggedTriangle(VMobject):
    def __init__(self, base_length: float, height: float, name: str='A', color=TRIANGLE_COLOR, **kwargs):
        super().__init__(color=color, **kwargs)

        triangle = self.create_triangle(base_length, height)
        legs = self.create_legs(base_length)
        self.add(triangle, *legs)

        if name:
            self.add_name(name)

    def create_triangle(self, base_length: float, height: float):
        edges = [
            height * UP,
            (base_length / 2) * RIGHT,
            (base_length / 2) * LEFT,
        ]
        shifted_edges = [
            e - (height / 3)*UP
            for e in edges
        ]
        self.triangle = Polygram(shifted_edges, color=TRIANGLE_COLOR, fill_opacity=0.75)
        return self.triangle

    def create_legs(self, base_length: float):
        triangle_top = self.triangle.get_top()
        top_leg = Line(start=triangle_top, end=triangle_top + INITIAL_LEG_LENGTH * UP)

        triangle_bottom = self.triangle.get_bottom()
        triangle_width = base_length / 2

        right_leg_start = triangle_bottom + (triangle_width - TRIANGLE_LEG_WIDTH_OFFSET) * RIGHT
        right_leg = Line(start=right_leg_start, end=right_leg_start + INITIAL_LEG_LENGTH * DOWN)

        left_leg_start = triangle_bottom + (triangle_width - TRIANGLE_LEG_WIDTH_OFFSET) * LEFT
        left_leg = Line(start=left_leg_start, end=left_leg_start + INITIAL_LEG_LENGTH * DOWN)

        self.legs = [top_leg, right_leg, left_leg]
        return self.legs

    def add_name(self, name: str):
        self.name_tex = name_tex = Tex(name)

        self.add(name_tex)
        return name_tex

class UpperTriangle(LeggedTriangle):
    def create_triangle(self, base_length: float, height: float):
        edges = [
            height * UP,
            (base_length / 2) * RIGHT,
            (base_length / 2) * LEFT,
        ]
        shifted_edges = [
            e - (height / 3)*UP
            for e in edges
        ]
        self.triangle = Polygram(shifted_edges, color=TRIANGLE_COLOR, fill_opacity=0.75)
        return self.triangle

    def create_legs(self, base_length: float):
        triangle_top = self.triangle.get_top()
        top_leg = Line(start=triangle_top, end=triangle_top + INITIAL_LEG_LENGTH * UP)

        triangle_bottom = self.triangle.get_bottom()
        triangle_width = base_length / 2

        right_leg_start = triangle_bottom + (triangle_width - TRIANGLE_LEG_WIDTH_OFFSET) * RIGHT
        right_leg = Line(start=right_leg_start, end=right_leg_start + INITIAL_LEG_LENGTH * DOWN)

        left_leg_start = triangle_bottom + (triangle_width - TRIANGLE_LEG_WIDTH_OFFSET) * LEFT
        left_leg = Line(start=left_leg_start, end=left_leg_start + INITIAL_LEG_LENGTH * DOWN)

        self.legs = [top_leg, right_leg, left_leg]
        return self.legs

class LowerTriangle(LeggedTriangle):
    def create_triangle(self, base_length: float, height: float):
        edges = [
            height * DOWN,
            (base_length / 2) * RIGHT,
            (base_length / 2) * LEFT,
        ]
        shifted_edges = [
            e - (height / 3)*DOWN
            for e in edges
        ]
        self.triangle = Polygram(shifted_edges, color=TRIANGLE_COLOR, fill_opacity=0.75)
        return self.triangle

    def create_legs(self, base_length: float):
        triangle_bottom = self.triangle.get_bottom()
        bottom_leg = Line(start=triangle_bottom, end=triangle_bottom + INITIAL_LEG_LENGTH * DOWN)

        triangle_top = self.triangle.get_top()
        triangle_width = base_length / 2

        right_leg_start = triangle_top + (triangle_width - TRIANGLE_LEG_WIDTH_OFFSET) * RIGHT
        right_leg = Line(start=right_leg_start, end=right_leg_start + INITIAL_LEG_LENGTH * UP)

        left_leg_start = triangle_top + (triangle_width - TRIANGLE_LEG_WIDTH_OFFSET) * LEFT
        left_leg = Line(start=left_leg_start, end=left_leg_start + INITIAL_LEG_LENGTH * UP)

        self.legs = [bottom_leg, right_leg, left_leg]
        return self.legs
        

class TestScene(Scene):

    def construct(self):
        A = UpperTriangle(2, 1)
        A.shift(UP)
        self.add(A)

        A_dagger = LowerTriangle(2, 1)
        A_dagger.shift(DOWN)
        self.add(A_dagger)

        # numberplane = NumberPlane(
        #     x_range=[-6, 6],
        #     y_range=[-6, 6],
        # )
        # self.add(numberplane)
