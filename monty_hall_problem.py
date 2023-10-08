import pygame
import sys
from time import sleep
from monty_hall_button import Button
from random import randint


class MontyHall:
    """A class to manage the Monty Hall Problem"""
    def __init__(self):
        """Initialize assets"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.bg_color = (30, 30, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 96)
        self.wins = 0
        self.losses = 0
        self._reset_assets()
        pygame.display.set_caption("Monty Hall")

        self._create_buttons()

    def run_game(self):
        """Runs the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Responds to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.clicked_first:
                    self._check_button1(mouse_pos)
                else:
                    self._check_button2(mouse_pos)

    def _check_button1(self, mouse_pos):
        """Answers when the first button is pressed"""
        for i in range(3):
            button_clicked = self.buttons[i].rect.collidepoint(mouse_pos)
            if button_clicked:
                self.buttons[i].button_clicked(-1)
                self.clicked_first = i+1
                self._update_screen()
                self._choose_wrong_button()

    def _check_button2(self, mouse_pos):
        """Answers the final decision of the game"""
        for i in range(3):
            button_clicked = self.buttons[i].rect.collidepoint(mouse_pos)
            if button_clicked and self.chose_wrong != i+1:
                self.buttons[self.clicked_first - 1].reset_color()
                self.buttons[i].button_clicked(self.winning_button == i+1)
                if self.winning_button == i+1:
                    self.wins += 1
                    self.text = "You won!"
                else:
                    self.losses += 1
                    self.text = "You lost!"
                self._update_screen()
                sleep(0.5)
                self._reset_assets()
                self._create_buttons()

    def _choose_wrong_button(self):
        """Purposely chooses a wrong button and allows the player to choose again"""
        random_button = randint(1, 3)
        while random_button == self.winning_button or random_button == self.clicked_first:
            random_button = randint(1, 3)
        sleep(0.5)
        self.text = f"I can assure you that button {random_button} is wrong! You may choose again."
        self._update_screen()
        self.buttons[random_button-1].button_clicked(0)
        self.chose_wrong = random_button

    def _create_buttons(self):
        """Creates the 3 main buttons"""
        self.buttons.append(Button(self, "1", self.screen_width / 4))
        self.buttons.append(Button(self, "2", self.screen_width / 4 * 2))
        self.buttons.append(Button(self, "3", self.screen_width / 4 * 3))

    def _reset_assets(self):
        """Resets the variables that need to be reset"""
        self.clicked_first = 0
        self.chose_wrong = 0
        self.buttons = []
        self.winning_button = randint(1, 3)
        self.text = "Only one out of the following 3 choices is correct. Choose one!"

    def _update_text(self):
        """
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        """
        title_image = self.font.render("Monty Hall Problem", True, self.text_color)
        title_image_rect = title_image.get_rect()
        title_image_rect.midtop = self.screen_rect.midtop
        title_image_rect.y += 10
        self.screen.blit(title_image, title_image_rect)

        win_loss_str = f"Wins: {self.wins}    Losses: {self.losses}"
        win_loss_img = self.font.render(win_loss_str, True, self.text_color)
        win_loss_img_rect = win_loss_img.get_rect()
        win_loss_img_rect.midbottom = self.screen_rect.midbottom
        win_loss_img_rect.y -= 10
        self.screen.blit(win_loss_img, win_loss_img_rect)

        try:
            win_percentage = self.wins / (self.wins + self.losses) * 100
        except ZeroDivisionError:
            win_percentage = 0
        win_percentage_str = "{0:.2f}".format(win_percentage) + "%"
        win_percentage_img = self.font.render(win_percentage_str, True, self.text_color)
        win_percentage_img_rect = win_percentage_img.get_rect()
        win_percentage_img_rect.midbottom = win_loss_img_rect.midbottom
        win_percentage_img_rect.y -= 100
        self.screen.blit(win_percentage_img, win_percentage_img_rect)

        text_img = self.font.render(self.text, True, self.text_color)
        text_img_rect = text_img.get_rect()
        text_img_rect.center = self.screen_rect.center
        text_img_rect.y -= self.buttons[0].rect.y - 200
        self.screen.blit(text_img, text_img_rect)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.bg_color)
        for i in range(3):
            self.buttons[i].draw_button()
        self._update_text()
        pygame.display.flip()


if __name__ == "__main__":
    game = MontyHall()
    game.run_game()
