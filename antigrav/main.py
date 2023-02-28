import math
import pygame
import random

pygame.font.init()
pygame.mixer.init()

# Define screen constants
kScreenHeight = 750
kScreenWidth = 1000

# Define player constants
kPlayerRadius = 41
kPlayerSpeed = 0.035
kPlayerJumpPower = -4
kPlayerMaxJumps = 3

# Define game constants
kGrav = 0.09
kFric = 100
kWallGrav = 0.02
kMaxWallGrav = 2.3

# Define game variables
playerAcceleration = [0,0]
gameCounter = 0
jumps = 0

# Define colors
cBlack = (0,0,0)
cWhite = (255,255,255)

# Create button mappings
buttonMap = {
    pygame.K_LEFT : False,
    pygame.K_RIGHT : False,
    pygame.K_SPACE : False,
    pygame.K_DOWN : False,
}

# Create game screen
window = pygame.display.set_mode((kScreenWidth, kScreenHeight))
pygame.display.set_caption('Moving player')

# Create player
player = pygame.Rect(kPlayerRadius, (kScreenHeight - kPlayerRadius), kPlayerRadius, kPlayerRadius)


# calculate player movement every 10 game cycles
def calcMovement():
    if buttonMap[pygame.K_LEFT]:
    elif:
    buttonMap[pygame.K_RIGHT]:
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
    if (gameCounter % 10 == 0):      
        calcMovement()
    # Tick game counter
    gameCounter += 1
    
    # Keep the player within the bounds of the screen
    player.clamp_ip(pygame.Rect(0, 0, kScreenWidth, kScreenHeight))
    
    # Draw screen
    window.fill(screenColor)
    pygame.draw.rect(window, playerColor, player)
    pygame.display.update()
