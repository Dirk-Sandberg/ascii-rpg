from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty


class OutlinedBoxLayout(BoxLayout):
    inset = NumericProperty(5)
    the_line_width = NumericProperty(1)
    dash_offset = NumericProperty(10)
    dash_length = NumericProperty(10)
