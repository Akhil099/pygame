import pygame
import time
import random
pygame.font.init()   # to use font pygame makes us to initialize the font

WIDTH, HEIGHT = 1000, 800 #in caps as they are constant values in pixels
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #WIN is Window
pygame.display.set_caption("Space Dodge")

BG = pygame.image.load("bg.jpeg")  #if the image is small and you want to spread it to the whole screen then you can use 'bg = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))' to scale the image to the window size

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont("Times New Roman", 24)
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 4

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0)) # special method that is used to draw an image or a surface onto the screen (0,0) is the top left corner of the background image should be placed , then the width and height is fixed
    
    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "white")  #1 here makes our font look better
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, 'red', player)  #player provides the coordinates, drawing the rectangle on WINDow and color is red
    
    for star in stars: 
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update() # update refresh the display and applies the changes


def main():   #contains the main logic of the game
    run = True
    
    player = pygame.Rect(200,HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH,PLAYER_HEIGHT)  #means the rectangle will start from the 740 pixels from the top left corner of the and we are giving all the 4 dimensions of rectangle
    
    clock = pygame.time.Clock()
    
    start_time  = time.time()   #Gives the current time
    elapsed_time = 0 
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    
    while run:
        
        star_count += clock.tick(60) #delay the while loop only till 60 loops per second, returning number of milliseconds before the last tick
        elapsed_time = time.time() - start_time  #number of seconds since we have started the game
        
        if star_count > star_add_increment:
            for _ in range(3):   # '_' is a place holder
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)#-STAR_HEIGHT IS GIVEN AS WE WANT THE STAR TO MOVE SLOWLY ON THE SCREEN RATHER THAN APPEARING ON THE SCREEN AND MOVING DOWNWARDS
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50) #To generate the stars a little bit faster by subtracting in -50 seconds faster
            star_count = 0
        
        for event in pygame.event.get(): #a list containing all differ3ent evnets that have ocuured in the iteration of the loop
            if event.type == pygame.QUIT:
                run = False
                break
            
            
        keys = pygame.key.get_pressed()  #list of keys that are pressed in the game
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:  #it is the key code for the left key, FOR KEY a is K_a, for shift key is K_SHIFT, for SPACE key is K_SPACE
            player.x -= PLAYER_VEL
        
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH: 
            player.x += PLAYER_VEL      # we can even access for height and breadth
            
        for star in stars[:]:  #REMOVE THE STARS THAT HIT THE PLAYER OR HIT THE BOTTOM OF THE SCREEN
            star.y +=STAR_VEL
            if star.y >HEIGHT:
                stars.remove(star)
            elif star.y + star.y >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/ 2))
            pygame.display.update()   #as not drawn in the WINDOW we have updated it manually
            pygame.time.delay(10000)
            break
        
        draw(player, elapsed_time, stars)
    
    pygame.quit()
    
    
if __name__ == '__main__':
    main()