import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import CoreLabel
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

HUMAN_SOURCES = ['./images/fellow_stance1.png', './images/fellow_stance2.png',
                 './images/fellow_stance3.png', './images/fellow_stance4.png',
                 './images/fellow_stance5.png']
HUMAN_HIT = ['./sounds/ouch1.WAV', './sounds/ouch2.WAV', './sounds/ouch3.WAV']

class Master(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.on_keyboard_closed, self)
        self.keyboard.bind(on_key_down = self.on_key_down)
        self.keyboard.bind(on_key_up = self.on_key_up)
        self.keys_pressed = set()
       
        self.sprites = []
        self.score = 0
        self.score_label = CoreLabel(text=f'score: {self.score}', font_size=20)
        self.score_label.refresh()
        
        self.register_event_type("on_next_frame")
        
        self.cannon_loaded = 0
        
        with self.canvas:
            Rectangle(source='./images/background.jpg', pos = (-300, -300), size = (3 * Window.width, 3 * Window.height))
            self.scoreboard = Rectangle(texture = self.score_label.texture, pos = (0.5 * Window.width - 0.5 * self.score_label.texture.width, Window.height - 20), size = self.score_label.texture.size)
                    
        Clock.schedule_interval(self.on_frame, 0) # 0 for every frame
        Clock.schedule_interval(self.spawn_human, 2)
        
        self.music = SoundLoader.load('./sounds/song1.mp3')
        self.music.play()
        
    def on_keyboard_closed(self):
        self.keyboard.unbind(on_key_down = self.on_key_down)
        self.keyboard.unbind(on_key_up = self.on_key_up)
        self.keyboard = None
    
    def on_key_down(self, keyboard, keycode, text, modifiers):
        self.keys_pressed.add(keycode[1])
    
    def on_key_up(self, keyboard, keycode):
        if keycode[1] in self.keys_pressed:
            self.keys_pressed.remove(keycode[1])
    
    def score_change(self, scoring):
        self.score += scoring
        self.score_label.text = f'score: {self.score}'
        self.score_label.refresh()
        self.scoreboard.texture = self.score_label.texture
        self.scoreboard.pos = (0.5 * Window.width - 0.5 * self.score_label.texture.width, Window.height - 20)
        self.scoreboard.size = self.score_label.texture.size
        
    def add_sprite(self, entity):
        self.sprites.append(entity)
        self.canvas.add(entity.drawing)
        
    def remove_sprite(self, entity):
        if entity in self.sprites:
            self.sprites.remove(entity)
            self.canvas.remove(entity.drawing)
        
    def collides(self, rect1, rect2): # collide for non-rotating rectangles
        r1x = int(rect1.pos[0])
        r1y =rect1.pos[1]
        r2x =rect2.pos[0]
        r2y =rect2.pos[1]
        r1w =rect1.size[0]
        r1h =rect1.size[1]
        r2w =rect2.size[0]
        r2h =rect2.size[1]
        
        if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
            return True
        else:
            return False
        
    def colliding(self, entity):
        result_list = []
        for current in self.sprites:
            if current is entity:
                continue
            if self.collides(current, entity):
                result_list.append(current)
        return result_list
    
    def spawn_human(self, dt):
        self.add_sprite(Human((random.randint(25, Window.width - 75), Window.height +50), random.randint(150, 250)))
    
    def on_frame(self, dt):
        self.dispatch('on_next_frame', dt)  
        if self.cannon_loaded > 0:
            self.cannon_loaded -= 1
           
    def on_next_frame(self, dt):
        pass

class Sprite():
    def __init__(self):
        self.size = (50,50)
        self.human = False
        self.player = False
        self.drawing = Rectangle(source = self.source, pos = self.pos, size = self.size)
                   
class Human(Sprite):
    def __init__(self, pos, speed=100):
        self.pos = pos
        self.speed = speed
        self.hit_sound = SoundLoader.load(HUMAN_HIT[random.randint(1, len(HUMAN_HIT)) - 1])
        self.source = HUMAN_SOURCES[random.randint(1, len(HUMAN_SOURCES)) - 1]
        controller.bind(on_next_frame = self.move)
        super().__init__()
        self.human = True
    
    def move(self, dispatcher, dt):
        newy = self.pos[1] - self.speed * dt
        self.pos = (self.pos[0], newy)
        self.drawing.pos = self.pos
        if self.pos[1] < 0 - self.size[1]:
            controller.score_change(-10)
            controller.unbind(on_next_frame = self.move)
            controller.remove_sprite(self)
        
    def die(self):
        self.hit_sound.play()
        controller.unbind(on_next_frame = self.move)
        controller.remove_sprite(self)
        controller.score_change(1)

class Cannonball(Sprite):
    def __init__(self, pos, speed=100):
        self.init_sound = SoundLoader.load('./sounds/Cannon.WAV')
        self.init_sound.play()
        self.pos = pos
        self.speed = speed
        self.source = './images/bomb.png'
        controller.bind(on_next_frame = self.fly)
        super().__init__()
        
    def fly(self, dispatcher, dt):
        newy = self.pos[1] + self.speed * dt
        self.pos = (self.pos[0], newy)
        self.drawing.pos = self.pos
        if self.pos[1] > Window.height + 10:
            controller.unbind(on_next_frame = self.fly)
            controller.remove_sprite(self)
            return
        colliding_with = controller.colliding(self)
        if colliding_with:
            for all in colliding_with:
                if all.human:
                    controller.unbind(on_next_frame = self.fly)
                    controller.remove_sprite(self)
                    all.die()      
                    
class Player(Sprite):
    def __init__(self):
        self.source ='./images/PS.png'
        self.pos = (0.5 * Window.width, 0)
        super().__init__()  
        self.player = True
        controller.bind(on_next_frame = self.interact)
        self.shooting = False
        self.movingr = False
        self.movingl = False
        self.changed = False
        
    def interact(self, dispatcher, dt):
        currentx = self.pos[0]
        currenty = self.pos[1]
        
        step_size = 300 * dt
        
        if controller.cannon_loaded < 80:
            self.shooting = False
        self.movingr = False
        self.movingl = False
        
        if 'a' in controller.keys_pressed or 'left' in controller.keys_pressed:
            currentx -= step_size
            self.movingl = True
        if 'd' in controller.keys_pressed or 'right' in controller.keys_pressed:
            currentx += step_size
            self.movingr = True
        if 'y' in controller.keys_pressed:
            controller.add_sprite(Human((random.randint(25, Window.width - 75), Window.height +50), random.randint(150, 250)))
        if 'spacebar' in controller.keys_pressed and controller.cannon_loaded == 0:
            controller.add_sprite(Cannonball((controller.player.pos[0], controller.player.pos[1] + 50 ), 250))
            controller.cannon_loaded = 100
            self.shooting = True
            
        if self.shooting:
            self.drawing.source = './images/PU.png'
        elif self.movingl:
            self.drawing.source = './images/PL.png'  
        elif self.movingr:
            self.drawing.source = './images/PR.png'  
        else:
            self.drawing.source = './images/PS.png'
        
        self.pos = (currentx, currenty)   
        
        self.drawing.pos = self.pos
        
         
        
controller = Master()
controller.player = Player()
controller.add_sprite(controller.player)
            
class Constructor_Conductor(App):
    def build(self):
        return controller
       
if __name__ == '__main__':
    app = Constructor_Conductor()
    app.run()
    
    
    
    '''
    init:
        Clock.schedule_once(self.reinstigate , 1)
    
    def reinstigate(self, dt):
        print('triggers once after one sec')
    '''
    