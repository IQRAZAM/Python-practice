####### pynput module 
'''from pynput import keyboard
def onPress(key):
    try:
        print(f'key {key.char} pressed')
    except AttributeError:
        print(f"key {key} pressed")
def onRelease(key):
    print(f"key {key} released")
    if key == keyboard.key.esc:
        return False
with keyboard.Listener(onPress = onPress , onRelese = onRelease) as Listener:
    Listener.join()'''
# a part of pygame for button events 
#    if event.type == pygame.KEYDOWN:
    #        if event.key == pygame.K_LEFT:
    #            print("left key is being pressed ")
#####using pygame basics to make a game 
import pygame 
import random
x = pygame.init()
#colors
white = (255,255,255)
black = (0,0,0)
pink = (255, 192, 203)
neon = (57, 255, 20)
#print(x)
screen_width = 1000 
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("my Pookie game")
#game specific variables 
exit_game = False
game_over = False 
snake_x = 45
snake_y = 55
snake_size_x =10
snake_size_y =10
velocity_x = 0
velocity_y = 0
fps = 30
score = 0
food_x = random.uniform(20,screen_width/2)
food_y = random.uniform(20,screen_height/2)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,40)
snk_length = 1
snk_list = []
def textScreen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plotsnake(gameWindow,color,snk_list,x1,y1):
    for x,y in snk_list:
      pygame.draw.ellipse(gameWindow,color,(x,y,snake_size_x,snake_size_y))
def gameover():
     if game_over == True:
        gameWindow .fill(white)
        textScreen("Game over",neon,100,100)
#looping through 
while not exit_game:
    for event in pygame.event.get():
       # print(event)
       if event.type == pygame.QUIT:
           exit_game = True
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
               velocity_x  = 10
               velocity_y = 0
           if event.key == pygame.K_LEFT:
               velocity_x =  - 10
               velocity_y = 0
           if event.key == pygame.K_UP:
               velocity_y=  - 10 
               velocity_x = 0      #Coordinate System in Pygame:
           if event.key == pygame.K_DOWN:
               velocity_y= 10
               velocity_x = 0
               #cheat code 
           if event.key == pygame.K_q:
                score += 10

           if snake_x<0 or snake_x > screen_width or snake_y<0 or snake_y > screen_height:
               game_over = True
               print("game over")
               gameover()
           
# Origin (0, 0): In Pygame, the origin (0, 0) is at the top-left corner of the window.
# X-Axis: The x-coordinate increases as you move to the right.
# Y-Axis: The y-coordinate increases as you move downward.
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    #chnaging score an dproducing food randomly
    if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
        score = score +1
        food_x = random.uniform(20,screen_width/2)
        food_y = random.uniform(20,screen_height/2)
        snk_length += 5
    gameWindow.fill(pink)
    textScreen("Score" + str(score),neon,5,5)
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list)>snk_length:
        del snk_list[0]
    plotsnake(gameWindow,black,snk_list,snake_size_x,snake_size_y)
                      
    pygame.draw.rect(gameWindow,neon,(food_x,food_y,snake_size_x,snake_size_y))
    pygame.display.update()     #run it everytime to make changes to game  
    clock.tick(fps)
               
pygame.quit()
quit()
#########another oneee
'''import pygame 
import random
x = pygame.init()
#colors
white = (255,255,255)
black = (0,0,0)
pink = (255, 192, 203)
neon = (57, 255, 20)
#print(x)
screen_width = 1000 
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("my Pookie game")
#game specific variables 
snake_x = 45
snake_y = 55
snake_size_x =10
snake_size_y =10
font = pygame.font.SysFont(None,40)
snk_length = 1
snk_list = []
def textScreen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plotsnake(gameWindow,color,snk_list,x1,y1):
    for x,y in snk_list:
      pygame.draw.ellipse(gameWindow,color,(x,y,snake_size_x,snake_size_y))
#looping through 
def gameloop():
    exit_game = False
    game_over = False 
    snake_x = 45
    snake_y = 55
    snake_size_x =10
    snake_size_y =10
    velocity_x = 0
    velocity_y = 0
    fps = 30
    score = 0
    food_x = random.uniform(20,screen_width/2)
    food_y = random.uniform(20,screen_height/2)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,40)
    snk_length = 1
    snk_list = []
    while not exit_game:
        if game_over == True:
            gameWindow .fill(white)
            textScreen("Game over, Press Enter to play again ",neon,100,100)
            for event in pygame.event.get():
        # print(event)
                if event.type == pygame.QUIT:
                        exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
        # print(event)
                if event.type == pygame.QUIT:
                        exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x  = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x =  - 10
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y=  - 10 
                        velocity_x = 0      #Coordinate System in Pygame:
                    if event.key == pygame.K_DOWN:
                        velocity_y= 10
                        velocity_x = 0
                #cheat code 
                    if event.key == pygame.K_q:
                            score += 10

                if snake_x<0 or snake_x > screen_width or snake_y<0 or snake_y > screen_height:
                    game_over == True
    # Origin (0, 0): In Pygame, the origin (0, 0) is at the top-left corner of the window.
    # X-Axis: The x-coordinate increases as you move to the right.
    # Y-Axis: The y-coordinate increases as you move downward.
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            #chnaging score an dproducing food randomly
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score = score +1 
                food_x = random.uniform(20,screen_width/2)
                food_y = random.uniform(20,screen_height/2)
                snk_length += 5 
            gameWindow.fill(pink)
            textScreen("Score" + str(score),neon,5,5)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if head in snk_list[0:-1]:
                game_over ==True
            if len(snk_list)>snk_length:
                del snk_list[0]
            plotsnake(gameWindow,black,snk_list,snake_size_x,snake_size_y)
                            
            pygame.draw.rect(gameWindow,neon,(food_x,food_y,snake_size_x,snake_size_y))
        pygame.display.update()     #run it everytime to make changes to game  
        clock.tick(fps)
gameloop()         
pygame.quit()
quit()'''
