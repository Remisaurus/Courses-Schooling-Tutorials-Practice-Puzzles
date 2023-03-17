#hurdle sizes became cap = 70, 22    layers = 50, 12

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.clock import Clock

class Hurdle(Widget):
    GAP_SIZE = NumericProperty(90)
    CAP_SIZE = NumericProperty(22) # Height of cap
    hurdle_center = NumericProperty(0)
    bottom_body_pos = NumericProperty(0)
    bottom_cap_pos = NumericProperty(0)
    top_body_pos = NumericProperty(0)
    top_cap_pos = NumericProperty(0)
    
    hurdle_body_texture = ObjectProperty(None)
    lower_hurdle_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))
    top_hurdle_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hurdle_body_texture = Image(source='walllayer.png').texture
        self.hurdle_body_texture.wrap = 'repeat'
        
    def on_size(self, *args):
        lower_body_size = self.bottom_cap_pos - self.bottom_body_pos
        
        amount_of_layers = lower_body_size / 12
        
        self.lower_hurdle_tex_coords[5] = int(amount_of_layers)
        self.lower_hurdle_tex_coords[7] = int(amount_of_layers) 
        
        top_body_size = self.top - self.top_body_pos
        another_amount_of_layers = top_body_size / 12
        
        self.top_hurdle_tex_coords[5] = int(another_amount_of_layers)
        self.top_hurdle_tex_coords[7] = int(another_amount_of_layers)
        
    def on_hurdle_center(self, *args):
        Clock.schedule_once(self.on_size, 0)
        
  