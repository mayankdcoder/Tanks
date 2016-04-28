import pygame


__author__ = 'capt_MAKO'
__since__ = '30/December/2015 20:26:00'
__version__ = '1.0'


class Game:
    display_width = int()
    display_height = int()
    game_title = str()
    game_display = object()
    game_clock = object()
    constant_object = object()
    cursor_object = object()

    def __init__(self, constants):
        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.game_title = 'Tanks'
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption(self.game_title)
        self.game_clock = pygame.time.Clock()
        self.constant_object = constants
        self.cursor_object = pygame.mouse.get_pos()

    def text_objects(self, text, color, size='small'):
        if size == 'small':
            text_surface = self.constant_object.small_fonts.render(text, True, color)
        elif size == 'medium':
            text_surface = self.constant_object.medium_fonts.render(text, True, color)
        else:
            text_surface = self.constant_object.large_fonts.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, message, color, y_displacement=0, size='small'):
        text_surface, text_rectangle = self.text_objects(message, color, size)
        text_rectangle.center = (int(self.display_width / 2), int(self.display_height / 2) + y_displacement)
        self.game_display.blit(text_surface, text_rectangle)

    def make_button(self, parent, text, text_color, button_color_inactive, button_color_active, pos, size='small'):
        pygame.draw.rect(parent, button_color_inactive, pos)
        text_surface, text_rectangle = self.text_objects(text, text_color, size)
        text_rectangle.center = ((pos[0] + (pos[2] / 2)), (pos[1] + (pos[3] / 2)))
        self.game_display.blit(text_surface, text_rectangle)

    def pause(self):
        game_paused = True
        self.message_to_screen('Paused', self.constant_object.black, - 100, size='large')
        self.message_to_screen('Press C to continue playing or Q to quit', self.constant_object.black, 25)
        pygame.display.update()
        while game_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        self.game_clock.tick(5)

    def intro(self):
        game_intro = True
        while game_intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_intro = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.game_display.fill(self.constant_object.white)
            self.message_to_screen('Welcome to Tanks!!', self.constant_object.green, - 100, size='large')
            self.message_to_screen('The objective is to shoot and destroy', self.constant_object.black, - 30)
            self.message_to_screen('before they destroy you.', self.constant_object.black, 10)
            self.message_to_screen('The more enemies you destroy, the harder they get.', self.constant_object.black, 50)
            # pygame.draw.rect(self.game_display, self.constant_object.green, (150, 500, 100, 50))
            # pygame.draw.rect(self.game_display, self.constant_object.yellow, (350, 500, 100, 50))
            pygame.display.update()
            self.game_clock.tick(15)

    def main_loop(self):
        game_exit = False
        game_over = False
        fps = 15
        while not game_exit:
            if game_over:
                self.message_to_screen('Game Over!', self.constant_object.red, - 50, size='large')
                self.message_to_screen('Press C to play again or Q to quit', self.constant_object.black, 50)
                pygame.display.update()
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_exit = True
                            game_over = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_c:
                                self.main_loop()
                            elif event.key == pygame.K_q:
                                game_exit = True
                                game_over = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_UP:
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass
                    elif event.key == pygame.K_p:
                        self.pause()
            self.game_display.fill(self.constant_object.white)
            pygame.display.update()
            self.game_clock.tick(fps)
        pygame.quit()
        quit()
