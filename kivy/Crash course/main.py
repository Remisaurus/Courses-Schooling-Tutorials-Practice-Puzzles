from kivy.app import App
from kivy import platform
from kivy.core.audio import SoundLoader
from kivy.lang.builder import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Quad, Triangle
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, Clock
from kivy.core.window import Window
from random import randint

Builder.load_file('menu.kv')

class MainWidget(RelativeLayout):
    from transform import transform, transform_2D, transform_perspective
    from user_actions import on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up, keyboard_closed
    
    menu_widget = ObjectProperty()
    
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    perspective_mode = '3d' # '2d' or '3d'
    
    number_vertical_lines = 8 # even number for balance.
    spacing_vertical_lines = 0.25 # *100 = percentage screen width
    vertical_lines = []
    current_offset_x = 0
    
    speed_x = 9
    current_speed_x = 0
    
    number_horizontal_lines = 12
    spacing_horizontal_lines = 0.1 # *100 = percentage screen heigth
    horizontal_lines = []
    current_offset_y = 0
    current_y_loop = 0
    progress_counter = 0
    
    speed = 5
    
    number_tiles = 16
    tiles = []
    tiles_coordinates = []
    
    ship = None
    ship_width = 0.08
    ship_height = 0.035
    ship_base_y = 0.04
    ship_coordinates = [(0,0), (0,0), (0,0)]
    
    menu_title = StringProperty("c  r  a  s  h     c  o  u  r  s  e")
    menu_button_title = StringProperty("start")
    score_txt = StringProperty()
    
    game_over = False
    game_started = False
    
    sound_begin = None
    sound_galaxy = None
    sound_gameover_impact = None
    sound_gameover_voice = None
    sound_music1 = None
    sound_restart = None
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_sound()
        self.init_vertical_lines()
        self.init_horizontal_lines()
        self.init_tiles()
        self.init_ship()
        self.pre_fill_tile_coordinates()
        self.generate_tile_coordinates()
        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_keyboard_down)
            self.keyboard.bind(on_key_up=self.on_keyboard_up)
        self.sound_galaxy.play()
        Clock.schedule_interval(self.update, 1/60)
        
    def init_sound(self):
        self.sound_begin = SoundLoader.load("audio/begin.wav")
        self.sound_galaxy = SoundLoader.load("audio/startup.mp3")
        self.sound_gameover_impact = SoundLoader.load("audio/gameover_impact.wav")
        self.sound_gameover_voice = SoundLoader.load("audio/gameover_voice.wav")
        self.sound_music1 = SoundLoader.load("audio/music1.wav")
        self.sound_restart = SoundLoader.load("audio/restart.wav")
        
        self.sound_begin.volume = .25
        self.sound_galaxy.volume = .25
        self.sound_gameover_impact.volume = .6
        self.sound_gameover_voice.volume = .25
        self.sound_music1.volume = 1
        self.sound_restart.volume = .25


    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        else:
            return False
    
    def on_size(self, *args):
        self.perspective_point_x = int(0.5 * self.width)
        self.perspective_point_y = int(0.75 * self.height)
        
    def init_ship(self):
          with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle()
            
    def update_ship(self):
        self.ship_coordinates[0] = (self.perspective_point_x - 0.5 * self.ship_width * self.width, self.ship_base_y * self.height)
        self.ship_coordinates[1] = (self.perspective_point_x, self.ship_base_y * self.height + self.ship_height * self.height)
        self.ship_coordinates[2] = (self.perspective_point_x + 0.5 * self.ship_width * self.width, self.ship_base_y * self.height)
        
        x1, y1 = self.transform(*self.ship_coordinates[0])
        x2, y2 = self.transform(*self.ship_coordinates[1])
        x3, y3 = self.transform(*self.ship_coordinates[2])
        
        self.ship.points = [x1, y1, x2, y2, x3, y3]
        
    def check_collission(self):
        for i in range(0, len(self.tiles_coordinates)):
            tile_x, tile_y = self.tiles_coordinates[i]
            if tile_y > self.current_y_loop + 1:
                return False
            if self.check_collission_tile(tile_x, tile_y):
                return True
        return False
        
    def check_collission_tile(self, tile_x, tile_y):
        xmin, ymin = self.get_tile_coordinates(tile_x, tile_y)
        xmax, ymax = self.get_tile_coordinates(tile_x + 1, tile_y + 1)
        for i in range (0, len(self.ship_coordinates)):
            px, py = self.ship_coordinates[i]
            if xmin <= px <= xmax and ymin <= py <= ymax:
                return True
        return False
        
    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.number_tiles):
                self.tiles.append(Quad())
        
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.number_vertical_lines):
                self.vertical_lines.append(Line())
                
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.number_horizontal_lines):
                self.horizontal_lines.append(Line()) 
    
    def pre_fill_tile_coordinates(self):
        for i in range(0,11):
            self.tiles_coordinates.append((0, i))  
    
    def generate_tile_coordinates(self):
        next_y = 0
        last_x = 0
        start_index = -int(self.number_vertical_lines / 2) + 1
        end_index = start_index + self.number_vertical_lines - 1
        for i in range(len(self.tiles_coordinates) - 1, -1, -1):
            if self.tiles_coordinates[i][1] < self.current_y_loop:
                del self.tiles_coordinates[i]
                
        if len(self.tiles_coordinates) > 0:
            last_coordinates = self.tiles_coordinates[-1]
            next_y = last_coordinates[1] + 1
            last_x = last_coordinates[0]
                
        for i in range(len(self.tiles_coordinates), self.number_tiles):
            r = randint(0, 2)
            self.tiles_coordinates.append((last_x, next_y))
            if r == 1 and last_x >= end_index - 1:
                r = 2
            if r == 2 and last_x <= start_index:
                r = 1
            if r == 1:
                last_x += 1
                self.tiles_coordinates.append((last_x, next_y))
                next_y += 1
                self.tiles_coordinates.append((last_x, next_y))
            if r == 2:
                last_x -= 1
                self.tiles_coordinates.append((last_x, next_y))
                next_y += 1
                self.tiles_coordinates.append((last_x, next_y))
            next_y += 1
              
    def update_vertical_lines(self):
        start_index = -int(self.number_vertical_lines / 2) + 1
        for i in range(start_index, start_index + self.number_vertical_lines):
            line_x = self.get_line_x_from_index(i)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
        
    def get_line_x_from_index(self, index):
        spacing = self.spacing_vertical_lines * self.width
        line_number = index - 0.5
        line_x = self.perspective_point_x + line_number * spacing - self.current_offset_x
        return int(line_x)
    
    def get_line_y_from_index(self, index):
        spacing_y = self.spacing_horizontal_lines * self.height
        line_y = index * spacing_y - self.current_offset_y
        return line_y
            
    def update_horizontal_lines(self):
        start_index = -int(self.number_vertical_lines / 2) + 1
        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(start_index + self.number_vertical_lines - 1)
        for i in range(0, self.number_horizontal_lines):
            line_y = self.get_line_y_from_index(i)
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]
            
    def get_tile_coordinates(self, tile_x, tile_y):
        tile_y = tile_y - self.current_y_loop
        x = self.get_line_x_from_index(tile_x)
        y = self.get_line_y_from_index(tile_y)
        return x, y
    
    def update_tiles(self):
        for i in range(0, self.number_tiles):
            tile_coordinates = self.tiles_coordinates[i]
            
            xmin, ymin = self.get_tile_coordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.get_tile_coordinates(tile_coordinates[0] + 1, tile_coordinates[1] + 1)
            x1, y1 = self.transform(xmin, ymin)
            x2, y2 = self.transform(xmin, ymax)
            x3, y3 = self.transform(xmax, ymax)
            x4, y4 = self.transform(xmax, ymin)
            self.tiles[i].points = (x1, y1, x2, y2, x3, y3, x4, y4)
    
    def update(self, dt):
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        self.update_ship()
        
        if not self.game_over and self.game_started:
            speed_y = self.speed / 1000 * self.height
            speed_x = self.current_speed_x / 1000 * self.width
            self.current_offset_y += speed_y * time_factor
            self.current_offset_x += speed_x * time_factor
            spacing_y = self.spacing_horizontal_lines * self.height
            if self.progress_counter > 10:
                self.progress_counter -= 10
                self.speed += 0.1
            while self.current_offset_y >= spacing_y:
                self.current_offset_y -= spacing_y 
                self.current_y_loop += 1
                self.progress_counter += 1
                self.score_txt = f'not yet crashed scoring: {self.current_y_loop}'
                self.generate_tile_coordinates()
            if not self.check_collission():
                self.sound_gameover_impact.play()
                self.sound_music1.stop()
                self.game_over = True
                self.menu_title = "c r a s h e d   w e l l"
                self.menu_button_title = "crash again"
                self.menu_widget.opacity = 1
                Clock.schedule_once(self.delay_gameover_sound, 2)
                
    def delay_gameover_sound(self, dt):
        if self.game_over:
            self.sound_gameover_voice.play()
                
                
    def on_menu_button_pressed(self):
        self.menu_widget.opacity = 0
        self.sound_galaxy.stop()
        if self.game_over:
            self.sound_restart.play()
        else:
            self.sound_begin.play()
        self.sound_music1.play()
        self.reset_game()
        
    def reset_game(self):
        self.current_offset_x = 0
        self.current_speed_x = 0
        self.current_offset_y = 0
        self.current_y_loop = 0
        self.score_txt = f'not yet crashed scoring: {self.current_y_loop}'
        self.tiles_coordinates = []
        self.pre_fill_tile_coordinates()
        self.generate_tile_coordinates()
        
        
        
        self.game_started = True        
        self.game_over = False
        

class GalaxyApp(App):
    pass

GalaxyApp().run()