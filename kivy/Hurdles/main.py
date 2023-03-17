from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty, NumericProperty

from random import randint

from hurdle import Hurdle

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
        self.cloud_texture.uvpos = ( (self.cloud_texture.uvpos[0] + dt/25) % Window.width , self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ( (self.floor_texture.uvpos[0] + dt/50) % Window.width , self.floor_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)
        texture2 = self.property('floor_texture')
        texture2.dispatch(self)

class Bird(Image):
    velocity = NumericProperty(0)
    walking_image = ['een.png', 'twee.png']
    current_walking_index = 0
    touching = False
    
    def on_touch_down(self, touch):
        if self.y < 80:
            self.source = 'naaromhoog.png'
            self.velocity = 150
            self.touching = True
        super().on_touch_down(touch)
        
    def on_touch_up(self, touch):
        if self.y > 90:
            self.source = 'boven.png'
        self.touching = False
        super().on_touch_up(touch)
  
class Mainapp(App):
    hurdles = []
    num_hurdles = 2
    GRAVITY = 150
    distance_between_hurdles = Window.width / (num_hurdles -1)
    is_colliding = False
    was_colliding = False
    music = SoundLoader.load('song1.mp3')
    crash = SoundLoader.load('gameover_impact.WAV')
    score = 0
    
    def move_bird(self, dt):
        bird = self.root.ids.bird
        bird.current_walking_index += 0.2
        if int(bird.current_walking_index) == 2:
            bird.current_walking_index = 0  
        bird.y = bird.y + bird.velocity * dt
        if not bird.touching:
            if bird.y > 75:
                bird.velocity = bird.velocity - self.GRAVITY * dt
                if bird.velocity < 0:
                    bird.source = 'naarbenee.png'
            else:
                bird.velocity = 0
                bird.source = bird.walking_image[int(bird.current_walking_index)]
                
        self.check_collision()
        
    def check_collision(self):
        bird = self.root.ids.bird
        
        for hurdle in self.hurdles:
            if hurdle.collide_widget(bird): #COLLIDE WIDGET
                self.is_colliding = True
                if bird.y < hurdle.hurdle_center - hurdle.GAP_SIZE / 2:
                    self.game_over()
        if bird.top > Window.height:
            self.game_over()
            
        if self.was_colliding and not self.is_colliding:
            self.score += 1
            self.root.ids.score.text = f'score: {self.score}'
        self.was_colliding = self.is_colliding
        self.is_colliding = False
                    
    def game_over(self):
        self.music.stop()
        self.crash.play()
        bird = self.root.ids.bird
        bird.pos = (33,  85)
        bird.source = bird.walking_image[int(bird.current_walking_index)]
        for hurdle in self.hurdles:
            self.root.remove_widget(hurdle)
        self.run.cancel()
        bird.velocity = 0
        self.root.ids.start_button.disabled = False
        self.root.ids.start_button.opacity = 1
                
    def next_frame(self, dt):
        self.move_bird(dt)
        self.move_hurdles(dt)
        self.root.ids.background.scroll_textures(dt)
                
    def start_game(self):
        self.music.play()
        self.hurdles = []
        self.score = 0
        self.root.ids.score.text = f'score: {self.score}'
        self.is_colliding = False
        self.was_colliding = False
        
        self.run = Clock.schedule_interval(self.next_frame, 1/60)
        for i in range(self.num_hurdles):
            hurdle = Hurdle()
            hurdle.hurdle_center = randint(119, self.root.height - 0.35 * self.root.height)
            hurdle.size_hint = (None, None)
            hurdle.pos = (Window.width + i * self.distance_between_hurdles , 75)
            hurdle.size = (70, self.root.height - 75)
            
            self.hurdles.append(hurdle)
            self.root.add_widget(hurdle)
        
    def move_hurdles(self, dt):
        for hurdle in self.hurdles:
            hurdle.x -= dt * 200
         
        hurdles_xs = list(map(lambda hurdle: hurdle.x, self.hurdles))
        right_most_x = max(hurdles_xs)
        if right_most_x <= Window.width - self.distance_between_hurdles:
            left_most_hurdle = self.hurdles[hurdles_xs.index(min(hurdles_xs))]
            left_most_hurdle.hurdle_center = randint(119, self.root.height - 0.35 * self.root.height)
            left_most_hurdle.x = Window.width
        
        
            
        
Mainapp().run()