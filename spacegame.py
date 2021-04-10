import math
import random

import pygame

# initiates the pygame
pygame.init()  # this line must be added for game

# create the screen in which the game will be played in
# specified as widthscreen y=800pcs,,, hightscreen x =600
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('space.png.png')
# changing the logo of the window and the backgroup picture of the window
pygame.display.set_caption("space Invadors")
# pygame.display changes the caption
icon = pygame.image.load('missile.ico')
# pygame.image.load sets the icon variable to the chosen picture
pygame.display.set_icon(icon)  # this command sets the icon to our chosen icon

# player
PlayerImg = pygame.image.load('spaceship.png')
playerX = 370  # these x and y values plave the image on the "graph"
playerY = 480
playerX_change = 0
# enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for I in range(num_of_enemies):
    EnemyImg.append(pygame.image.load(
        'monster.png'))  # the append function adds all of these to the list, instead of writing this 6x more
    EnemyX.append(random.randint(0, 735))  # random.randint will randomize the numbers
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(40)
    EnemyY_change.append(60)
# Bullet
BulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletX_change = 1
BulletY_change = 2
Bullet_state = "ready"  # ready state= cant see the bullet

score = 0  # varibale for score


def player(x, y):
    screen.blit(PlayerImg, (x, y))  # blit is the command for draw


# blit requires the image and its position

def Enemy(x, y, I):
    screen.blit(EnemyImg[I], (x, y))


def Fire_Bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))


def iscollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt(math.pow(EnemyX - BulletX, 2) + math.pow(EnemyY - BulletY,
                                                                  2))  # euqation squrt((x2-x)^2 + (y2-y1)^2), is used to measure distance between two points
    if distance < 27:  # so if the ditance between the enemy and the bullet is less than 27 pixles, then there is collison
        return True
    else:
        return False


# running is turned into a variable
# game loop is created
# so we have imported the event from pygame byt the get method
# if x is pressed while statments "running" is turned to flase
running = True
while running:

    screen.fill((0, 0, 0))  # RGB is red grren blue and using these u can make any color
    # can search rgb values, this command needs to be under looop , because we want the screen to constanly have that color
    # playerX += 0.1 #this allows the image to move 0.1 to the right, in the X direction. a negative sign will do viseversa

    # background image we want it here coz constant
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed, check whether it is left or right
    if event.type == pygame.KEYDOWN:  # this tells if a key is pressed
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3  # this will say if left is pressed with the speed of 0.1 it should go to the left
        if event.key == pygame.K_RIGHT:
            playerX_change = +0.3
        if event.key == pygame.K_SPACE:
            if Bullet_state is "ready":  # only when the bullet has travelled fully then the space key works
                BulletX = playerX  # get the bullet at the player x X value, so fires from spaceship
                Fire_Bullet(playerX, BulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            # this tells if the key is up "stopped being pressed"
            playerX_change = 0  # this is saying that the spaceship needs to stop after key is stopped
    # checkign for bnoundaries of spaceship
    playerX += playerX_change
    if playerX <= 0:  # if the spaceship goes below 0 in X coordiates,
        playerX = 0  # it shall be put back to 0
    elif playerX >= 736:  # if it goes to the right past 800,
        playerX = 736  # it shall be put back to 800
    for I in range(num_of_enemies):
        # bounderies for enemy movments
        EnemyX[I] += EnemyX_change[I]
        if EnemyX[I] <= 0:  # if the spaceship goes below 0 in X coordiates,
            EnemyX_change[I] = 0.2  # it shall be put back to 0
            EnemyY[I] += EnemyY_change[I]
        elif EnemyX[I] >= 736:  # if it goes to the right past 800,
            EnemyX_change[I] = -0.2
            EnemyX[I] += EnemyX_change[I]
        # collison
        collison = iscollision(EnemyX[I], EnemyY[I], BulletX, BulletY)
        if collison:
            BulletY = 480
            Bullet_state = "ready"
            score += 1
            print(score)
            EnemyX[I] = random.randint(0, 735)  # need the coordiantes to respawn the enemy
            EnemyY[I] = random.randint(50, 150)

        Enemy(EnemyX[I], EnemyY[I], I)

    # Bullet movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"

    if Bullet_state is "fire":
        Fire_Bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    player(playerX, playerY)  # this under the while loop will show the "player" at all times

    pygame.display.update()  # this will updat eteh screen and keep the color contant
    # must also be added always
