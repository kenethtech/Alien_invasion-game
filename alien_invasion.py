
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # making a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets
    bullets = Group()


    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Remove the bullets that have disappeared from the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()