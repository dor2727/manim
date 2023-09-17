from utils import (
    create_body,
    create_connecting_horizontal_line,
    create_left_leg,
    create_matrix_horizontal,
    create_right_leg,
    create_surrounding_horizontal_rectangle,
    create_vector_left,
    create_vector_right,
    spacing_horizontal,
)

from manim import *


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

        self.number_name = Text("Number")
        self.number_name.move_to(self.some_number.get_center() + 2 * UP)

        self.vector_name = Text("Vector")
        self.vector_name.move_to(self.some_vector.get_center() + 2 * UP)

        self.matrix_name = Text("Matrix")
        self.matrix_name.move_to(self.some_matrix.get_center() + 2 * UP)

        self.play(Create(some_number), Create(self.number_name), run_time=0.5)
        self.wait(0.5)
        self.play(Create(some_vector), Create(self.vector_name), run_time=0.5)
        self.wait(0.5)
        self.play(Create(some_matrix), Create(self.matrix_name), run_time=0.5)
        self.wait(0.5)

    def move_mathematical_objects_aside(self):
        self.play(
            self.some_number.animate.shift(2 * DOWN),
            self.some_vector.animate.shift(2 * DOWN),
            self.some_matrix.animate.shift(2 * DOWN),
            run_time=1.5,
        )

    def introduce_tnn_objects(self):
        self.tnn_number = tnn_number = create_body("dot")
        tnn_number.shift(spacing_horizontal * LEFT)

        self.tnn_vector = tnn_vector = create_vector_left("dot")
        # tnn_vector.shift()

        self.tnn_matrix = tnn_matrix = create_matrix_horizontal("dot")
        tnn_matrix.shift(spacing_horizontal * RIGHT)

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

        # Text: Likewise,
        #       A vector is represented with 1 leg
        #       < pause >
        #       And the result of:
        #         - matrix
        #         - vector
        #         - multiplication
        #       < pause >
        #       Is also a vector, which is a one-legged object
        self.sub_scene_matrix_vector_multiplication()
        self.wait(1)

        # Text: And, similarly,
        #       A matrix is represented with 2 legs
        #       < pause >
        #       And the result of:
        #         - matrix
        #         - matrix
        #         - multiplication
        #       < pause >
        #       Is also a matrix, with 2 legs sticking out
        self.sub_scene_matrix_matrix_multiplication()
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

    def sub_scene_matrix_vector_multiplication(self):
        tnn_vector_representation = create_vector_left()
        tnn_vector_representation.shift(UP)

        self.play(Create(tnn_vector_representation), run_time=0.5)
        self.wait(1)

        tnn_matrix = create_matrix_horizontal(left_leg_length=INITIAL_LEG_LENGTH + 0.3)
        tnn_matrix.shift(LEFT + DOWN)
        self.play(Create(tnn_matrix), run_time=0.5)
        self.wait(0.25)

        tnn_vector = create_vector_left()
        tnn_vector.shift(RIGHT + DOWN)
        self.play(Create(tnn_vector), run_time=0.5)
        self.wait(0.5)

        dot_product_line = create_connecting_horizontal_line(tnn_matrix, tnn_vector)
        self.play(Create(dot_product_line), run_time=0.5)
        self.wait(1)

        surrounding_rectangle = create_surrounding_horizontal_rectangle(
            tnn_matrix, tnn_vector, extra_width=0
        )
        surrounding_rectangle.move_to(dot_product_line.get_center())

        self.play(Create(surrounding_rectangle), run_time=0.5)
        self.wait(1)

    def sub_scene_matrix_matrix_multiplication(self):
        tnn_matrix_representation = create_matrix_horizontal()
        tnn_matrix_representation.shift(spacing_horizontal * RIGHT + UP)

        self.play(Create(tnn_matrix_representation), run_time=0.5)
        self.wait(1)

        tnn_matrix_left = create_matrix_horizontal(
            left_leg_length=INITIAL_LEG_LENGTH + 0.3
        )
        tnn_matrix_left.shift(spacing_horizontal * RIGHT + LEFT + DOWN)
        self.play(Create(tnn_matrix_left), run_time=0.5)
        self.wait(0.25)

        tnn_matrix_right = create_matrix_horizontal(
            right_leg_length=INITIAL_LEG_LENGTH + 0.3
        )
        tnn_matrix_right.shift(spacing_horizontal * RIGHT + RIGHT + DOWN)
        self.play(Create(tnn_matrix_right), run_time=0.5)
        self.wait(0.5)

        dot_product_line = create_connecting_horizontal_line(
            tnn_matrix_left, tnn_matrix_right
        )
        self.play(Create(dot_product_line), run_time=0.5)
        self.wait(1)

        surrounding_rectangle = create_surrounding_horizontal_rectangle(
            tnn_matrix_left, tnn_matrix_right, extra_width=-0.3
        )
        surrounding_rectangle.move_to(dot_product_line.get_center())

        self.play(Create(surrounding_rectangle), run_time=0.5)
        self.wait(1)
