from manim import *
import itertools

COLORS = {
	'A': BLUE,
	'B': GREEN,
	'C': RED,
}

HEIGHT = 1

X_RANGE = (8, 20, 0.5)
X_LENGTH = 6

CREATE_RECTANGLES = True
HAVE_RECTANGLES_AROUND = False
DECREASE_RECTANGLE_CREATION_TIME = False
def run_time(index: int):
	res = 0.1 - 0.01*index
	if res < 0.02:
		res = 0.02
	return res

CREATE_SIN_FUNCTIONS = True
HAVE_SIN_FUNCTIONS_AROUND = False

FADE_OUT_RECTANGLES = True

class ContextSwitchShort(Scene):
	short = True

	def construct(self):
		number_plane = self.add_number_plane()

		a_rectangles, b_rectangles, c_rectangles = self.create_rectangles()

		if CREATE_RECTANGLES:
			if DECREASE_RECTANGLE_CREATION_TIME:
				for i in range(len(b_rectangles)):
					self.play(FadeIn(a_rectangles[i*2    ]), run_time=run_time(4*i))
					self.play(FadeIn(b_rectangles[i      ]), run_time=run_time(4*i+1))
					self.play(FadeIn(a_rectangles[i*2 + 1]), run_time=run_time(4*i+2))
					self.play(FadeIn(c_rectangles[i      ]), run_time=run_time(4*i+3))

			else:
				for i in range(len(b_rectangles)):
					self.play(FadeIn(a_rectangles[i*2    ]), run_time=0.25)
					self.play(FadeIn(b_rectangles[i      ]), run_time=0.25)
					self.play(FadeIn(a_rectangles[i*2 + 1]), run_time=0.25)
					self.play(FadeIn(c_rectangles[i      ]), run_time=0.25)

			if self.short:
				self.wait(2)
			else:
				self.wait(1)
		elif HAVE_RECTANGLES_AROUND:
			self.add(*a_rectangles, *b_rectangles, *c_rectangles)

		a_sin_func, b_sin_func, c_sin_func = self.create_sin_functions()
		if CREATE_SIN_FUNCTIONS:
			if self.short:
				self.wait(0.2)

			self.play(Create(a_sin_func), run_time=1.5)
			self.play(Create(b_sin_func), run_time=1.5)
			self.play(Create(c_sin_func), run_time=1.5)

			if self.short:
				self.wait(2)
			else:
				self.wait(1)
		elif HAVE_SIN_FUNCTIONS_AROUND:
			self.add(a_sin_func, b_sin_func, c_sin_func)

		if FADE_OUT_RECTANGLES:
			self.play(*[
				FadeOut(rec)
				for rec in itertools.chain(a_rectangles, b_rectangles, c_rectangles)
			])
			self.play(FadeOut(self.number_plane))

			if self.short:
				self.wait(2)
			else:
				self.wait(1)

	def add_number_plane(self):
		self.number_plane = number_plane = NumberPlane(
			x_range=X_RANGE,
			y_range=(0, 1, 1),
			x_length=X_LENGTH,
			y_length=HEIGHT,
			background_line_style={
				"stroke_opacity": 0
			}
		).add_coordinates(
			{h: f"{h:02d}:00" for h in range(X_RANGE[0], X_RANGE[1]+1, 2)},
			direction=1.3*DOWN
		)

		number_plane.get_x_axis().add_ticks()

		self.add(number_plane)

		labels = number_plane.get_x_axis().labels
		number_plane.get_x_axis().labels.shift(3*LEFT)
		number_plane.get_x_axis().labels.shift(3*RIGHT)

		return number_plane

	def create_rectangles(self):
		a_rectangles = [
			self.place_rectangle_at_hour('A', h, 0.5)
			for h in range(X_RANGE[0], X_RANGE[1])
		]
		b_rectangles = [
			self.place_rectangle_at_hour('B', h+0.5, 0.5)
			for h in range(X_RANGE[0], X_RANGE[1], 2)
		]
		c_rectangles = [
			self.place_rectangle_at_hour('C', h+0.5, 0.5)
			for h in range(X_RANGE[0]+1, X_RANGE[1], 2)
		]

		# self.add(*a_rectangles, *b_rectangles, *c_rectangles)
		return a_rectangles, b_rectangles, c_rectangles

	def place_rectangle_at_hour(self, group: str, start_hour: float, duration_in_hours: float):
		color = COLORS.get(group, GREY)

		hour_rescale = (X_LENGTH / (X_RANGE[1] - X_RANGE[0]))

		rescale_duration_in_hours = duration_in_hours * hour_rescale

		# shift by start of x axis
		rescale_start_hour = (start_hour - X_RANGE[0])
		# rescale
		rescale_start_hour *= hour_rescale
		# move to start of axis
		rescale_start_hour = rescale_start_hour - 3 + (rescale_duration_in_hours / 2)

		# # 4 is 24/6, which is x_range / x_length
		# rescale_start_hour = start_hour / 4 - 3

		rec = Rectangle(
			color,
			fill_color=color,
			fill_opacity=0.7,
			width=rescale_duration_in_hours,
			height=HEIGHT,

		).move_to(rescale_start_hour*RIGHT)

		text = Text(group, font_size=17).move_to(rec.get_center())

		return VGroup(rec, text)


	def _create_single_sin_function(self, group: str, frequency: float, phase: float):
		return FunctionGraph(
			lambda h: np.sin(frequency * (h + phase) * np.pi),
			x_range=[- X_LENGTH/2 , X_LENGTH/2 ],
			color=COLORS.get(group, GREY),
		)

	def create_sin_functions(self):
		a_frequency = 4
		a_phase = 0
		a_sin_func = self._create_single_sin_function('A', a_frequency, a_phase)

		b_frequency = 2
		b_phase = -1/8
		b_sin_func = self._create_single_sin_function('B', b_frequency, b_phase)

		c_frequency = 2
		c_phase = -5/8
		c_sin_func = self._create_single_sin_function('C', c_frequency, c_phase)

		return a_sin_func, b_sin_func, c_sin_func


class ContextSwitchLong(ContextSwitchShort):
	short = False

	def create_rectangles(self):
		a_rectangles = [
			self.place_rectangle_at_hour('A', h, 3)
			for h in (8, 8+6)
		]
		b_rectangles = [
			self.place_rectangle_at_hour('B', 8+3, 3)
		]
		c_rectangles = [
			self.place_rectangle_at_hour('C', 8+6+3, 3)
		]

		# self.add(*a_rectangles, *b_rectangles, *c_rectangles)
		return a_rectangles, b_rectangles, c_rectangles

	def create_sin_functions(self):
		ratio_short_long = 0.5 / 3 # 1/6

		a_frequency = 4 * ratio_short_long
		a_phase = 0
		a_sin_func = self._create_single_sin_function('A', a_frequency, a_phase)

		b_frequency = 2 * ratio_short_long
		b_phase = -5/8 / ratio_short_long
		b_sin_func = self._create_single_sin_function('B', b_frequency, b_phase)

		c_frequency = 2 * ratio_short_long
		c_phase = -1/8 / ratio_short_long
		c_sin_func = self._create_single_sin_function('C', c_frequency, c_phase)

		return a_sin_func, b_sin_func, c_sin_func

