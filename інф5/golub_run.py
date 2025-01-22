import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golub run")
clock = pygame.time.Clock()

fontt = pygame.font.SysFont(None, 40)


background_image = pygame.image.load("background_fon.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("golub.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

class Coinss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coins.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, HEIGHT - self.rect.width)
        self.rect.y = (0)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.y = random.randint(-100, -50)
            self.rect.x = random.randint(0, HEIGHT - self.rect.width)
            self.speed = random.randint(1, 3)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("golub_enemy.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, HEIGHT - self.rect.width)
        self.rect.y = (0)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.y = random.randint(-100, -50)
            self.rect.x = random.randint(0, HEIGHT - self.rect.width)
            self.speed = random.randint(1, 3)

def show_menu():
    title = fontt.render("Golub run", True, (23, 78, 96))
    start_button = fontt.render("Press Enter to Start", True, (200, 197, 45))

    window.fill((0, 0, 0))
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3 - title.get_height() // 2))
    pygame.display.flip()


def GameLoop():
        player = Player(400, 595)




        group_player = pygame.sprite.Group()
        group_player.add(player)

        coins = pygame.sprite.Group()
        for i in range(3):
            coins.add(Coinss())

        enemy = pygame.sprite.Group()
        for i in range(3):
            enemy.add(Enemy())



        leave = 3
        score = 0
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

            for coin in coins:
                if player.rect.colliderect(coin.rect):
                    coin.rect.y = random.randint(-100, -50)
                    coin.rect.x = random.randint(0, WIDTH - coin.rect.width)
                    score += 1

            for enem in enemy:
                if player.rect.colliderect(enem.rect):
                    leave -= 1
                    enem.rect.y = random.randint(-100, -50)
                    enem.rect.x = random.randint(0, WIDTH - enem.rect.width)

            window.blit(background_image, (0, 0))
            group_player.update()
            group_player.draw(window)

            coins.update()
            coins.draw(window)

            enemy.update()
            enemy.draw(window)

            font = pygame.font.SysFont(None, 40)
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            window.blit(score_text, (10, 10))

            if leave <= 0:
                game_running = False

            leave_text = font.render(f"Leave: {leave}", True, (255, 255, 255))
            window.blit(leave_text, (685, 10))

            pygame.display.flip()
            clock.tick(60)


running = True
in_menu = True
while running:
    if in_menu:
        show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    in_menu = False
                    GameLoop()
                    in_menu = True
        

pygame.quit()