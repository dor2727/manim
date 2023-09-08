from manim import *


class SimpleThetaDotCircle(Scene):
    omega = 1
    alpha = 1

    def theta_dot_of_theta(self, theta: float = None) -> float:
        if theta is None:
            theta = self.theta

        return 1.0

    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([0, 0, 0])
        x_end = np.array([TAU, 0, 0])

        # PI is x_midpoint
        y_start = np.array([PI, -2, 0])
        y_end = np.array([PI, 2, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

    def add_x_labels(self):
        x_labels = [
            MathTex("- \\pi"),
            MathTex("-\\frac{\\pi}{2}"),
            MathTex("\\frac{\\pi}{2}"),
            MathTex("\\pi"),
        ]
        x_label_location = [-PI, -PI / 2, PI / 2, PI]

        for label, loc in zip(x_labels, x_label_location):
            label.scale(0.5)
            label.next_to(np.array([PI + loc, 0, 0]), DOWN)
            self.add(label)

        y_labels = [
            MathTex("1"),
            MathTex("-1"),
        ]
        y_label_location = [1, -1]
        for label, loc in zip(y_labels, y_label_location):
            label.scale(0.5)
            label.next_to(np.array([PI, loc, 0]), LEFT)
            self.add(label)

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to([-PI, 0, 0])
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        # orbit = self.circle
        origin_point = self.circle.get_center()

        starting_theta = PI / 3
        self.theta = starting_theta

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(self.circle.point_from_proportion(self.theta / TAU % 1))

        def go_around_circle(mob, dt):
            self.theta += dt * self.theta_dot_of_theta()
            if self.theta > PI:
                self.theta -= TAU
            if self.theta < -PI:
                self.theta += TAU
            mob.move_to(self.circle.point_from_proportion(self.theta / TAU % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            return Line(
                dot.get_center(), self._get_x_y(), color=YELLOW_A, stroke_width=2
            )

        self.curve_trace = VGroup()
        self.curve_trace.add(Dot(self._get_x_y(), radius=0.08, color=RED))

        def add_curve_trace():
            self.curve_trace[-1].scale(0.25)
            self.curve_trace.add(Dot(self._get_x_y(), radius=0.08, color=RED))
            return self.curve_trace[-250:]

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        curve_trace = always_redraw(add_curve_trace)

        self.add(dot)
        self.add(self.circle, origin_to_circle_line, dot_to_curve_line, curve_trace)
        self.wait(9.5)

        dot.remove_updater(go_around_circle)

    def _get_x_y(self, theta: float = None) -> np.ndarray:
        if theta is None:
            theta = self.theta

        return np.array([PI + theta, self.theta_dot_of_theta(theta), 0])


class AbsThetaDotCircle(SimpleThetaDotCircle):
    def theta_dot_of_theta(self, theta: float = None) -> float:
        if theta is None:
            theta = self.theta

        return abs(self.theta) + 0.1


class ChaosThetaDotCircle(SimpleThetaDotCircle):
    omega = 1.5

    def theta_dot_of_theta(self, theta: float = None) -> float:
        if theta is None:
            theta = self.theta

        return self.omega - self.alpha * np.sin(theta)
