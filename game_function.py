import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # responds to key presses
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # move the ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # stop moving the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # stop moving the ship to the left
        ship.moving_left = False


def check_event(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets from ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    pygame.display.flip()
