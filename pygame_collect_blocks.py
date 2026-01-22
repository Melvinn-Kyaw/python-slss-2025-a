import pygame
import random

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

class Block(pygame.sprite.Sprite):
    def __init__(self, colour: pygame.Color, width: int, height: int):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100

        self.point_value = 1

    def level_up(self, val: int):
        self.point_value *= val

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """The player"""
        super().__init__()

        self.image_right =  pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0              
        self.health = 100
        self.points = 0

    def calc_damage(self, amt: int) -> int:

        Returns:
  
        self.health -= amt
        return self.health

    def incr_score(self, amt: int) -> int:
        Returns:
        self.points += amt
        return self.points

    def get_damage_percentage(self) -> float:
        return self.health / 100

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x

def game():
    pygame.init()

    WIDTH = 700
    HEIGHT = 400
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    done = False
    clock = pygame.time.Clock()
    num_enemies = 5
    num_blocks = 100
    health_bar = HealthBar(200, 10)
    level = 1

    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()


    for _ in range(num_blocks):
        block = Block(BLUE, 20, 10)
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(block)
        block_sprites_group.add(block)

    player = Mario()
    player.rect.center = (WIDTH / 2, HEIGHT / 2)
    all_sprites_group.add(player)


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        all_sprites_group.update()


        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        for block in blocks_collided:
            if type(block) is Block:
                print("Player score: ", player.incr_score(block.point_value))

  
        if not block_sprites_group:
            level += 1

            for _ in range(num_blocks):
                block = Block(BLUE, 20, 10)

                block.rect.centerx = random.randrange(0, WIDTH)
                block.rect.centery = random.randrange(0, HEIGHT)

                block.level_up(level)

                all_sprites_group.add(block)
                block_sprites_group.add(block)


        health_bar.update_info(player.get_damage_percentage())

        if player.health <= 0:
            done = True

        screen.fill(WHITE)
        all_sprites_group.draw(screen)
        screen.blit(health_bar, (10, 10))

        pygame.display.flip()

        clock.tick(120) # 120 fps

    print("Good game!")
    print("Score:", player.points)

    pygame.quit()

if __name__ == "__main__":
    game()
