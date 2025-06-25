import pygame
pygame.init()
pygame.display.set_caption("FeatherFall: Siege of Avaria!")

import tools
import game_screens, game_modes

# Main loop
clock = pygame.time.Clock()
running = True
started = False
mode = None
while running:
    tools.play_background_music()
    if not started:
        running, started = game_screens.show_start_screen()
        if not running: break
    
    if mode is None:
        mode, player1_name, player2_name = game_screens.show_main_menu()
        if mode is None: break

    if mode == 'quick':
        running, mode = game_modes.quick_game(player1_name, player2_name)
        if not running: break
    
    if mode == 'basic':
        running, mode = game_modes.basic_game(player1_name, player2_name)
        if not running: break

    pygame.display.update()
    clock.tick(60)