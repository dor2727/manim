from consts import (
    CIRCLE_COLOR,
    INITIAL_LEG_LENGTH,
    SQUARE_COLOR,
    TRIANGLE_COLOR,
    TRIANGLE_LEG_WIDTH_OFFSET,
)

from manim import *

spacing_horizontal = 4.5


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


def create_up_leg(body: Mobject, leg_length: float = INITIAL_LEG_LENGTH):
    return Line(
        start=body.get_top(),
        end=body.get_top() + leg_length * UP,
    )


def create_down_leg(body: Mobject, leg_length: float = INITIAL_LEG_LENGTH):
    return Line(
        start=body.get_bottom(),
        end=body.get_bottom() + leg_length * DOWN,
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


def create_matrix_vertical(
    shape="square",
    up_leg_length: float = INITIAL_LEG_LENGTH,
    down_leg_length: float = INITIAL_LEG_LENGTH,
):
    matrix = VMobject()
    matrix_body = create_body(shape)
    matrix.add(
        matrix_body,
        create_up_leg(matrix_body, up_leg_length),
        create_down_leg(matrix_body, down_leg_length),
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


def get_all_greek_letters():
    # https://stackoverflow.com/questions/47956451/get-a-list-of-all-greek-unicode-characters
    from itertools import chain

    greek_codes = chain(range(0x370, 0x3E2), range(0x3F0, 0x400))
    greek_symbols = (chr(c) for c in greek_codes)
    greek_letters = [c for c in greek_symbols if c.isalpha()]


def get_greek_letters():
    alpha_code = 945
    omega_code = 969
    greek_codes = range(alpha_code, omega_code + 1)
    greek_symbols = map(chr, greek_codes)
    return list(greek_symbols)


def get_greek_letter_names():
    return [
        "Alpha",
        "Beta",
        "Gamma",
        "Delta",
        "Epsilon",
        "Zeta",
        "Eta",
        "Theta",
        "Iota",
        "Kappa",
        "Lambda",
        "Mu",
        "Nu",
        "Xi",
        "Omicron",
        "Pi",
        "Rho",
        "Sigma",
        "Tau",
        "Upsilon",
        "Phi",
        "Chi",
        "Psi",
        "Omega",
    ]
