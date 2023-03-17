from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, PushMatrix, PopMatrix, Rotate
from kivy.clock import Clock

class Master(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.change = 0
        with self.canvas:
            PushMatrix()
            # setup a default size for the object
            self.size = (25, 200)
            # center the widget
            self.pos = (300, 300)
            self.rot = Rotate()
            self.rot.origin = (self.pos[0] + 0.5 * self.size[0], self.pos[1])# + 0.5 * self.size[1])
            #self.rot.axis = (0, 0, 1)
            self.rot.angle = 45
            # this line creates a rectangle
            self.rect = Rectangle(pos=self.pos,
                                     size=self.size)
            PopMatrix()
        
        Clock.schedule_interval(self.rotate, 0)
        
    def rotate(self, dt):
        print(self.rot.angle, self.rect.size)
        self.rot.angle -= 1
        self.change += 1
        #self.rect.pos = (self.rect.pos[0], self.rect.pos[1]+1)
        #self.rot.origin = (self.rect.pos[0] + 12.5 , self.rect.pos[1])
        if self.rot.angle >= 360:
            self.rot.angle -= 360
            
class Constructor_Conductor(App):
    def build(self):
        return Master()
       
if __name__ == '__main__':
    app = Constructor_Conductor()
    app.run()