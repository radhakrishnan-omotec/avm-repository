import pygame
import assets
import math, random

class Bird:
    def __init__(self, bird_type, player):
        self.type = bird_type
        self.player = player
        img = assets.bird_images[bird_type]
        self.image = img if player==1 else pygame.transform.flip(img, True, False)
        self.reset() # Initialize remaining values

    def reset(self):
        if self.player == 1:
            self.x, self.y = 280, 430
        else:
            self.x, self.y = 636, 430
        self.vx = self.vy = 0
        self.path = []
        self.launched = False
        self.step = 0

    # Create trajectory according to vx, vy
    def simulate(self, vx, vy, steps):
        pts = []
        x, y = self.x, self.y
        for _ in range(steps):
            x += vx
            y += vy
            vy += 1 # g=1
            if y > 600: break
            pts.append((x, y))
        return pts

    def draw(self):
        assets.screen.blit(self.image, (self.x - self.image.get_width()//2,
                                 self.y - self.image.get_height()//2))

    # Update (x,y) along path
    def update(self):
        if self.launched and self.step < len(self.path):
            self.x, self.y = self.path[self.step]
            self.step += 1

class Block:
    def __init__(self, type):
        self.health = 4
        self.type = type
        self.images = assets.block_images[type]
        self.update_image()

    def update_image(self):
        if self.health > 0:
            self.image = self.images[4 - self.health]
        else:
            self.image = None

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        self.update_image()

class Alien:
    def __init__(self, start_x, base_y):
        self.x = self.start_x = start_x
        self.y = self.base_y = base_y
        self.phase = random.uniform(0,2*math.pi)
        self.image = assets.alien_bird
        self.active = True
        self.respawn_timer = 0

    def update(self):
        if self.active: # Bobbing motion of alien bird
            self.x += 2
            self.phase += (2*math.pi) / 100
            self.y = self.base_y + 20*math.sin(self.phase)
            if self.x + self.image.get_width() > 900:
                self.x = -self.image.get_width()
        else:
            self.respawn_timer -= 1
            if self.respawn_timer <= 0:
                self.active = True
                self.x = self.start_x
                self.phase = random.uniform(0,2*math.pi)

    def draw(self):
        assets.screen.blit(self.image, (self.x, self.y))

    def hit(self):
        self.active = False
        self.respawn_timer = 180 # Adding a respawn delay

class Button:
    def __init__(self, x, y, w, h, text, normal_color=(144,238,144), hover_color =(34,139,34)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.text_color = (0,0,0)

    def draw(self, screen):
        color = self.hover_color if self.rect.collidepoint(pygame.mouse.get_pos()) else self.normal_color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        text_surf = assets.button_font.render(self.text, True, self.text_color)
        screen.blit(text_surf, (self.rect.centerx - text_surf.get_width()//2, self.rect.centery - text_surf.get_height()//2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = text
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, (46,103,248), self.rect)
        border_w = 3 if self.active else 1
        pygame.draw.rect(screen, (0,0,139), self.rect, border_w)

        txt_surf = assets.textbox_font.render(self.text, True, (0,0,0))
        screen.blit(txt_surf, (self.rect.x + 10, self.rect.y + (self.rect.height - txt_surf.get_height())//2))

class Powerup:
    def __init__(self, x, y, powerup_type):
        self.x = x
        self.y = y
        self.type = powerup_type
        self.active = True
        if powerup_type == "full_path":
            self.image = assets.full_path
        elif powerup_type == "double_dmg":
            self.image = assets.double_dmg
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, screen):
        if self.active: screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, pos):
        return self.active and self.rect.collidepoint(pos)

    def use(self):
        self.active = False