#####
# Fantasy Card Game
# Written by Luigi (Phobos70)
# AkamiLab
#
# DE - main module
#####
import pygame
import config
import colors

class Game:
    def __init__(self):
        self.state = config.SPLASH_SCREEN
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.update()
            

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if self.state == config.GAME_PLAY:
                        self.state = config.PAUSE
                    elif self.state == config.PAUSE:
                        self.state = config.GAME_PLAY

    def update(self):
        if self.state == config.SPLASH_SCREEN:
            self.update_splash_screen()
        elif self.state == config.TITLE_SCREEN:
            self.update_title_screen()
        elif self.state == config.GAME_PLAY:
            self.update_game_play()
        elif self.state == config.OPTIONS:
            self.update_options()
        elif self.state == config.PAUSE:
            self.update_pause()

    def draw(self):
        if self.state == config.SPLASH_SCREEN:
            self.draw_splash_screen()
        elif self.state == config.TITLE_SCREEN:
            self.draw_title_screen()
        elif self.state == config.GAME_PLAY:
            self.draw_game_play()
        elif self.state == config.OPTIONS:
            self.draw_options()
        elif self.state == config.PAUSE:
            self.draw_pause()
        pygame.display.flip()

    def update_splash_screen(self):
        # Logica di aggiornamento per lo splash screen
        pygame.time.wait(3000)  # Mostra lo splash screen per 3 secondi
        #self.state = config.TITLE_SCREEN
        self.state = config.GAME_PLAY

    def update_title_screen(self):
        # Logica di aggiornamento per il titolo
        pass

    def update_game_play(self):
        # Logica di aggiornamento per il gioco
        pass

    def update_options(self):
        # Logica di aggiornamento per le opzioni
        pass

    def update_pause(self):
        # Logica di aggiornamento per la pausa
        pass

    def draw_splash_screen(self):
        # Disegna lo splash screen
        self.screen.fill(colors.ORANGE)
        font = pygame.font.Font(None, 74)
        text = font.render("Splash Screen", True, (255, 255, 255))
        self.screen.blit(text, (250, 250))

    def draw_title_screen(self):
        # Disegna il titolo
        self.screen.fill(colors.BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Title Screen", True, (255, 255, 255))
        self.screen.blit(text, (250, 250))

    def draw_game_play(self):
        # Disegna il gioco
        self.screen.fill(colors.ORANGE)
        font = pygame.font.Font(None, 74)
        text = font.render("Game Play", True, (255, 255, 255))
        self.screen.blit(text, (250, 250))

    def draw_options(self):
        # Disegna le opzioni
        font = pygame.font.Font(None, 74)
        text = font.render("Options", True, (255, 255, 255))
        self.screen.blit(text, (250, 250))

    def draw_pause(self):
        # Disegna la pausa
        font = pygame.font.Font(None, 74)
        text = font.render("Pause", True, (255, 255, 255))
        self.screen.blit(text, (250, 250))

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
