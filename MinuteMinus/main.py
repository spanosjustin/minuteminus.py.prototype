
#
#
# When coliding, its accessing this method twice
# Make this impossible
#
# Maybe related, but its destroying the block underneath it
#
#

### Minus Minute Python Prototype
import pygame
import sys
import random

# Initialize Game
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 10
ORIGINAL_METER_X = 370
RED_COLOR = (251, 0, 0, 50)
ORANGE_COLOR = (251, 126, 0, 100)
clock = pygame.time.Clock()
BLOCK_ROW_COUNT = 2

# Fonts
font = pygame.font.Font(None, 36)

## Variables
# General Vars
running = True
initialSetUp = True
currentScore = 0
highScore = 0
totalActiveScore = 0
directionRight = True
blockArray = [[0] * 5 for _ in range(BLOCK_ROW_COUNT + 1)]
blockIdentityArray = [[0] * 5 for _ in range(BLOCK_ROW_COUNT + 1)]
blockRowGen = 0
arrayTotal = 0

# Jumping Vars
goingUp = True
playerInAir = False
inTheAirTurnCount = 0

# Create the Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minus Minute Py.Prototype")

# Declare Fonts
font = pygame.font.Font(None, 36)

# declare images
## Player
player_image = pygame.transform.scale(pygame.image.load("player/playerIdleProto.png"), (100, 100))

## Squares
five_box = pygame.transform.scale(pygame.image.load("squares/fiveSqu.png"), (100, 100))
five_box_broken = pygame.transform.scale(pygame.image.load("squares/fiveSquBroken.png"), (100, 100))

three_box = pygame.transform.scale(pygame.image.load("squares/threeSqu.png"), (100, 100))
three_box_broken = pygame.transform.scale(pygame.image.load("squares/threeSquBroken.png"), (100, 100))

one_box = pygame.transform.scale(pygame.image.load("squares/oneSqu.png"), (100, 100))
one_box_broken = pygame.transform.scale(pygame.image.load("squares/oneSquBroken.png"), (100, 100))

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
one_box_rect = one_box.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 200))
one_box_broken_rect = one_box_broken.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

three_box_rect = three_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200))
three_box_broken_rect = three_box_broken.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

five_box_rect = five_box.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200))
five_box_broken_rect = five_box_broken.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))

# Meter Point
meter_point_rect = meter_point.get_rect(center=((SCREEN_WIDTH // 2), 45))

### Load best score from file
##try:
##    with open("best_score.txt", "r") as file:
##        highScore = int(file.read())
##except FileNotFoundError:
##    highScore = 0

## Functions / Methods
# Create Block Row
def CreateABlockRow(blockAr):
    # handling New x & y
    newX = 200
    newY = SCREEN_HEIGHT - 200

    # Scoring Variables
    global totalActiveScore
    global currentScore

    for j in range(BLOCK_ROW_COUNT):
        # Set row's Y cordinance
        if(j > 0):
            newY += 100
        # Iterate, set X location and box's values
        for i in range(5):
            # Set row's X cordinance
            if(i > 0):
                newX += 100
            elif(i == 0):
                newX = 200
            # determine block value  
            r = random.randint(1, 3)
            blockIdentityArray[j][i] = r
            # Assign a value to a memory space in list
            if(r == 1):
                totalActiveScore += 1
                blockAr[j][i] = one_box_rect.copy()
                blockAr[j][i] = newBlockLocation(blockAr[j][i], newX, newY)
                #print("Assigned: ", r, " ",  blockAr[j][i], " ; ", j, i)
            elif(r == 2):
                totalActiveScore += 3
                blockAr[j][i] = three_box_rect.copy()
                blockAr[j][i] = newBlockLocation(blockAr[j][i], newX, newY)
                #print("Assigned: ", r, " ",  blockAr[j][i], " ; ", j, i)
            elif(r == 3):
                totalActiveScore += 5
                blockAr[j][i] = five_box_rect.copy()
                blockAr[j][i] = newBlockLocation(blockAr[j][i], newX, newY)
                #print("Assigned: ", r, " ",  blockAr[j][i], " ; ", j, i)
    # Initialize Score
    currentScore = totalActiveScore

# Create a new instance
def newBlockLocation(rect, x, y):
    rect.center = (x, y)
    return rect

# Display Block Array
def rowDisplay(blockAry):
    for j in range(BLOCK_ROW_COUNT):
        # Iterate and Display Block Array
        for i in range(5):       
            if(blockIdentityArray[j][i] == 1):
                screen.blit(one_box, blockAry[j][i])
                blockIdentityArray[j + 1][i] = 3
                
            elif(blockIdentityArray[j][i] == 2):
                screen.blit(three_box, blockAry[j][i])
                blockIdentityArray[j + 1][i] = 3
                
            elif(blockIdentityArray[j][i] == 3):
                screen.blit(five_box, blockAry[j][i])
            # This sets the last row to 3 which will be used as an object that has no mass for gravity interaction
            #blockIdentityArray[j + 1][i] = 3

# Display UI
def displayWallUI(wall_img, wall_rect_L, wall_rect_R):
    screen.blit(wall_img, wall_rect_L)
    screen.blit(wall_img, wall_rect_R)

def displayMeterUI(meter_bl, meter_pnt, meter_pnt_rect):
    meter_rect_mid = meter_bl.get_rect(center=(SCREEN_WIDTH // 2, 45))
    meter_rect_left = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) - 41, 45))
    meter_rect_left_end = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) - 82, 45))
    meter_rect_right = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) + 41, 45))
    meter_rect_right_end = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) + 82, 45))

    # Draw the Meter Block
    if(meter_point_rect.x < meter_rect_mid.right and meter_point_rect.x > meter_rect_mid.left):
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_mid, meter_rect_left, meter_rect_left_end,meter_rect_right,meter_rect_right_end)

    elif(meter_point_rect.x < meter_rect_left.right and meter_point_rect.x > meter_rect_left.left):
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_left, meter_rect_left_end,meter_rect_right,meter_rect_right_end, meter_rect_mid)
        
    elif(meter_point_rect.x < meter_rect_left_end.right and meter_point_rect.x > meter_rect_left_end.left):
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_left_end, meter_rect_right, meter_rect_right_end, meter_rect_mid, meter_rect_left)
        
    elif(meter_point_rect.x < meter_rect_right.right and meter_point_rect.x > meter_rect_right.left):
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_right, meter_rect_right_end, meter_rect_mid, meter_rect_left, meter_rect_left_end)
        
    elif(meter_point_rect.x < meter_rect_right_end.right and meter_point_rect.x > meter_rect_right_end.left):
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_right_end, meter_rect_mid, meter_rect_left, meter_rect_left_end, meter_rect_right)
        
##    screen.blit(meter_bl, meter_rect_mid)
##    screen.blit(meter_bl, meter_rect_left)
##    screen.blit(meter_bl, meter_rect_left_end)
##    screen.blit(meter_bl, meter_rect_right)
##    screen.blit(meter_bl, meter_rect_right_end)

def meterColorChange(meterH, meterW, meter1, meter2, meter3, meter4, meter5):
    screen.blit(meterH, meter1)
    screen.blit(meter_block, meter2)
    screen.blit(meter_block, meter3)
    screen.blit(meter_block, meter4)
    screen.blit(meter_block, meter5)

# Check Collison
def check_collision(player_r, block):
    #rowToCheck = player_r.y - 100
    global currentScore

    for j in range(BLOCK_ROW_COUNT):
        for i in range(5):
            if(player_r.bottom >= block[j][i].top and player_r.bottom <= block[j][i].top and player_rect.x == block[j][i].x and blockIdentityArray[j][i] > 0):
                # Calculate the score of the brick and add it to the current score
                if(blockIdentityArray[j][i] == 1):
                    currentScore -= 1
                elif(blockIdentityArray[j][i] == 2):
                    currentScore -= 3
                elif(blockIdentityArray[j][i] == 3):
                    currentScore -= 5
                # Set the block's identy number to so it will no longer be acted with
                blockIdentityArray[j][i] = 0
                print("Current Score: ", currentScore)
            
def gravityKinda(player_r, block):
    for j in range(BLOCK_ROW_COUNT):
        for i in range(5):
            if(player_r.bottom < block[j][i].bottom and player_rect.x == block[j][i].x and blockIdentityArray[j][i] == 0):
                player_r.y += 5
                screen.blit(player_image, player_r)
            # Fall when there's no block under you
            elif(player_r.top > block[j][i].bottom and blockIdentityArray[j + 1][i] == 3):
                player_r.y += 5
                screen.blit(player_image, player_r)

# Row Timer
def rowTimer():
    print("Count down")

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
                displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                # Display Meter 
                displayMeterUI(meter_block, meter_point, meter_point_rect)
                screen.blit(meter_point, meter_point_rect)
                # Row Display
                rowDisplay(blockArray)
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
                displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                # Display Meter 
                displayMeterUI(meter_block, meter_point, meter_point_rect)
                screen.blit(meter_point, meter_point_rect)
                # Dispay Block Array
                rowDisplay(blockArray)
                # Player Display
                screen.blit(player_image, player_rect)
                pygame.display.flip()
            
        if keys[pygame.K_UP] and player_rect.top > 0:
            originalPos = player_rect.y
            for i in range(11):
                # Graphic Logic
                clock.tick(50)
                player_rect.y -= PLAYER_SPEED
                screen.fill((0, 0, 0))
                # Display UI
                displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                # Display Meter 
                displayMeterUI(meter_block, meter_point, meter_point_rect)
                screen.blit(meter_point, meter_point_rect)
                # Display Block Array
                rowDisplay(blockArray)
                # Player Display
                screen.blit(player_image, player_rect)
                pygame.display.flip()
                if(i == 10):
                    playerInAir = True
            if(playerInAir == True):
                for i in range(11):
                    # Graphic Logic
                    clock.tick(50)
                    player_rect.y += PLAYER_SPEED
                    screen.fill((0, 0, 0))
                    # Display UI
                    displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                    # Display Meter 
                    displayMeterUI(meter_block, meter_point, meter_point_rect)
                    screen.blit(meter_point, meter_point_rect)
                    # Display Block Array
                    rowDisplay(blockArray)
                    # Player Display
                    screen.blit(player_image, player_rect)
                    pygame.display.flip()
                    if(i == 10):
                        playerInAir = False
                        check_collision(player_rect, blockArray)

    # Create The Block Rows
    if initialSetUp == True:
        CreateABlockRow(blockArray)
        initialSetUp = False

    # Print a blank screen
    screen.fill((0, 0, 0))

    # Print the row
    rowDisplay(blockArray)
                
    # Handling Player
    gravityKinda(player_rect, blockArray)
    screen.blit(player_image, player_rect)

    # Display UI
    displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)

    # Display Meter 
    displayMeterUI(meter_block, meter_point, meter_point_rect)
    
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

    # Main Game Loop Graphics
    pygame.display.flip()
    clock.tick(100)

# Quit Pygame
pygame.quit()
sys.exit()







