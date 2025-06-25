import pygame

# Loading fonts
button_font = pygame.font.Font("media/Fragile Bombers.otf", 48)
title_font = pygame.font.Font("media/Audiowide-Regular.ttf", 60)
textbox_font = pygame.font.Font("media/Audiowide-Regular.ttf", 30)

# Loading images
screen=pygame.display.set_mode((900,600))
start_screen=pygame.transform.scale(pygame.image.load("media/start_screen.png"), (900,600))
bgimg=pygame.transform.scale(pygame.image.load("media/background.png"), (900,600))
game_bgimg=pygame.transform.scale(pygame.image.load("media/game_background.png"), (900,600))
title=pygame.transform.scale(pygame.image.load("media/title.png"), (341, 183))
left_ss=pygame.transform.scale(pygame.image.load("media/leftslingshot.png"), (80,80))
right_ss=pygame.transform.scale(pygame.image.load("media/rightslingshot.png"), (80,80))
alien_bird=pygame.transform.scale(pygame.image.load("media/alien.png"), (48,48))

block_images = {
    "ice": [pygame.transform.scale(pygame.image.load(f"media/ice_{i}.png"), (48, 48)) for i in range(4)],
    "wood": [pygame.transform.scale(pygame.image.load(f"media/wood_{i}.png"), (48, 48)) for i in range(4)],
    "stone": [pygame.transform.scale(pygame.image.load(f"media/stone_{i}.png"), (48, 48)) for i in range(4)]
}

bird_images = {
    "red": pygame.transform.scale(pygame.image.load("media/Red.png"), (32, 32)),
    "chuck": pygame.transform.scale(pygame.image.load("media/Chuck.png"), (32, 32)),
    "blue": pygame.transform.scale(pygame.image.load("media/Blue.png"), (32, 32)),
    "bomb": pygame.transform.scale(pygame.image.load("media/Bomb.png"), (32, 32))
}

# Powerup icons
full_path = pygame.transform.scale(pygame.image.load("media/full_path.png"), (48,48))
double_dmg = pygame.transform.scale(pygame.image.load("media/double_dmg.png"), (48,48))
