from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class WidgetsExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    my_count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('default')
    my_slider = StringProperty(str(50))
    my_text_input = StringProperty('initial text')
        
    def on_button_click(self):
        print('button clicked')
        if self.count_enabled:
            self.my_count += 1
            self.my_text = str(self.my_count)
        
    def on_toggle_state(self, toggle_button):
        print('toggled ' + toggle_button.state)
        if toggle_button.state == 'down':
            print('on')
            toggle_button.text = 'on'
            self.count_enabled = True
        else:
            print('off')
            toggle_button.text='off'
            self.count_enabled = False
            
    def on_active_switch(self, switch):
        print('toggled switch to: ' + str(switch.active) )

    def on_slider_value(self, slider):
        print('slided to: ' + str(slider.value))
        # self.my_slider = str(int(slider.value))
    
    def on_text_validate(self, textinput):
        self.my_text_input = "you just validated: " + textinput.text
        
class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=(300,50), size= (50, 50))
            Color(1,0,0,1)
            Line(points=(100,100,200,200), width = 8)
            Color(0,0,1,1)
            Line(circle=(200,200,20),width = 2)
            Line(rectangle=(50,100,20,20))
            
    def pressed_move(self):
        print('ff')
        x, y = self.rect.pos
        w, h = self.rect.size
        x += dp(10)
        if x + w > self.width:
            x = self.width - w
        self.rect.pos = (x, y)
    
class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = 2
        self.vy = 2
        with self.canvas:
            self.ball = Ellipse(pos=(100,100), size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    def on_size(self, *args):
        print(self.width, self.height)  
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)
    def update(self, dt):
        x, y = self.ball.pos
        if x + self.ball_size > self.width:
            self.vx = -1 * self.vx 
        if x < 0:
            self.vx = -1 * self.vx 
        if y + self.ball_size > self.height:
            self.vy = -1 * self.vy
        if y < 0:
            self.vy = -1 * self.vy           
            
        self.ball.pos = (x+self.vx , y+self.vy)
        
class CanvasExample6(Widget):
    pass
        
             

        
    
    

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "rl-bt"  # left-right top-bottom options, default is "lr-tb"
        for i in range(100):
            size = dp(50+ i*10)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, dp(100)))
            self.add_widget(b)

#class GridLayoutExample(GridLayout):
 #   pass

class AnchorLayoutExample(AnchorLayout):
    pass
    
    
    
class BoxLayoutExample(BoxLayout):
    pass
'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        '''
        

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()