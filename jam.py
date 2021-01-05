"""
jam eaaaa
Made with PyGame
"""

import pygame, sys, time, random


# Difficulty settings
# sahl/ easy     ->  10
# motawasit    ->  25
# s3ib   ->  40
# s3ib bzaf    ->  60
# mymknch haha /imp ->  120
difficulty = 25

# game size
frame_size_x = 740
frame_size_y = 500
# Checks for errors encountered
# ila kano chi akhta2
check_errors = pygame.init()
# had loop for stuation dyal lcode
if check_errors[1] > 0:
    print(f'hadlproblem {check_errors[1]} kyn chi errors , exiting...')
    sys.exit(-1)
else:
    print('good game')


# lwindow dyal display
pygame.display.set_caption('jamal game')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R/hmer, G/khder, B/khl) green
black = pygame.Color(0, 0, 0)
green = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
white = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# setting dyal fps
fps_controller = pygame.time.Clock()


# variables dlgame
jam_pos = [100, 50]
jam_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


# Game is Over / mnine ktkhser
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score /dlgame
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame display /p1
#  logic:/
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down #(until myb9ach hahaha)
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right 
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # "jam" esc
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the sneky haha cannot move in opposite direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving 
    if direction == 'UP':
        jam_pos[1] -= 10
    if direction == 'DOWN':
        jam_pos[1] += 10
    if direction == 'LEFT':
        jam_pos[0] -= 10
    if direction == 'RIGHT':
        jam_pos[0] += 10

    #  body growing mechanism / yumikoo tchaaan i see you
    jam_body.insert(0, list(jam_pos))
    if jam_pos[0] == food_pos[0] and jam_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        jam_body.pop()

    # food on the screen /random for sure
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    # cg
    game_window.fill(black)
    for pos in jam_body:
        # drawing mic///(londjam, xy-coordonee...)
        # xy-coordonee -> (x, y, size_x, size_y /flboard)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # \ food R
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over / loop ila khsarti
    # and how tkhraj mn lgame
    if jam_pos[0] < 0 or jam_pos[0] > frame_size_x-10:
        game_over()
    if jam_pos[1] < 0 or jam_pos[1] > frame_size_y-10:
        game_over()
    # ext..dlf mic
    for block in jam_body[1:]:
        if jam_pos[0] == block[0] and jam_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    # /deset/:
    fps_controller.tick(difficulty)