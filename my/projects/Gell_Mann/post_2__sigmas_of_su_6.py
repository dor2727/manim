from manim import *


class DrawSigmas(Scene):
    N = 6

    def construct(self):
        sigmas = []
        for plus in range(self.N - 1):
            for minus in range(plus + 1, self.N):
                plus_minus = VMobject()
                plus_minus.add(
                    Tex("$\\sigma_{%d,%d}$" % (plus + 1, minus + 1)).shift(UP),
                    Tex("$1$").shift(plus * DOWN),
                    Tex("$-1$").shift(minus * DOWN),
                )
                sigmas.append(plus_minus)

        for index, mobj in enumerate(sigmas):
            mobj.shift(
                2 * UP,
                (len(sigmas) / 2) * LEFT,
                index * RIGHT,
            )

        barriers = []
        for index, mobj in enumerate(sigmas[:-1]):
            barrier = DashedLine(2.2 * UP, self.N * DOWN)
            right_edge = mobj.get_right()
            right_edge_value = np.dot(right_edge, RIGHT)
            barrier.shift(
                right_edge_value * RIGHT,
                0.1 * RIGHT,
                2 * UP,
            )
            barriers.append(barrier)

        self.add(*sigmas, *barriers)

        self.camera.frame_width *= 1.25
        self.camera.frame_height *= 1.25
