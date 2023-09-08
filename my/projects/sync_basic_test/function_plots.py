from manim import *


class Chapter4_3_Eq1(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, TAU / 8],
            y_range=[-2, 2, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-PI, PI, TAU / 8),
                "numbers_with_elongated_ticks": np.arange(-2, 2, 1),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()

        # theta_dot = omega - a sin(theta)
        omega = 0.9
        a = 1
        the_function = axes.plot(lambda theta: omega - a * np.sin(theta), color=BLUE)

        the_label = axes.get_graph_label(
            the_function, f"\\omega={omega} ; a={a}", x_val=-10, direction=UP
        )

        plot = VGroup(axes, the_function)
        labels = VGroup(axes_labels, the_label)
        self.add(plot, labels)
