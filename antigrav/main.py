import math
import pygame
import random

pygame.font.init()
pygame.mixer.init()

# Define screen constants
screenHeight = 750
screenWidth = 1000

# Define player constants
playerRadius = 41
playerSpeed = 0.035
jumpPower = -4

# Define game Constants
gravity = 0.09
friction = 0.032
wallGrav = 0.02
maxWallGrav = 2.3

# Define variables
playerAcceleration = [0,0]
maxJumps = 100
jumps = 0
# Define colors
screenColor = (0,0,0)
playerColor = (255,255,255)

# Keep game tick
gameCounter = 0

# Init game font and text
font = pygame.font.SysFont("arial", 32)
text = pygame.font.Font.render(font, "lolz", False, (122, 122, 122))
text2 = pygame.font.Font.render(font, "", False, (122, 122, 122))

# Create button mapping
buttonsPressed = {
    pygame.K_LEFT : False,
    pygame.K_RIGHT : False,
    pygame.K_SPACE : False,
    pygame.K_DOWN : False,
    pygame.K_LALT : False
}

# Create game screen
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Moving player')

# Create player
player = pygame.Rect(playerRadius, (screenHeight - playerRadius), playerRadius, playerRadius)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key in buttonsPressed:
                buttonsPressed[event.key] = True
        
        if event.type == pygame.KEYUP:
            if event.key in buttonsPressed:
                buttonsPressed[event.key] = False
    
    # Movement handling
    if (gameCounter % 10 == 0 and not buttonsPressed[pygame.K_LALT]) or (gameCounter % 30 == 0 and buttonsPressed[pygame.K_LALT]):               
        # Controls player jumping
        if player.y == (screenHeight - playerRadius):
            jumps = 0
        if buttonsPressed[pygame.K_SPACE] and jumps < maxJumps:
            buttonsPressed[pygame.K_SPACE] = False
            jumps += 1
            playerAcceleration[1] = jumpPower
            
        # Control player movement
        if buttonsPressed[pygame.K_LEFT]:
            playerAcceleration[0] -= playerSpeed
        if buttonsPressed[pygame.K_RIGHT]:
            playerAcceleration[0] += playerSpeed

        # Applies friction if the player is not moving
        if player.y == screenHeight - playerRadius and not buttonsPressed[pygame.K_LEFT] and not buttonsPressed[pygame.K_RIGHT]:
            if playerAcceleration[0] < 0:
                playerAcceleration[0] -= friction
            if playerAcceleration[0] < 0:
                playerAcceleration[0] += friction
        
        if (player.x == (0) and buttonsPressed[pygame.K_LEFT]) or (player.x == (screenWidth - playerRadius) and buttonsPressed[pygame.K_RIGHT]):
            if playerAcceleration[1] < -0.1 :
                playerAcceleration[1] = 0
            elif playerAcceleration[1] > maxWallGrav:
                playerAcceleration[1] -= wallGrav
            elif playerAcceleration[1] < maxWallGrav:
                playerAcceleration[1] += wallGrav
        else:
            playerAcceleration[1] += gravity
            
        # move player
        player.x += playerAcceleration[0]
        player.y += playerAcceleration[1]
            
    # If player is on edge of the screen, stop moving
    if player.y == (screenHeight - playerRadius) and playerAcceleration[1] > 0:
        playerAcceleration[1] = 0
    if player.x == (screenWidth - playerRadius) and playerAcceleration[0] > 0:
        playerAcceleration[0] = 0
    if player.y == (0) and playerAcceleration[1] < 0:
        playerAcceleration[1] = 0
    if player.x == (0) and playerAcceleration[0] < 0:
        playerAcceleration[0] = 0
    
    # Tick game counter
    gameCounter += 1
    
    # Keep the player within the bounds of the screen
    player.clamp_ip(pygame.Rect(0, 0, screenWidth, screenHeight))
    
    if buttonsPressed[pygame.K_LALT]:
        playerColor = (0,0,0)
        screenColor = (255,255,255)
    else:
        playerColor = (255,255,255)
        screenColor = (0,0,0)
    
    # Draw screen
    window.fill(screenColor)
    pygame.draw.rect(window, playerColor, player)
    window.blit(text, (-155, 155))
    window.blit(text2, (400, 200))
    pygame.display.update()