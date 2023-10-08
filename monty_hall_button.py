import pygame.font


class Button:
    """A class to manage the buttons/doors in the monty hall problem"""
    def __init__(self, game, msg, x_coords):
        """Initialize assets"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 400, 400)
        self.button_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 256)
        self.text_color = (255, 255, 255)

        self.rect.center = self.screen_rect.center
        self.rect.centerx = x_coords

        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def button_clicked(self, winner):
        """Updates a button when it is clicked"""
        # self.msg_image = self.font.render("", False, self.text_color)
        if winner == 1:
            self.button_color = (0, 255, 0)
        elif winner == 0:
            self.button_color = (255, 0, 0)
        else:
            self.button_color = (255, 165, 0)

    def reset_color(self):
        self.button_color = (100, 100, 100)

    def draw_button(self):
        """Draws the button to the screen"""
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
