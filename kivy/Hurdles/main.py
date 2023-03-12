from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty

class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cloud_texture = Image(source = 'cloud.png').texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (3 * Window.width / self.cloud_texture.width, -1)
        self.floor_texture = Image(source = 'floor.png').texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (0.1 * Window.width / self.floor_texture.width, -1)

    def scroll_textures(self, dt):
        self.cloud_texture.uvpos = ( (self.cloud_texture.uvpos[0] + dt/5.0) % Window.width , self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ( (self.floor_texture.uvpos[0] + dt/5) % Window.width , self.floor_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)
        texture2 = self.property('floor_texture')
        texture2.dispatch(self)
  
class Mainapp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1 / 60)
    
Mainapp().run()