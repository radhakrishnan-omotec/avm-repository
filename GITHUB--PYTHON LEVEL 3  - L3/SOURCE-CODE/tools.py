import pygame
import random, math
import assets
import classes

def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load("media/background_music.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)

def draw_scores(screen, player1_name, player1_score, player2_name, player2_score):
    p1_surf = assets.textbox_font.render(f"{player1_name}: {player1_score}", True, (255, 255, 255))
    p2_surf = assets.textbox_font.render(f"{player2_name}: {player2_score}", True, (255, 255, 255))
    screen.blit(p1_surf, (20, 20))
    screen.blit(p2_surf, (880 - p2_surf.get_width(), 20))

def draw_scene():
    assets.screen.blit(assets.game_bgimg, (0, 0))
    assets.screen.blit(assets.title, (280, 0))
    assets.screen.blit(assets.left_ss, (250, 420))
    assets.screen.blit(assets.right_ss, (586, 420))

def generate_structure(): # Create grid structure for both players
    block_types = ["ice"]*5 + ["stone"]*5 + ["wood"]*5 + [None]
    random.shuffle(block_types)
    
    grid = []
    for i in range(4):
        row = []
        for j in range(4):
            b_type = block_types[i*4 + j]
            if b_type:
                row.append(classes.Block(b_type))
            else:
                row.append(None)
        grid.append(row)
    return grid

def draw_structure(grid, start_x, start_y):
    for i in range(4):
        for j in range(4):
            b = grid[i][j]
            if b and b.image:
                assets.screen.blit(b.image, (start_x + j*48, start_y + i*48))

def get_damage(bird_type, block_type):
    damage_map = {
        "red": {"ice": 2, "wood": 2, "stone": 2},
        "chuck": {"ice": 1, "wood": 3, "stone": 1},
        "blue": {"ice": 3, "wood": 1, "stone": 1},
        "bomb": {"ice": 1, "wood": 1, "stone": 3}
    }
    return damage_map[bird_type][block_type]

# 12 birds per player, randomly generated
player1_bird_queue = ["red", "chuck", "blue", "bomb"]
player2_bird_queue = ["red", "chuck", "blue", "bomb"]
random.shuffle(player1_bird_queue)
random.shuffle(player2_bird_queue)

def get_next_bird(player):
    global player1_bird_queue, player2_bird_queue
    if player == 1:
        if len(player1_bird_queue) == 0:
            player1_bird_queue += ["red", "chuck", "blue", "bomb"]
            random.shuffle(player1_bird_queue)
        return player1_bird_queue.pop(0)
    else:
        if len(player2_bird_queue) == 0:
            player2_bird_queue += ["red", "chuck", "blue", "bomb"]
            random.shuffle(player2_bird_queue)
        return player2_bird_queue.pop(0)

def draw_next_birds(player):
    bird_queue = player1_bird_queue if player == 1 else player2_bird_queue
    for i, bird in enumerate(bird_queue[:3]):
        bird_img = assets.bird_images[bird]
        if player == 1:
            assets.screen.blit(bird_img, (30 + i * 50, 550))
        else:
            bird_img = pygame.transform.flip(bird_img, True, False)
            assets.screen.blit(bird_img, (838 - i * 50, 550))

def draw_trajectory(current_bird, current_player, full_trajectory_enabled=False):
    mx, my = pygame.mouse.get_pos()
    start_x, start_y = (280, 430) if current_player == 1 else (636, 430)
    dx = mx - start_x
    dy = my - start_y
    distance = math.hypot(dx, dy)
    max_distance = 150
    if distance > max_distance:
        scale = max_distance / distance
        dx *= scale
        dy *= scale
    vx = -dx * 0.2
    vy = -dy * 0.2
    trajectory = current_bird.simulate(vx, vy, steps = 25 if full_trajectory_enabled else 8)
       
    pygame.draw.line(assets.screen, (255, 255, 255), (start_x, start_y), (start_x+dx, start_y+dy), 2)
    for i, point in enumerate(trajectory):
        pygame.draw.circle(assets.screen, (255, 255, 255, max((255-30*i),0)), (int(point[0]), int(point[1])), (4-i//6))

def handle_bird_launch(bird):
    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - bird.x, my - bird.y
    distance = math.hypot(dx, dy)
    max_distance = 150
    if distance > max_distance:
        scale = max_distance / distance
        dx *= scale
        dy *= scale
    vx_launch = -dx * 0.2
    vy_launch = -dy * 0.2
    bird.path = bird.simulate(vx_launch, vy_launch, steps=200)
    bird.vx, bird.vy = vx_launch, vy_launch
    bird.launched = True
    bird.step = 0

def check_alien_collisions(bird, aliens):
    bird_rect = pygame.Rect(bird.x - 16, bird.y - 16, 32, 32)
    for alien in aliens:
        alien_rect = pygame.Rect(alien.x - 24, alien.y - 24, 48, 48)
        if alien.active and bird_rect.colliderect(alien_rect):
            alien.hit()
            return 5 # Score of 5 on hitting an alien
    return 0

def falling_blocks(grid):
    for j in range(4):
        for i in range(3, -1, -1):
            if grid[i][j] is None and i > 0:
                for k in range(i-1, -1, -1):
                    if grid[k][j] is not None:
                        grid[i][j] = grid[k][j]
                        grid[k][j] = None
                        break

def check_block_collisions(bird, grid, grid_x, grid_y, double_damage_enabled=False):
    bird_rect = pygame.Rect(bird.x - 16, bird.y - 16, 32, 32)
    for i in range(4):
        for j in range(4):
            block = grid[i][j]
            if block and block.health > 0:
                block_rect = pygame.Rect(grid_x + j*48, grid_y + i*48, 48, 48)
                if bird_rect.colliderect(block_rect):
                    damage = get_damage(bird.type, block.type)
                    block.take_damage(damage)

                    if double_damage_enabled: 
                        block.take_damage(damage)
                        damage*=2
                    
                    if block.health==0: grid[i][j]=None
                    falling_blocks(grid)
                    return damage * 10 # Return score
    return 0

def structure_demolished(grid):
    for i in range(4):
        for j in range(4):
            if (grid[i][j] != None):
                if (grid[i][j].health != 0):
                    return False
    return True