from kivy.config import Config

# don't make the app re-sizeable
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import partial
from kivy.graphics.context_instructions import PopMatrix, PushMatrix, Rotate

from random import randint


class WidgetDrawer(Widget):
    # This widget is used to draw all of the objects on the screen
    # it handles the following:
    # widget movement, size, positioning
    # whever a WidgetDrawer object is created, an image string needs to be
    # specified, along with the windowsize tuple
    # example:    wid - WidgetDrawer('./image.png', (Window.height, Window.width))
    # windowsize is used for the default size and position,
    # but can pe updated later

    def __init__(self, imageStr, windowsize, **kwargs):
        super(WidgetDrawer, self).__init__(**kwargs)
        # this is part of the**kwargs notation
        # if you haven't seen with before, here's a link
        # http://effbot.org/zone/python-with-statement.html
        self.WindowHeigth, self.WindowWidth = windowsize

        with self.canvas:
            PushMatrix()

            # setup a default size for the object
            self.size = (self.WindowWidth*.002*25, self.WindowWidth*.002*25)
            # center the widget
            self.pos = (self.center_x, self.center_y)
            self.rot = Rotate()
            self.rot.origin = self.pos
            self.rot.axis = (0, 0, 1)
            self.rot.angle = 30
            # this line creates a rectangle with the image drawn on top
            self.rect_bg = Rectangle(source=imageStr,
                                     pos=self.pos,
                                     size=self.size)
            PopMatrix()
            # this line calls the update_graphics_pos function every time the
            # position variable is modified
            self.bind(pos=self.update_graphics_pos)

            self.velocity_x = 0  # initialize velocity_x and velocity_y
            self.velocity_y = 0

    def update_graphics_pos(self, instance, value):
        # if the widgets position moves, the rectangle that contains the image
        # is also moved
        self.rect_bg.pos = value

    # use this function to change widget position
    def setPos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

        if self.y > self.WindowHeigth*0.95:
            # don't let the ship go up too high
            self.y = self.WindowHeigth*0.95
        if self.y <= 0:
            self.y = 0  # set heigth to 0 if ship too low
        
    def rotate(self):
        self.rot.origin = self.center
        self.rot.angle += self.delta_angle

    def update(self):
        # the update function moves the astreoid. Other things could happen
        # here as well (speed changes for example)
        self.move()
        self.rotate()


class Asteroid(WidgetDrawer):
    # Asteroid class. The flappy ship will dodge these
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delta_angle = randint(-3, 3)

    def update(self):
        # self.rot.angle += 1  # this should animate the object, but rotates the layout
        super().update()


class Game(Widget):
    # this is the main widget that contains the game.
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.windowsize = (Window.height, Window.width)
        self.asteroidList = []  # use this to keep track of asteroids
        self.minProb = 1700  # this variable used in spawning asteroids

    def addAsteroid(self):
        # add an asteroid to the screen
        # self.asteroid
        imageNumber = randint(1, 4)
        imageStr = './sandstone_'+str(imageNumber)+'.png'  #change the image here
        tmpAsteroid = Asteroid(imageStr, self.windowsize)
        tmpAsteroid.x = Window.width*0.99

        # randomize y position
        ypos = randint(0, 16)

        ypos = ypos*Window.height*.0625

        tmpAsteroid.y = ypos
        tmpAsteroid.velocity_y = 0
        vel = 10
        tmpAsteroid.velocity_x = -0.1*vel

        self.asteroidList.append(tmpAsteroid)
        self.add_widget(tmpAsteroid)

    def update(self, dt):
        # This update function is the main update function for the game
        # All of the game logic has its origin here
        # events are setup here as well

        # update game objects

        # update asteroids
        # randomly add an asteroid
        tmpCount = randint(1, 1800)
        if tmpCount > self.minProb:
            self.addAsteroid()
        if self.minProb < 1700:
            self.minProb = 1900
        self.minProb = self.minProb - 1

        for k in self.asteroidList:
            if k.x < -20:
                self.remove_widget(k)
                self.asteroidList.remove(k)

            k.update()


class ClientApp(App):
    def build(self):
        # this is where the root widget goes
        # should be a canvas
        parent = Widget()  # this is an empty holder for buttons, etc
        Window.clearcolor = (0, 0, 0, 1.)

        game = Game()
        # Start the game clock (runs update function once every (1/60) seconds
        # Clock.schedule_interval(app.update, 1.0/60.0)
        parent.add_widget(game)
        Clock.schedule_interval(game.update, 1.0/60.0)
        # use this hierarchy to make it easy to deal w/buttons
        return parent


if __name__ == '__main__':
    ClientApp().run()
