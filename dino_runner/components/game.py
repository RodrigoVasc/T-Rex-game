import pygame

from dino_runner.utils.constants import BG, CLOUD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

half_screen_heigth = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.scores = []
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = 35
        self.font = pygame.font.Font(FONT_STYLE, 22)
        self.score = 0
        self.death_count = 0

        
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

        self.obstacle_manager.update(self)  
        self.update_score()  
        
    def update_score(self):
        self.score += 1
    
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_scoreRank()
        self.obstacle_manager.draw(self.screen)
        self.count_morte = self.font.render(f'Death: {self.death_count}',True, (0,0,0))

        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        self.textScore = self.font.render(f"Score: {self.score}", True, (0,0,0))
        textScore_rect = self.textScore.get_rect()
        textScore_rect.center = (950, 50)
        self.screen.blit(self.textScore, textScore_rect)

    def draw_scoreRank(self):
        self.scores.append(self.score)
        self.textMax = self.font.render(f"Max score: {max(self.scores)}", True, (0,0,0))
        textMax_rect = self.textMax.get_rect()
        textMax_rect.center = (750, 50)
        self.screen.blit(self.textMax, textMax_rect)
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def render_text(self, message, x, y, font):
        text = font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255,255,255))

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        font = pygame.font.Font(FONT_STYLE, 22)

        if self.death_count == 0:
            self.render_text("Press (S) to start playing", half_screen_width, half_screen_height, font)
        else:
            self.render_text("Press (C) to continue playing", half_screen_width, half_screen_height + 25, font)
            self.screen.blit(self.textScore, (100, 50))
            self.screen.blit(self.count_morte, (100, 80))
            self.render_text("Press (S) to new playing", half_screen_width, half_screen_height - 25, font)

        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c] and self.death_count >= 1:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_s] and self.death_count >= 1:
                    self.death_count = 0
                    self.game_speed = 20
                    self.score = 0
                    self.run()