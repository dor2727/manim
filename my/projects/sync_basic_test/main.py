from manim import *

class ACircleWith2Dots(Scene):
    def construct(self):
        r = 1.5
        circle = Circle(radius=r)

        d1 = Dot(r*RIGHT, radius=.3)
        d2 = Dot(r*LEFT , radius=.3)

        self.play(Create(circle))
        self.play(SpiralIn(d1))
        self.play(DrawBorderThenFill(d2))
        


class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
