import pygame
import random


#colors
white = (255, 255, 255)
red = (255, 0 ,0)
black = (0, 0, 0)
game_width = 900
game_height = 600
pygame.init()
game_display = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("snake game")
pygame.display.update()


exit_game = False
game_over = False


snake_x = 45
snake_y = 55
velocity_x = 3
velocity_y = 3

food_x = random.randint(10, game_width )
food_y = random.randint(10, game_height )
score = 0
snake_size = 30
fps = 60

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_display.blit(screen_text, [x,y])

def plot_snake(game_display, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_display, color, [x, y, snake_size, snake_size])



snk_list = []
snk_length = 1    
while not exit_game:
    for event in pygame.event.get() :
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_RIGHT:
                # snake_x = snake_x + 10 
                velocity_x = 3
                velocity_y= 0

            if event.key == pygame.K_LEFT:
                # snake_x = snake_x - 10 
                velocity_x = -3
                velocity_y = 0

            if event.key == pygame.K_UP:
                # snake_y = snake_y - 10  
                velocity_y = -3
                velocity_x= 0  

            if event.key == pygame.K_DOWN:
                # snake_y = snake_y + 10   
                velocity_y = 3
                velocity_x = 0     
      
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x) <6 and abs(snake_y - food_y) < 6 :
        score += 1
        food_x = random.randint(10, game_width  )
        food_y = random.randint(10, game_height ) 
        snk_length += 5
        

    game_display.fill(white)
    text_screen("score : "+ str( score * 10), red, 5, 5)
    pygame.draw.rect(game_display, red, [food_x, food_y, snake_size, snake_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]
    # pygame.draw.rect(game_display, black, [snake_x, snake_y, snake_size, snake_size])
    plot_snake(game_display, black, snk_list, snake_size)
    pygame.display.update()  
    clock.tick(fps)  


pygame.quit()
quit()


       