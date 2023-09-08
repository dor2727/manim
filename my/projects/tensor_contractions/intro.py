from consts import (
    CIRCLE_COLOR,
    INITIAL_LEG_LENGTH,
    SQUARE_COLOR,
    TRIANGLE_COLOR,
    TRIANGLE_LEG_WIDTH_OFFSET,
)

from manim import *

spacing_horizontal = 3.5


def create_body(shape: str = "square", size: float = DEFAULT_DOT_RADIUS * 3):
    # possible shape values: "dot" | "square" | "diamond"
    body: Mobject
    if shape == "dot":
        body = Dot(radius=size, color=CIRCLE_COLOR)
    else:  # square / diamond
        body = Square(side_length=size * 2, color=SQUARE_COLOR, fill_opacity=1.0)

    if shape == "diamond":
        body.rotate(PI / 4)

    return body


def create_left_leg(body: Mobject, leg_length: float = INITIAL_LEG_LENGTH):
    return Line(
        start=body.get_left(),
        end=body.get_left() + leg_length * LEFT,
    )


def create_right_leg(body: Mobject, leg_length: float = INITIAL_LEG_LENGTH):
    return Line(
        start=body.get_right(),
        end=body.get_right() + leg_length * RIGHT,
    )


def create_vector_left(shape="square", leg_length: float = INITIAL_LEG_LENGTH):
    vector = VMobject()
    vector_body = create_body(shape)
    vector.add(
        vector_body,
        create_left_leg(vector_body, leg_length),
    )
    return vector


def create_vector_right(shape="square", leg_length: float = INITIAL_LEG_LENGTH):
    vector = VMobject()
    vector_body = create_body(shape)
    vector.add(
        vector_body,
        create_right_leg(vector_body, leg_length),
    )
    return vector


def create_matrix_horizontal(
    shape="square",
    left_leg_length: float = INITIAL_LEG_LENGTH,
    right_leg_length: float = INITIAL_LEG_LENGTH,
):
    matrix = VMobject()
    matrix_body = create_body(shape)
    matrix.add(
        matrix_body,
        create_left_leg(matrix_body, left_leg_length),
        create_right_leg(matrix_body, right_leg_length),
    )
    return matrix


def create_connecting_horizontal_line(left_mobject, right_mobject):
    return Line(
        start=left_mobject.get_right(),
        end=right_mobject.get_left(),
    )


def create_surrounding_horizontal_rectangle(
    left_mobject, right_mobject, extra_width=0.3, extra_height=0.5
):
    rectangle_right_edge = right_mobject.get_right() + extra_width * RIGHT
    rectangle_left_edge = left_mobject.get_left() + extra_width * LEFT

    width = np.linalg.norm(rectangle_right_edge - rectangle_left_edge)

    return Rectangle(
        height=(DEFAULT_DOT_RADIUS * 2 + extra_height) * 2,
        width=width,
        color=RED_B,
    )


class Intro(Scene):
    def construct(self):
        # Text: We will work with
        #       - Numbers
        #       - Vectors
        #       - and Matrices
        self.introduce_mathematical_objects()
        self.wait(1)

        # Text: Though we will represent them as
        self.move_mathematical_objects_aside()
        self.wait(1)

        # Text: - dots      (number)
        #       - and lines (vector, matrix)
        #       ## <small pause>
        #       ## - and more lines connecting them    (trace, dot product)
        self.introduce_tnn_objects()
        self.wait(1)

        # Text: The shape won't matter, the number of legs does.
        #       Thus, we will sometimes draw the center as
        #       - a circle
        #       - a square
        #       - a diamond
        self.change_tnn_objects_body()
        self.wait(1)

    def introduce_mathematical_objects(self):
        self.some_number = some_number = Tex("2.4")
        some_number.shift(spacing_horizontal * LEFT)

        self.some_vector = some_vector = Matrix([[1], [2], [3]])

        self.some_matrix = some_matrix = Matrix([["\\pi", 5], [-1, "e"]])
        some_matrix.shift(spacing_horizontal * RIGHT)

        self.play(Create(some_number), run_time=0.5)
        self.wait(0.5)
        self.play(Create(some_vector), run_time=0.5)
        self.wait(0.5)
        self.play(Create(some_matrix), run_time=0.5)
        self.wait(0.5)

    def move_mathematical_objects_aside(self):
        self.play(
            self.some_number.animate.shift(2 * UP),
            self.some_vector.animate.shift(2 * UP),
            self.some_matrix.animate.shift(2 * UP),
            run_time=1.5,
        )

    def introduce_tnn_objects(self):
        self.tnn_number = tnn_number = create_body("dot")
        tnn_number.shift(spacing_horizontal * LEFT + DOWN)

        self.tnn_vector = tnn_vector = create_vector_left("dot")
        tnn_vector.shift(DOWN)

        self.tnn_matrix = tnn_matrix = create_matrix_horizontal("dot")
        tnn_matrix.shift(spacing_horizontal * RIGHT + DOWN)

        self.play(Create(tnn_number), run_time=0.5)
        self.wait(0.5)
        self.play(Create(tnn_vector), run_time=0.5)
        self.wait(0.5)
        self.play(Create(tnn_matrix), run_time=0.5)
        self.wait(0.5)

    def change_tnn_objects_body(self):
        self._change_body(self.tnn_vector, create_body("square"))

        self._change_body(self.tnn_matrix, create_body("diamond"))

    def _change_body(self, original_vmobject, new_body):
        original_body = original_vmobject.submobjects[0]

        new_body.move_to(original_body.get_center())
        self.play(Transform(original_body, new_body))


class IntroActions(Scene):
    def construct(self):
        # Text: For example,
        #       We can represent a number as a circle with no legs
        #       < pause >
        #       Likewise, taking 2 vectors
        #       < pause >
        #       And taking their dot product
        #       < pause >
        #       Gives us something that's also an object with no legs
        self.sub_scene_dot_product()
        self.wait(1)

        # self.sub_scene_matrix_vector_multiplication()
        self.wait(1)

        # self.sub_scene_matrix_matrix_multiplication()
        self.wait(1)

    def sub_scene_dot_product(self):
        tnn_number = create_body("dot")
        tnn_number.shift(spacing_horizontal * LEFT + UP)

        self.play(Create(tnn_number), run_time=0.5)
        self.wait(1)

        #     the vector on the left  will point to the right
        # and the vector on the right will point to the left
        tnn_vector_left = create_vector_right()
        tnn_vector_left.shift((spacing_horizontal + 1) * LEFT + DOWN)

        tnn_vector_right = create_vector_left()
        tnn_vector_right.shift((spacing_horizontal - 1) * LEFT + DOWN)

        self.play(Create(tnn_vector_left), Create(tnn_vector_right), run_time=0.5)
        self.wait(1)

        dot_product_line = create_connecting_horizontal_line(
            tnn_vector_left, tnn_vector_right
        )

        self.play(Create(dot_product_line), run_time=0.5)
        self.wait(1)

        surrounding_rectangle = create_surrounding_horizontal_rectangle(
            tnn_vector_left, tnn_vector_right
        )
        surrounding_rectangle.move_to(dot_product_line.get_center())

        self.play(Create(surrounding_rectangle), run_time=0.5)
        self.wait(1)


class SimpleActions(Scene):
    def construct(self):
        self.sub_scene_dot_product()

        self.wait(1)

        self.sub_scene_matrix_vector_multiplication()

        self.wait(1)

        self.sub_scene_matrix_matrix_multiplication()
        # self.sub_scene_outer_product()

    def sub_scene_dot_product(self):
        # Text: For example,
        #       We can represent a number as a circle with no legs

        tnn_number = Dot(color=CIRCLE_COLOR)
        tnn_number.shift(spacing_horizontal * LEFT + UP)
        self.play(Create(tnn_number), run_time=0.5)

        self.wait(1)

        # Text: Likewise, taking 2 vectors

        tnn_vector_left_dot = Dot(color=CIRCLE_COLOR)
        tnn_vector_left = VMobject()
        tnn_vector_left.add(
            tnn_vector_left_dot,
            Line(
                start=tnn_vector_left_dot.get_right(),
                end=tnn_vector_left_dot.get_right() + INITIAL_LEG_LENGTH * RIGHT,
            ),
        )
        tnn_vector_left.shift((spacing_horizontal + 1) * LEFT + DOWN)

        tnn_vector_right_dot = Dot(color=CIRCLE_COLOR)
        tnn_vector_right = VMobject()
        tnn_vector_right.add(
            tnn_vector_right_dot,
            Line(
                start=tnn_vector_right_dot.get_left(),
                end=tnn_vector_right_dot.get_left() + INITIAL_LEG_LENGTH * LEFT,
            ),
        )
        tnn_vector_right.shift((spacing_horizontal - 1) * LEFT + DOWN)

        self.play(Create(tnn_vector_left), Create(tnn_vector_right), run_time=0.5)

        self.wait(1)

        # Text: And taking their dot product
        dot_product_line = Line(
            start=tnn_vector_left.get_right(), end=tnn_vector_right.get_left()
        )

        self.play(Create(dot_product_line), run_time=0.5)

        self.wait(1)

        # Text: Gives us something that's also an object with no legs
        rectangle_right_edge = tnn_vector_right.get_right() + 0.5 * RIGHT
        rectangle_left_edge = tnn_vector_left.get_left() + 0.5 * LEFT
        rectangle_center_height = DOWN

        surrounding_rectangle = Rectangle(
            height=(DEFAULT_DOT_RADIUS * 2 + 0.5) * 2,
            width=np.linalg.norm(rectangle_right_edge - rectangle_left_edge),
            color=RED_B,
        )
        surrounding_rectangle.move_to(dot_product_line.get_center())

        self.play(Create(surrounding_rectangle), run_time=0.5)

        self.wait(1)

    def sub_scene_matrix_vector_multiplication(self):
        # Text: Likewise,
        #       A vector is represented with 1 leg
        tnn_vector_dot = Dot(color=CIRCLE_COLOR)
        tnn_vector = VMobject()
        tnn_vector.add(
            tnn_vector_dot,
            Line(
                start=tnn_vector_dot.get_left(),
                end=tnn_vector_dot.get_left() + INITIAL_LEG_LENGTH * LEFT,
            ),
        )
        tnn_vector.shift(UP)

        self.play(Create(tnn_vector), run_time=0.5)

        self.wait(1)

        # Text: And the result of matrix-vector multiplication

        # Maybe show each part separately
        #   matrix (show matrix)
        #   vector (show vector)
        #   multiplication (show line)

        tnn_vector_left_dot = Dot(color=CIRCLE_COLOR)
        tnn_vector_left = VMobject()
        tnn_vector_left.add(
            tnn_vector_left_dot,
            Line(
                start=tnn_vector_left_dot.get_right(),
                end=tnn_vector_left_dot.get_right() + INITIAL_LEG_LENGTH * RIGHT,
            ),
        )
        tnn_vector_left.shift(LEFT + DOWN)

        tnn_matrix_dot = Dot(color=CIRCLE_COLOR)
        tnn_matrix = VMobject()
        tnn_matrix.add(
            tnn_matrix_dot,
            Line(
                start=tnn_matrix_dot.get_right(),
                end=tnn_matrix_dot.get_right() + (INITIAL_LEG_LENGTH + 0.8) * RIGHT,
            ),
            Line(
                start=tnn_matrix_dot.get_left(),
                end=tnn_matrix_dot.get_left() + INITIAL_LEG_LENGTH * LEFT,
            ),
        )
        tnn_matrix.shift(RIGHT + DOWN)

        self.play(Create(tnn_vector_left), Create(tnn_matrix), run_time=0.5)

        self.wait(1)

        dot_product_line = Line(
            start=tnn_vector_left.get_right(), end=tnn_matrix.get_left()
        )

        self.play(Create(dot_product_line), run_time=0.5)

        self.wait(1)

        # Text: Is also a vector, which is a one-legged object
        rectangle_right_edge = (
            tnn_matrix.get_right() + 0.4 * LEFT
        )  # a bit to the left, cutting the matrix
        rectangle_left_edge = tnn_vector_left.get_left() + 0.5 * LEFT
        rectangle_center_height = DOWN

        surrounding_rectangle = Rectangle(
            height=(DEFAULT_DOT_RADIUS * 2 + 0.5) * 2,
            width=np.linalg.norm(rectangle_right_edge - rectangle_left_edge),
            color=RED_B,
        )
        surrounding_rectangle.move_to(dot_product_line.get_center())

        self.play(Create(surrounding_rectangle), run_time=0.5)

        self.wait(1)

    def sub_scene_matrix_matrix_multiplication(self):
        tnn_matrix_dot = Dot(color=CIRCLE_COLOR)
        tnn_matrix = VMobject()
        tnn_matrix.add(
            tnn_matrix_dot,
            Line(
                start=tnn_matrix_dot.get_right(),
                end=tnn_matrix_dot.get_right() + INITIAL_LEG_LENGTH * RIGHT,
            ),
            Line(
                start=tnn_matrix_dot.get_left(),
                end=tnn_matrix_dot.get_left() + INITIAL_LEG_LENGTH * LEFT,
            ),
        )
        tnn_matrix.shift(UP)

        self.play(Create(tnn_matrix), run_time=0.5)

        self.wait(1)

        # Text: And the result of matrix-vector multiplication

        # Maybe show each part separately
        #   matrix (show matrix)
        #   vector (show vector)
        #   multiplication (show line)

        tnn_matrix_left_dot = Dot(color=CIRCLE_COLOR)
        tnn_matrix_left = VMobject()
        tnn_matrix_left.add(
            tnn_matrix_left_dot,
            Line(
                start=tnn_matrix_left_dot.get_right(),
                end=tnn_matrix_left_dot.get_right() + INITIAL_LEG_LENGTH * RIGHT,
            ),
            Line(
                start=tnn_matrix_left_dot.get_left(),
                end=tnn_matrix_left_dot.get_left() + (INITIAL_LEG_LENGTH + 0.8) * LEFT,
            ),
        )
        tnn_matrix_left.shift(LEFT + DOWN)

        tnn_matrix_right_dot = Dot(color=CIRCLE_COLOR)
        tnn_matrix_right = VMobject()
        tnn_matrix_right.add(
            tnn_matrix_right_dot,
            Line(
                start=tnn_matrix_right_dot.get_right(),
                end=tnn_matrix_right_dot.get_right()
                + (INITIAL_LEG_LENGTH + 0.8) * RIGHT,
            ),
            Line(
                start=tnn_matrix_right_dot.get_left(),
                end=tnn_matrix_right_dot.get_left() + INITIAL_LEG_LENGTH * LEFT,
            ),
        )
        tnn_matrix_right.shift(RIGHT + DOWN)

        self.play(Create(tnn_matrix_left), Create(tnn_matrix_right), run_time=0.5)

        self.wait(1)

        dot_product_line = Line(
            start=tnn_matrix_left.get_right(), end=tnn_matrix_right.get_left()
        )

        self.play(Create(dot_product_line), run_time=0.5)

        self.wait(1)

        # Text: Is also a vector, which is a one-legged object
        rectangle_right_edge = (
            tnn_matrix_right.get_right() + 0.4 * LEFT
        )  # a bit to the left, cutting the matrix
        rectangle_left_edge = tnn_matrix_left.get_left() + 0.5 * LEFT
        rectangle_center_height = DOWN

        surrounding_rectangle = Rectangle(
            height=(DEFAULT_DOT_RADIUS * 2 + 0.5) * 2,
            width=np.linalg.norm(rectangle_right_edge - rectangle_left_edge),
            color=RED_B,
        )
        surrounding_rectangle.move_to(dot_product_line.get_center())

        self.play(Create(surrounding_rectangle), run_time=0.5)

        self.wait(1)

    def sub_scene_outer_product(self):
        # Text: As a last example,
        #       The outer product is a less familiar operation
        #       With a very simple TNN diagram

        tnn_matrix_dot = Dot(color=CIRCLE_COLOR)
        tnn_matrix = VMobject()
        tnn_matrix.add(
            tnn_matrix_dot,
            Line(
                start=tnn_matrix_dot.get_right(),
                end=tnn_matrix_dot.get_right() + INITIAL_LEG_LENGTH * RIGHT,
            ),
            Line(
                start=tnn_matrix_dot.get_left(),
                end=tnn_matrix_dot.get_left() + INITIAL_LEG_LENGTH * LEFT,
            ),
        )
        tnn_matrix.shift(spacing_horizontal * RIGHT + UP)

        self.play(Create(tnn_matrix), run_time=0.5)

        self.wait(1)

        # Text: You start by taking 2 vectors

        tnn_vector_pointing_left_dot = Dot(color=CIRCLE_COLOR)
        tnn_vector_pointing_left = VMobject()
        tnn_vector_pointing_left.add(
            tnn_vector_pointing_left_dot,
            Line(
                start=tnn_vector_pointing_left_dot.get_left(),
                end=tnn_vector_pointing_left_dot.get_left()
                + (INITIAL_LEG_LENGTH + 0.3) * LEFT,
            ),
        )
        tnn_vector_pointing_left.shift((spacing_horizontal - 0.5) * RIGHT + DOWN)

        tnn_vector_pointing_right_dot = Dot(color=CIRCLE_COLOR)
        tnn_vector_pointing_right = VMobject()
        tnn_vector_pointing_right.add(
            tnn_vector_pointing_right_dot,
            Line(
                start=tnn_vector_pointing_right_dot.get_right(),
                end=tnn_vector_pointing_right_dot.get_right()
                + (INITIAL_LEG_LENGTH + 0.3) * RIGHT,
            ),
        )
        tnn_vector_pointing_right.shift((spacing_horizontal + 0.5) * RIGHT + DOWN)

        self.play(
            Create(tnn_vector_pointing_left),
            Create(tnn_vector_pointing_right),
            run_time=0.5,
        )

        self.wait(1)

        # Text: and that's it. Here's a matrix.
        rectangle_right_edge = (
            tnn_vector_pointing_right.get_right() + 0.3 * LEFT
        )  # a bit to the left, cutting the vector
        rectangle_left_edge = (
            tnn_vector_pointing_left.get_left() + 0.3 * RIGHT
        )  # a bit to the right, cutting the vector
        rectangle_center_height = DOWN
        rectangle_center = (
            tnn_vector_pointing_right.get_center()
            + tnn_vector_pointing_left.get_center()
        ) / 2

        surrounding_rectangle = Rectangle(
            height=(DEFAULT_DOT_RADIUS * 2 + 0.5) * 2,
            width=np.linalg.norm(rectangle_right_edge - rectangle_left_edge),
            color=RED_B,
        )
        surrounding_rectangle.move_to(rectangle_center)

        self.play(Create(surrounding_rectangle), run_time=0.5)

        self.wait(1)
