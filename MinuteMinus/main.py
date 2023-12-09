###
#
## Minus Minute Py Prototype
## Justin Spanos
##
## Started:  November 2023
## Finished:
#
###

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
# Game Initializing Vars
running = True
start_screen = True
titleBlink = True
game_over = False
initialSetUp = True
currentScore = 0
highScore = 0
totalActiveScore = 0

# Game Vars
directionRight = True
blockArray = [[0] * 5 for _ in range(BLOCK_ROW_COUNT + 1)]
blockIdentityArray = [[0] * 5 for _ in range(BLOCK_ROW_COUNT + 1)]
blockRowGen = 0
arrayTotal = 0
smashedBlocked = False
playerForce = 0

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
defaultSkin = pygame.transform.scale(pygame.image.load("player/playerIdleProto.png"), (100, 100))
chickenSkin = pygame.transform.scale(pygame.image.load("player/chickenSkinIdle.png"), (100, 100))
player_image = defaultSkin

trackPlayerSkin = 0

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
try:
    with open("highScore.txt", "r") as file:
        highScore = int(file.read())
except FileNotFoundError:
    highScore = 0

## Functions / Methods
# Create Block Row
def scoreHandling(curSco):
    global currentScore
    if(curSco < 0):
        currentScore = 0

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
    currentScore = totalActiveScore - 10

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

def userSkinSelection():
    global trackPlayerSkin
    global player_image

    print("Changed")

    # Simple else/if statement, will change to a for loop iteration eventually
    if(trackPlayerSkin == 0):
        player_image = chickenSkin
        trackPlayerSkin = 1
        
    elif(trackPlayerSkin == 1):
        player_image = defaultSkin
        trackPlayerSkin = 0

# Display UI
def scoreDisplay():
    score_text = font.render(f"Score: {currentScore}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {highScore}", True, (255, 255, 255))
    screen.blit(score_text, (120, 10))
    screen.blit(high_score_text, (510, 10))

def displayWallUI(wall_img, wall_rect_L, wall_rect_R):
    screen.blit(wall_img, wall_rect_L)
    screen.blit(wall_img, wall_rect_R)

def displayMeterUI(meter_bl, meter_pnt):
    global meter_point_rect
    # Meter objects
    meter_rect_mid = meter_bl.get_rect(center=(SCREEN_WIDTH // 2, 45))
    
    meter_rect_left = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) - 41, 45))
    meter_rect_left_end = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) - 82, 45))
    
    meter_rect_right = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) + 41, 45))
    meter_rect_right_end = meter_bl.get_rect(center=((SCREEN_WIDTH // 2) + 82, 45))

    # Draw the Meter Block
    if(meter_point_rect.x < 390
       and meter_point_rect.x >= 340):
        
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_mid, meter_rect_left, meter_rect_left_end,meter_rect_right,meter_rect_right_end)
        #print("In Mid")
        
    elif(meter_point_rect.x < 340
         and meter_point_rect.x >= 300):
        
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_left, meter_rect_left_end,meter_rect_right,meter_rect_right_end, meter_rect_mid)
        #print("In left")
        
    elif(meter_point_rect.x < 300
         and meter_point_rect.x >= 260
         or meter_point_rect.x == meter_rect_left_end.left):
        
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_left_end, meter_rect_right, meter_rect_right_end, meter_rect_mid, meter_rect_left)
        #print("In left end")

    elif(meter_point_rect.x < 430
         and meter_point_rect.x >= 390):
        
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_right, meter_rect_right_end, meter_rect_mid, meter_rect_left, meter_rect_left_end)
        #print("In right")

    elif(meter_point_rect.x < 520
         and meter_point_rect.x >= 430
         or meter_point_rect.x >= meter_rect_right_end.right):
        
        meterColorChange(meter_bar_hot, meter_bar_warm, meter_rect_right_end, meter_rect_mid, meter_rect_left, meter_rect_left_end, meter_rect_right)
        #print("In right end")

def meterColorChange(meterH, meterW, meter1, meter2, meter3, meter4, meter5):
    screen.blit(meterH, meter1)
    screen.blit(meter_block, meter2)
    screen.blit(meter_block, meter3)
    screen.blit(meter_block, meter4)
    screen.blit(meter_block, meter5)

# Check Collison
def check_collision(player_r, block):
    # Declare Variables
    global currentScore

    for j in range(BLOCK_ROW_COUNT):
        for i in range(5):
            if(player_r.bottom >= block[j][i].top and player_r.bottom <= block[j][i].top and player_rect.x == block[j][i].x and blockIdentityArray[j][i] > 0):
                # Calculate the score of the brick and add it to the current score
                if(blockIdentityArray[j][i] == 1):
                    currentScore -= 1
                    scoreHandling(currentScore)
                elif(blockIdentityArray[j][i] == 2):
                    currentScore -= 3
                    scoreHandling(currentScore)
                elif(blockIdentityArray[j][i] == 3):
                    currentScore -= 5
                    scoreHandling(currentScore)
                # Set the block's identy number to so it will no longer be acted with
                blockIdentityArray[j][i] = 0

# Checks if there is a rect next to player rect
def LeftRightCollision(rectOne, rectTwo):
    global BLOCK_ROW_COUNT
    
    for j in range(BLOCK_ROW_COUNT):
        for i in range(5):
            return rectOne.right == rectTwo[j][i].left or rectOne.left == rectTwo[j][i].right
            
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

# Jump on to boxes
def jumpOnTo(player_r, block):
    global BLOCK_ROW_COUNT
    global blockIdentityArray
    
    for j in range(BLOCK_ROW_COUNT):
        for i in range(5):
            if(player_r.bottom >= block[j][i].top and player_r.bottom <= block[j][i].top and player_r.x == block[j][i].x and blockIdentityArray[j][i] > 0):
                newBlockLocation(player_r, player_r.x + 50, player_r.bottom - 50)
                ("Jumped ON")

# Player Direction
def jumpDirection(originPoint, meterP, playerFrc):
    # set player origin point to a point on the meter
    global player_rect
    originOnMeter = 0

    # Middle Direction
    if(originPoint.x == 350):
        originOnMeter = 400
    # To the right
    elif(originPoint.x == 450):
        originOnMeter = 441
    elif(originPoint.x == 550):
        originOnMeter = 482
    # To the left
    elif(originPoint.x == 250):
        originOnMeter = 359
    elif(originPoint.x == 150):
        originOnMeter = 318
        
    #print(originPoint.x)
    #print(originOnMeter)

    # Middle Direction
    if(meterP.x >= (originOnMeter - 50) and meterP.x < (originOnMeter - 10)):
        print("Jumps Up")

    # Right Direction
    elif(meterP.x >= (originOnMeter - 10) and meterP.x < (originOnMeter + 31)):
        print(f"Jump once right: {meterP.x}")
        player_rect.x += PLAYER_SPEED
        screen.blit(player_image, player_rect)

    elif(meterP.x >= (originOnMeter + 31) and meterP.x < (originOnMeter + 72)):
        print(f"Jump twice right: {meterP.x}")
        #player_rect.x += (PLAYER_SPEED * 2)
        
    # Left Direction
    elif(meterP.x >= (originOnMeter - 93) and meterP.x < (originOnMeter - 50)):
        print(f"Jump once left: {meterP.x}")
        #player_rect.x -= PLAYER_SPEED

    elif(meterP.x >= (originOnMeter - 136) and meterP.x < (originOnMeter - 93)):
        print(f"Jump twice left: {meterP.x}")
        #player_rect.x -= (PLAYER_SPEED * 2)

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
                # Player Movement
                if LeftRightCollision(player_rect, blockArray):
                    player_rect.x = player_rect.x
                else:
                    player_rect.x -= PLAYER_SPEED
                    
                screen.fill((0, 0, 0))
                # Display UI
                scoreDisplay()
                displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                # Display Meter 
                displayMeterUI(meter_block, meter_point)
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
                # Player Movement
                if LeftRightCollision(player_rect, blockArray):
                    player_rect.x = player_rect.x
                else:
                    player_rect.x += PLAYER_SPEED
                    
                screen.fill((0, 0, 0))
                # Display UI
                scoreDisplay()
                displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                # Display Meter 
                displayMeterUI(meter_block, meter_point)
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
                jumpDirection(player_rect, meter_point_rect, playerForce)
                player_rect.y -= PLAYER_SPEED
                screen.fill((0, 0, 0))
                # Display UI
                scoreDisplay()
                displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                # Display Meter 
                displayMeterUI(meter_block, meter_point)
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
                    scoreDisplay()
                    displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)
                    # Display Meter 
                    displayMeterUI(meter_block, meter_point)
                    screen.blit(meter_point, meter_point_rect)
                    # Display Block Array
                    rowDisplay(blockArray)
                    # Player Display
                    screen.blit(player_image, player_rect)
                    pygame.display.flip()

                    # Jump on a box
                    if(playerInAir == False and i < 8):
                        jumpOnTo(player_rect, blockArray)
                        break
                    else:
                        check_collision(player_rect, blockArray)
                           
                    if(i == 9):
                        playerInAir = False
        
        if keys[pygame.K_DOWN]:
            userSkinSelection()
            
        # Temporary developer Game Over Exit
        if keys[pygame.K_f]:
            game_over = True

    # Start Screen
    while(start_screen == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Start the game when space bar is pressed
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_SPACE]:
            start_screen = False
        
        # Print a blank screen
        screen.fill((0, 0, 0))

        # Print title
        title_text = font.render("MINUS MINUTE", True, (0, 255, 255))
        screen.blit(title_text, ((SCREEN_WIDTH // 2) - 90, (SCREEN_HEIGHT // 2) - 70))

        # Print flickering start prompt 
        if(titleBlink == True):
            start_text = font.render("PRESS SPACE TO START", True, (150, 0, 255))
            screen.blit(start_text, ((SCREEN_WIDTH // 2) - 140, (SCREEN_HEIGHT // 2) + 180))
            titleBlink = False
            clock.tick(8000)
        else:
            start_text = font.render("PRESS SPACE TO START", True, (0, 0, 0))
            screen.blit(start_text, ((SCREEN_WIDTH // 2) - 140, (SCREEN_HEIGHT // 2) + 180))
            titleBlink = True
        
        pygame.display.flip()
            
    # Create The Block Rows
    if initialSetUp == True:
        CreateABlockRow(blockArray)
        initialSetUp = False

    # Print a blank screen
    screen.fill((0, 0, 0))

    # Score
    scoreDisplay()

    # Print the row
    rowDisplay(blockArray)
                
    # Handling Player
    gravityKinda(player_rect, blockArray)
    screen.blit(player_image, player_rect)

    # Display UI
    displayWallUI(wall_image, wall_img_rect_L, wall_img_rect_R)

    # Display Meter 
    displayMeterUI(meter_block, meter_point)
    
    ## Move the Meter
    if meter_point_rect.x < ORIGINAL_METER_X + 100 and directionRight == True:
        meter_point_rect.x += 1
        if meter_point_rect.x == ORIGINAL_METER_X + 100:
            directionRight = False
    elif meter_point_rect.x > ORIGINAL_METER_X - 100 and directionRight == False:
        meter_point_rect.x -= 1
        if meter_point_rect.x == ORIGINAL_METER_X - 100:
            directionRight = True

    # Draw the Meter
    screen.blit(meter_point, meter_point_rect)

    # Main Game Loop Graphics
    pygame.display.flip()
    clock.tick(100)

    if(currentScore <= 0):
        game_over = True

    # Game Over
    if game_over:
        # Save the high score
        if currentScore > highScore:
            highScore = currentScore
            with open("highScore.txt", "w") as file:
                file.write(str(highScore))
                
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Re-start the game when space bar is pressed
            keys = pygame.key.get_pressed()  
            if keys[pygame.K_SPACE]:
                blockArray = [[0] * 5 for _ in range(BLOCK_ROW_COUNT + 1)]
                blockIdentityArray = [[0] * 5 for _ in range(BLOCK_ROW_COUNT + 1)]
                totalActiveScore = 0
                currentScore = 0
                player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300)
                initialSetUp = True
                game_over = False
                    
            # Print a blank screen
            screen.fill((0, 0, 0))

            score_text = font.render(f"Score: {currentScore}", True, (255, 255, 255))
            screen.blit(score_text, ((SCREEN_WIDTH // 2) - 50, (SCREEN_HEIGHT // 2) + 30))

            high_score_text = font.render(f"High Score: {highScore}", True, (255, 255, 255))
            screen.blit(high_score_text, ((SCREEN_WIDTH // 2) - 85, (SCREEN_HEIGHT // 2) - 20))

            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, ((SCREEN_WIDTH // 2) - 80, (SCREEN_HEIGHT // 2) - 70))

            retry_text = font.render("PRESS SPACE TO RETRY", True, (150, 0, 255))
            screen.blit(retry_text, ((SCREEN_WIDTH // 2) - 140, (SCREEN_HEIGHT // 2) + 180))

            pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()







