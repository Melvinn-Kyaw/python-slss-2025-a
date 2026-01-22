import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Final Project")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 200, 100)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

running = True
while running:
clock.tick(FPS)


for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False
# Key presses for player movement
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] or keys[pygame.K_a]:
player_x -= player_speed
if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
player_x += player_speed
if keys[pygame.K_UP] or keys[pygame.K_w]:
player_y -= player_speed
if keys[pygame.K_DOWN] or keys[pygame.K_s]:
player_y += player_speed

if player_x < 0:
player_x = 0
if player_x > WIDTH - player_size:
player_x = WIDTH - player_size
if player_y < 0:
player_y = 0
if player_y > HEIGHT - player_size:
player_y = HEIGHT - player_size

SCREEN.fill(WHITE)

pygame.draw.rect(SCREEN, GREEN, (100, 100, 200, 100)) 
pygame.draw.rect(SCREEN, GREEN, (500, 400, 200, 100))


pygame.draw.rect(SCREEN, BLUE, (player_x, player_y, player_size, player_size))


pygame.display.flip()


pygame.quit()
sys.exit()
