import pygame
import random
# Stable diffusion, dall-e
pygame.init()

# read best score file (autorskie)
file = open("best_score.txt", "r+")
best_score_temp = file.read()
file.close()

# colors (autorskie)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (128, 128, 128)
darkgrey = (60, 60, 60)

# screen (autorskie)
width = 500
height = 700
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('My Jumper')
font1 = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 32)
background_color = grey
background_color_2 = black
background_color_3 = red

# sounds (autorskie)
high_jump_sound = pygame.mixer.music.load('jump.mp3')
jump_sound = pygame.mixer.Sound('normal_jump.mp3')

# player data (wspierane internetem, pozmieniane na swoje)
player = pygame.Surface((30, 30))
player.fill(red)
player_x = 225
x_ch = 0
player_y = 550
y_ch = 0
player_s = 3
jump = False
gravity = 0.5
jump_last = 0
high_jump = 2

# list of available platforms (wspierane internetem, pozmieniane na swoje)
platforms = [[200, 600, 75, 10], [100, 650, 100, 10], [350, 550, 100, 10], [200, 500, 50, 10],
             [250, 450, 100, 10], [100, 350, 50, 10], [150, 200, 75, 10], [250, 250, 100, 10],
             [200, 100, 100, 10], [50, 150, 50, 10]]

# essential data (autorskie)
fps = 60
clock = pygame.time.Clock()
start = True
score = 0
best_score = int(best_score_temp)
last_score = 0
failure = False
pause = False

# zasugerowane internetem ale przerobione na swoje
def update_player_y(p_y):
    global jump
    global jump_sound
    global y_ch
    jump_height = 11
    global gravity
    if jump:
        y_ch = -jump_height
        jump_sound.play()
        jump = False
    p_y += y_ch
    y_ch += gravity
    return p_y

# zasugerowane internetem ale przerobione na swoje
def update_platforms(platforms_list, p_y, y_chng):
    global score
    if p_y < 800 and y_chng < 0:
        for i in range(len(platforms_list)):
            platforms_list[i][1] -= y_chng
    else:
        pass
    for i in range(len(platforms_list)):
        if platforms_list[i][1] > 700:
            platforms_list[i] = [random.randint(0, 300), random.randint(-10, 0), 100, 10]
            score += 1
    return platforms_list

# zasugerowane internetem ale przerobione na swoje
def check_collisions(rect_list, j):
    global player_y
    global player_x
    global y_ch
    for i in range(len(rect_list)):
        if rect_list[2].colliderect([player_x, player_y + 25, 30, 10]) and jump == False and y_ch > 0:
            j = False
        elif rect_list[i].colliderect([player_x, player_y + 25, 30, 10]) and jump == False and y_ch > 0:
            j = True
    return j


#autorskie
def super_jump_add(rect_list):
    global player_y
    global player_x
    global y_ch
    for i in range(len(rect_list)):
        if rect_list[5].colliderect([player_x, player_y + 25, 30, 10]) and jump == False and y_ch > 0:
            return 1
    return 0


# zasugerowane internetem ale przerobione na własne
while start:
    clock.tick(fps)
    screen.fill(background_color)
    screen.blit(player, (player_x, player_y))
    objects = []
    score_text = font1.render('Score: ' + str(score), True, background_color_2, background_color)
    screen.blit(score_text, (389, 20))
    best_score_text = font1.render('Best Score: ' + str(best_score), True, background_color_2, background_color)
    screen.blit(best_score_text, (350, 650))
    jump_text = font1.render('High Jumps: ' + str(high_jump), True, background_color_2, background_color)
    screen.blit(jump_text, (342, 50))
    if failure:
        screen.fill(background_color)
        failure_text1 = font2.render('You Lost! ', True, background_color_2, background_color)
        screen.blit(failure_text1, (170, 200))
        failure_text2 = font1.render('Your score: ' + str(score), True, background_color_2, background_color)
        screen.blit(failure_text2, (195, 230))
    # autorskie
    else:
        for i in range(len(platforms)):
            if i == 2:
                object = pygame.draw.rect(screen, background_color_3, platforms[i], 3, 1000)
                objects.append(object)
            elif i == 5:
                object = pygame.draw.rect(screen, background_color_3, platforms[i], 0, 1000)
                objects.append(object)
            else:
                object = pygame.draw.rect(screen, background_color_2, platforms[i], 0, 1000)
                objects.append(object)
    # zasugerowane internetem, przerobione
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and failure:
                failure = False
                score = 0
                player_x = 225
                player_y = 550
                jump_last = 0
                high_jump = 2
                platforms = [[200, 600, 75, 10], [100, 650, 100, 10], [350, 550, 100, 10], [200, 500, 50, 10],
                             [250, 450, 100, 10], [100, 350, 50, 10], [150, 200, 75, 10], [250, 250, 100, 10],
                             [200, 100, 100, 10], [50, 150, 50, 10]]
            if event.key == pygame.K_d:
                x_ch = player_s
            if event.key == pygame.K_a:
                x_ch = -player_s
            if event.key == pygame.K_SPACE and high_jump > 0:
                high_jump -= 1
                y_ch = -12
                high_jump_sound = pygame.mixer.music.play()

            if event.key == pygame.K_p:
                x_ch = 0
                y_ch = 0
                gravity = 0


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_ch = 0
            if event.key == pygame.K_a:
                x_ch = 0

            if event.key == pygame.K_u:
                gravity = 0.5

    if super_jump_add(objects) == True:
        high_jump += 1
    jump = check_collisions(objects, jump)
    player_x += x_ch
    if player_y < 700:
        player_y = update_player_y(player_y)
    else:
        failure = True
        y_ch = 0
        x_ch = 0


    platforms = update_platforms(platforms, player_y, y_ch)
    if player_x < -20:
        player_x = -60
    elif player_x > 500:
        player_x = 330
    # autorskie
    if best_score < score:
        best_score = score
        file = open("best_score.txt", "w")
        file.write(str(best_score))
        file.close()
    if score > last_score + 15:
        last_score = score
        background_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        background_color_2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        background_color_3 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        while background_color == background_color_2 == background_color_3 and background_color != red:
            background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            background_color_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pygame.display.flip()
pygame.quit()
file.close()