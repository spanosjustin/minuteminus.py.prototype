### Minus Minute Python Prototype
import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 10
ORIGINAL_METER_X = 370
clock = pygame.time.Clock()

## Variables
# General Vars
running = True
directionRight = True
blockArray = []

# Jumping Vars
goingUp = True
playerInAir = False
inTheAirTurnCount = 0

# Create the Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minus Minute Prototype")

# Declare Fonts
font = pygame.font.Font(None, 36)

# declare images
## Player
player_image = pygame.transform.scale(pygame.image.load("player/playerIdleProto.png"), (100, 100))

## Squares
five_box = pygame.transform.scale(pygame.image.load("squares/fiveSqu.png"), (60, 100))
five_box_broken = pygame.transform.scale(pygame.image.load("squares/fiveSquBroken.png"), (60, 100))

three_box = pygame.transform.scale(pygame.image.load("squares/threeSqu.png"), (60, 100))
three_box_broken = pygame.transform.scale(pygame.image.load("squares/threeSquBroken.png"), (60, 100))

one_box = pygame.transform.scale(pygame.image.load("squares/oneSqu.png"), (60, 100))
one_box_broken = pygame.transform.scale(pygame.image.load("squares/oneSquBroken.png"), (60, 100))

## UI images
wall_image = pygame.transform.scale(pygame.image.load("UI/wall.png"), (80, 800))
meter_bar_hot = pygame.transform.scale(pygame.image.load("UI/MeterBarHot.png"), (60, 100))
meter_bar_warm = pygame.transform.scale(pygame.image.load("UI/MeterBarWarm.png"), (60, 100))
meter_block = pygame.transform.scale(pygame.image.load("UI/MeterBlock.png"), (60, 100))
meter_point = pygame.transform.scale(pygame.image.load("UI/MeterPoint.png"), (60, 100))
minus_sign = pygame.transform.scale(pygame.image.load("UI/MinusSign.png"), (60, 100))

## Font Numbers
zero_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontZero.png"), (60, 100))
one_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontOne.png"), (60, 100))
two_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontTwo.png"), (60, 100))
three_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontThree.png"), (60, 100))
four_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontFour.png"), (60, 100))
five_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontFive.png"), (60, 100))
six_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontSix.png"), (60, 100))
seven_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontSeven.png"), (60, 100))
eight_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontEight.png"), (60, 100))
nine_font = pygame.transform.scale(pygame.image.load("fontNumbers/fontNine.png"), (60, 100))

### Initialize Objects
# Player
player_rect = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

# Wall
wall_img_rect_L = wall_image.get_rect(center=(SCREEN_WIDTH // 8, SCREEN_HEIGHT - 300))
wall_img_rect_R = wall_image.get_rect(center=(700, SCREEN_HEIGHT - 300))

# Boxes
one_box_rect = one_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))
one_box_broken_rect = one_box_broken.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

three_box_rect = three_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))
three_box_broken_rect = three_box_broken.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

five_box_rect = five_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))
five_box_broken_rect = five_box_broken.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

# Meter
meter_rect_mid = meter_block.get_rect(center=(SCREEN_WIDTH // 2, 45))
meter_rect_left = meter_block.get_rect(center=((SCREEN_WIDTH // 2) - 41, 45))
meter_rect_left_end = meter_block.get_rect(center=((SCREEN_WIDTH // 2) - 82, 45))
meter_rect_right = meter_block.get_rect(center=((SCREEN_WIDTH // 2) + 41, 45))
meter_rect_right_end = meter_block.get_rect(center=((SCREEN_WIDTH // 2) + 82, 45))

meter_point_rect = meter_point.get_rect(center=((SCREEN_WIDTH // 2), 45))

# Functions / Methods
# Jump Method

def isJumping(originalPos, playerY, gUp):
    while gUp == True:
        if(playerY < (originalPos + 6)):
            print("Going Up")
            playerY += 3
            print(playerY, originalPos)
        elif(playerY >= originalPos + 6 and playerY < 9):
            playerY += 2
            print(playerY, originalPos)
        elif(playerY >= originalPos + 9 and playerY < 11):
            playerY += 1
            if(playerY == 10):
                gUp = False
    while gUp == False:
        if(playerY < (originalPos + 6)):
            print("Going Down")
            playerY -= 3
            if(playerY == originalPosition):
                break
        elif(playerY >= originalPos + 6 and playerY < 9):
            playerY -= 2
        elif(playerY >= originalPos + 9 and playerY < 11):
            playerY -= 1
            print(playerY, originalPos)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Input reader
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > wall_img_rect_L.x + 149:
            for i in range(10):
                # Graphic Logic
                clock.tick(50)
                player_rect.x -= PLAYER_SPEED
                screen.fill((0, 0, 0))
                # Display UI
                screen.blit(wall_image, wall_img_rect_L)
                screen.blit(wall_image, wall_img_rect_R)
                # Display Meter 
                screen.blit(meter_block, meter_rect_mid)
                screen.blit(meter_block, meter_rect_left)
                screen.blit(meter_block, meter_rect_left_end)
                screen.blit(meter_block, meter_rect_right)
                screen.blit(meter_block, meter_rect_right_end)
                # Player Display
                screen.blit(player_image, player_rect)
                pygame.display.flip()
            #player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_rect.right < wall_img_rect_R.x - 40:
            for i in range(10):
                # Graphic Logic
                clock.tick(50)
                player_rect.x += PLAYER_SPEED
                screen.fill((0, 0, 0))
                # Display UI
                screen.blit(wall_image, wall_img_rect_L)
                screen.blit(wall_image, wall_img_rect_R)
                # Display Meter 
                screen.blit(meter_block, meter_rect_mid)
                screen.blit(meter_block, meter_rect_left)
                screen.blit(meter_block, meter_rect_left_end)
                screen.blit(meter_block, meter_rect_right)
                screen.blit(meter_block, meter_rect_right_end)
                # Player Display
                screen.blit(player_image, player_rect)
                pygame.display.flip()
            
        if keys[pygame.K_UP] and player_rect.top > 0:
            print("Jumped")
            originalPos = player_rect.y
            for i in range(10):
                # Graphic Logic
                clock.tick(50)
                player_rect.y -= PLAYER_SPEED
                screen.fill((0, 0, 0))
                # Display UI
                screen.blit(wall_image, wall_img_rect_L)
                screen.blit(wall_image, wall_img_rect_R)
                # Display Meter 
                screen.blit(meter_block, meter_rect_mid)
                screen.blit(meter_block, meter_rect_left)
                screen.blit(meter_block, meter_rect_left_end)
                screen.blit(meter_block, meter_rect_right)
                screen.blit(meter_block, meter_rect_right_end)
                # Player Display
                screen.blit(player_image, player_rect)
                pygame.display.flip()
                if(i == 9):
                    playerInAir = True
            if(playerInAir == True):
                for i in range(10):
                    # Graphic Logic
                    clock.tick(50)
                    player_rect.y += PLAYER_SPEED
                    screen.fill((0, 0, 0))
                    # Display UI
                    screen.blit(wall_image, wall_img_rect_L)
                    screen.blit(wall_image, wall_img_rect_R)
                    # Display Meter 
                    screen.blit(meter_block, meter_rect_mid)
                    screen.blit(meter_block, meter_rect_left)
                    screen.blit(meter_block, meter_rect_left_end)
                    screen.blit(meter_block, meter_rect_right)
                    screen.blit(meter_block, meter_rect_right_end)
                    # Player Display
                    screen.blit(player_image, player_rect)
                    pygame.display.flip()
                    if(i == 9):
                        playerInAir = False
            #player_rect.y -= 100
            #playerInAir = True
            
##            if(player_rect.y < originalPos):
##                player_rect.y += 100
##                print(player_rect.y)
            #if goingUp == True:
##            if(player_rect.y <= originalPos - 20):
##                print("Going UP step 1")
##                player_rect.y -= 5
##                screen.blit(player_image, player_rect)
##                print(player_rect.y, originalPos)
##                if(player_rect.y >= originalPos - 20 and player_rect.y < originalPos - 30):
##                    player_rect.y -= 2
##                    screen.blit(player_image, player_rect)
##                    print(player_rect.y, originalPos)
##                    if(player_rect.y >= originalPos - 30 and player_rect.y < originalPos - 35):
##                        player_rect.y -= 1
##                        screen.blit(player_image, player_rect)
##                        if(i == 100):
##                            goingUp = False
##                            print("goingUp is False")
##                        
##            if goingUp == False:
##                if(player_rect.y < (originalPos + 6)):
##                    print("Going Down")
##                    player_rect.y -= 3
##                    if(player_rect.y == originalPosition):
##                        goingUp = True
##                        print("Done")
##                elif(player_rect.y >= originalPos + 6 and player_rect.y < 9):
##                    player_rect.y -= 2
##                elif(player_rect.y >= originalPos + 9 and player_rect.y < 11):
##                    player_rect.y -= 1
##                    print(player_rect.y, originalPos)

    screen.fill((0, 0, 0))  
    # Display Player
    screen.blit(player_image, player_rect)

    # Display UI
    screen.blit(wall_image, wall_img_rect_L)
    screen.blit(wall_image, wall_img_rect_R)

    # Display Meter 
    screen.blit(meter_block, meter_rect_mid)
    screen.blit(meter_block, meter_rect_left)
    screen.blit(meter_block, meter_rect_left_end)
    screen.blit(meter_block, meter_rect_right)
    screen.blit(meter_block, meter_rect_right_end)
    
    # Move the Meter
    if meter_point_rect.x < ORIGINAL_METER_X + 100 and directionRight == True:
        meter_point_rect.x += 2
        if meter_point_rect.x == ORIGINAL_METER_X + 100:
            directionRight = False
    elif meter_point_rect.x > ORIGINAL_METER_X - 100 and directionRight == False:
        meter_point_rect.x -= 2
        if meter_point_rect.x == ORIGINAL_METER_X - 100:
            directionRight = True

    # Draw the Meter
    screen.blit(meter_point, meter_point_rect)

##    if(playerInAir == True):
##        if(inTheAirTurnCount == 0):
##            inTheAirTurnCount = 1
##        else:
##            clock.tick(25000)
##            player_rect.y += 100
##            playerInAir = False
##            inTheAirTurnCount = 0

    # Main Game Loop Clean Ups
    pygame.display.flip()
    clock.tick(100)

# Quit Pygame
pygame.quit()
sys.exit()







