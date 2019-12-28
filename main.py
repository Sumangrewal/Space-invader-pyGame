import pygame
import math
import random

pygame.init()
# display screen
screen = pygame.display.set_mode((800, 600))

# bakcground
background = pygame.image.load("back.png")

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)
# player
playerimg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# enemy
enemyimg = pygame.image.load("enemy.png")
# randint so that enemy can appear at random places after death
enemyX = random.randint(0, 730)
enemyY = random.randint(30, 200)
enemyX_change = 2.5
enemyYchange = 25

# Bullet
# two bullet states-ready and fire
bulletimg = pygame.image.load("bullet.png")
bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

Score = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 22, y + 10))


def isCollision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 40:
        return True
    else:
        return False


# close if quit is pressed
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check if any keystrock is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.5
            if event.key == pygame.K_UP:
                playerY_change = -3.5
            if event.key == pygame.K_DOWN:
                playerY_change = 3.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    # calling the player function after screen description
    playerX += playerX_change
    playerY += playerY_change
    enemyX += enemyX_change

    # setting boundaries
    if (playerX < 0):
        playerX = 0
    if (playerX > 730):
        playerX = 730
    if (playerY > 530):
        playerY = 530
    if (playerY < 0):
        playerY = 0
    if (enemyX < 0):
        enemyX_change = 2.5
        enemyY += enemyYchange
    if (enemyX > 730):
        enemyX_change = -2.5
        enemyY += enemyYchange

    # bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = isCollision(bulletX, bulletY, enemyX, enemyY)
    if collision:
        bulletX = playerX
        bulletY = playerY
        bullet_state = "ready"
        enemyX = random.randint(0, 730)
        enemyY = random.randint(30, 200)
        Score += 1
        print(Score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # always used in evry pygame
    pygame.display.update()
