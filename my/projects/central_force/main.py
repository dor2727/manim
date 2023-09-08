from manim import *

COLORS = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
NUM_DOTS = len(COLORS)

def get_initial_position_from_index(index: int) -> np.ndarray:
    return RIGHT * (3 + 0.1*index)

def get_force_power_from_initial_position(index: int) -> float:
    return 2 + 0.1*index

class LagRatios(Scene):

    def construct(self):
        center = Dot()

        moving_dots = self._create_moving_dots()

        numberplane = NumberPlane(
            x_range=[-6, 6, 0.25],
            y_range=[-6, 6, 0.25],
        )

        self.add(center, moving_dots, numberplane)


    def _create_moving_dots(self):
        return VGroup(*[
            Dot(get_initial_position_from_index(i), color=color)
            for i, color in zip(range(NUM_DOTS), COLORS)
        ])