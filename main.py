import pygame
from random import randint
from sys import exit

def szukanie(T,x):
    for i in range(len(T)):
        if T[i] == x:
            return True
    return False


pygame.init()
pygame.display.set_caption('Flappy Bird')

screen = pygame.display.set_mode((1600, 800))  # top pipe: -1600 bottom pipe:
clock = pygame.time.Clock()

bird_surf = pygame.image.load('images\Flappy_bird.png').convert_alpha()
bird_rect = bird_surf.get_rect(midbottom=(100, 500))
bird_gravity = 0
pygame.display.set_icon(bird_surf)

sky_surf = pygame.image.load('images\Sky.png').convert()
sky_surf_x = 0

ground_surf = pygame.image.load('images\Ground.png').convert()
ground_surf_x = 0
far = 10000

pipe1_down = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe1_down_rect = pipe1_down.get_rect(midtop=(far, far))
pipe1_up = pygame.image.load('images\pipe_down_1.png')
pipe1_up_rect = pipe1_up.get_rect(midbottom=(far, far))
pipe1_act = False

pipe2_down = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe2_down_rect = pipe2_down.get_rect(midtop=(far, far))
pipe2_up = pygame.image.load('images\pipe_down_1.png')
pipe2_up_rect = pipe2_up.get_rect(midbottom=(far, far))
pipe2_act = False

pipe3_down = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe3_down_rect = pipe3_down.get_rect(midtop=(far, far))
pipe3_up = pygame.image.load('images\pipe_down_1.png')
pipe3_up_rect = pipe3_up.get_rect(midbottom=(far, far))
pipe3_act = False

pipe4_down = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe4_down_rect = pipe4_down.get_rect(midtop=(far, far))
pipe4_up = pygame.image.load('images\pipe_down_1.png')
pipe4_up_rect = pipe4_up.get_rect(midbottom=(far, far))
pipe4_act = False

pipe5_down = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe5_down_rect = pipe5_down.get_rect(midtop=(far, far))
pipe5_up = pygame.image.load('images\pipe_down_1.png')
pipe5_up_rect = pipe5_up.get_rect(midbottom=(far, far))
pipe5_act = False

pipe6_down = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe6_down_rect = pipe6_down.get_rect(midtop=(far, far))
pipe6_up = pygame.image.load('images\pipe_down_1.png').convert_alpha()
pipe6_up_rect = pipe6_up.get_rect(midbottom = (far, far))
pipe6_act = False

# full pipe7
pipe7_down_1 = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe7_down_rect_1 = pipe7_down_1.get_rect(midtop=(far, far))
pipe7_up_1 = pygame.image.load('images\pipe_down_1.png').convert_alpha()
pipe7_up_rect_1 = pipe7_up_1.get_rect(midbottom = (far, far))

pipe7_down_2 = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe7_down_rect_2 = pipe7_down_2.get_rect(midtop=(far, far))
pipe7_up_2 = pygame.image.load('images\pipe_down_1.png').convert_alpha()
pipe7_up_rect_2 = pipe7_up_2.get_rect(midbottom = (far, far))

pipe7_down_3 = pygame.image.load('images\pipe_up_1.png').convert_alpha()
pipe7_down_rect_3 = pipe7_down_3.get_rect(midtop=(far, far))
pipe7_up_3 = pygame.image.load('images\pipe_down_1.png').convert_alpha()
pipe7_up_rect_3 = pipe7_up_3.get_rect(midbottom = (far, far))
pipe7_act = False
# []

score = 0
minecraft_font = pygame.font.Font('fonts\minecraft.ttf', 50)
minecraft_font2 = pygame.font.Font('fonts\minecraft.ttf', 25)
score_surf = minecraft_font.render(f'Score: {score}', True, 'black')
score_rect = score_surf.get_rect(midbottom = (800,200))

high_score = 0
high_score_surf = minecraft_font2.render(f'High Score: {high_score}', True, 'black')
high_score_rect = high_score_surf.get_rect(midbottom = (800,250))

game_over_surf = minecraft_font.render('GAME OVER', True, 'black')
game_over_rect = game_over_surf.get_rect(midbottom = (800, 400))

pipe_rand = randint(1,6)
pipe_x = 199
Act_pipes = []
trimp_pipe = False
game_active = False
first_round = True


while True:
    if game_active == True:
        for event in pygame.event.get():
            # quiting
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # skakanie
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_gravity = -10
        # chodzenie tła
        sky_surf_x -= 0.5
        if sky_surf_x <= -1600: sky_surf_x = 0
        screen.blit(sky_surf, (sky_surf_x, 0))
        # poruszanie sie birda
        bird_gravity += 0.7
        bird_rect.y += bird_gravity
        if bird_rect.bottom >= 750: bird_rect.bottom = 750
        if bird_rect.bottom <= -100: bird_rect.bottom = -100
        screen.blit(bird_surf, bird_rect)

        # postawianie pipow
        if pipe_x == 199:
            if pipe_rand == 1 and pipe1_act == False:
                pipe1_up_rect.x = 1600
                pipe1_up_rect.y = -1500         # -1600 + X
                pipe1_down_rect.x = 1600
                pipe1_down_rect.y = 300     # 800 - X
                pipe1_act = True
                Act_pipes.append(1)
            elif pipe_rand == 2 and pipe2_act == False:
                pipe2_up_rect.x = 1600
                pipe2_up_rect.y = -1400
                pipe2_down_rect.x = 1600
                pipe2_down_rect.y = 400
                pipe2_act = True
                Act_pipes.append(2)
            elif pipe_rand == 3 and pipe3_act == False:
                pipe3_up_rect.x = 1600
                pipe3_up_rect.y = -1300
                pipe3_down_rect.x = 1600
                pipe3_down_rect.y = 500
                pipe3_act = True
                Act_pipes.append(3)
            elif pipe_rand == 4 and pipe4_act == False:
                pipe4_up_rect.x = 1600
                pipe4_up_rect.y = -1200
                pipe4_down_rect.x = 1600
                pipe4_down_rect.y = 600
                pipe4_act = True
                Act_pipes.append(4)
            elif pipe_rand == 5 and pipe5_act == False:
                pipe5_up_rect.x = 1600
                pipe5_up_rect.y = -1100
                pipe5_down_rect.x = 1600
                pipe5_down_rect.y = 700
                pipe5_act = True
                Act_pipes.append(5)
            elif pipe_rand == 6 and pipe6_act == False:
                pipe6_up_rect.x = 1600
                pipe6_up_rect.y = -1050
                pipe6_down_rect.x = 1600
                pipe6_down_rect.y = 740
                pipe6_act = True
                Act_pipes.append(6)
            elif pipe_rand == 7 and pipe7_act == False:
                pipe7_up_rect_1.x = 1600
                pipe7_up_rect_1.y = -1300
                pipe7_down_rect_1.x = 1600
                pipe7_down_rect_1.y = 500
                pipe7_up_rect_2.x = 1650
                pipe7_up_rect_2.y = -1300
                pipe7_down_rect_2.x = 1650
                pipe7_down_rect_2.y = 500
                pipe7_up_rect_3.x = 1700
                pipe7_up_rect_3.y = -1300
                pipe7_down_rect_3.x = 1700
                pipe7_down_rect_3.y = 500
                pipe7_act = True
                trimp_pipe = True
                Act_pipes.append(7)

        #r esetowanie + przedluzanie pipow
        if pipe_x >= 200:
            pipe_x = 0
        if trimp_pipe == True:
            pipe_x -= 250
            trimp_pipe = False
        pipe_x += 1

        # losowanie pipa
        if pipe_x == 199:
            pipe_rand = randint(1,7)
            if pipe_x == 199:
                while True:
                    if szukanie(Act_pipes,pipe_rand) == True:
                        pipe_rand = randint(1,7)
                    else:
                        break
        # usuwanie pipa
        if pipe1_down_rect.x <= -100 and pipe1_act == True:
            Act_pipes.remove(1)
            pipe1_act = False
        elif pipe2_down_rect.x <= -100 and pipe2_act == True:
            Act_pipes.remove(2)
            pipe2_act = False
        elif pipe3_down_rect.x <= -100 and pipe3_act == True:
            Act_pipes.remove(3)
            pipe3_act = False
        elif pipe4_down_rect.x <= -100 and pipe4_act == True:
            Act_pipes.remove(4)
            pipe4_act = False
        elif pipe5_down_rect.x <= -100 and pipe5_act == True:
            Act_pipes.remove(5)
            pipe5_act = False
        elif pipe6_down_rect.x <= -100 and pipe6_act == True:
            Act_pipes.remove(6)
            pipe6_act = False
        elif pipe7_down_rect_3.x <= -100 and pipe7_act == True:
            Act_pipes.remove(7)
            pipe7_act = False

        # score
        if pipe1_down_rect.x == 100:
            score += 1
        elif pipe2_down_rect.x == 100:
            score += 1
        elif pipe3_down_rect.x == 100:
            score += 1
        elif pipe4_down_rect.x == 100:
            score += 1
        elif pipe5_down_rect.x == 100:
            score += 1
        elif pipe6_down_rect.x == 100:
            score += 1
        elif pipe7_down_rect_3.x == 100:
            score += 1

        # porusznie sie pipow
        pipe1_down_rect.x -= 2
        pipe1_up_rect.x -= 2

        screen.blit(pipe1_up, (pipe1_up_rect))
        screen.blit(pipe1_down, (pipe1_down_rect))

        pipe2_down_rect.x -= 2
        pipe2_up_rect.x -= 2

        screen.blit(pipe2_up, (pipe2_up_rect))
        screen.blit(pipe2_down, (pipe2_down_rect))

        pipe3_down_rect.x -= 2
        pipe3_up_rect.x -= 2

        screen.blit(pipe3_up, (pipe3_up_rect))
        screen.blit(pipe3_down, (pipe3_down_rect))

        pipe4_down_rect.x -= 2
        pipe4_up_rect.x -= 2

        screen.blit(pipe4_up, (pipe4_up_rect))
        screen.blit(pipe4_down, (pipe4_down_rect))

        pipe5_down_rect.x -= 2
        pipe5_up_rect.x -= 2

        screen.blit(pipe5_up, (pipe5_up_rect))
        screen.blit(pipe5_down, (pipe5_down_rect))

        pipe6_down_rect.x -= 2
        pipe6_up_rect.x -= 2

        screen.blit(pipe6_up, (pipe6_up_rect))
        screen.blit(pipe6_down, (pipe6_down_rect))

        pipe7_down_rect_1.x -= 2
        pipe7_up_rect_1.x -= 2
        pipe7_down_rect_2.x -= 2
        pipe7_up_rect_2.x -= 2
        pipe7_down_rect_3.x -= 2
        pipe7_up_rect_3.x -= 2

        screen.blit(pipe7_up_1, (pipe7_up_rect_1))
        screen.blit(pipe7_down_1, (pipe7_down_rect_1))
        screen.blit(pipe7_up_2, (pipe7_up_rect_2))
        screen.blit(pipe7_down_2, (pipe7_down_rect_2))
        screen.blit(pipe7_up_3, (pipe7_up_rect_3))
        screen.blit(pipe7_down_3, (pipe7_down_rect_3))
        # porusznie sie tla
        ground_surf_x -= 2
        if ground_surf_x <= -2144: ground_surf_x = -4
        screen.blit(ground_surf, (ground_surf_x, 750))

        # Score i high score
        score_surf = minecraft_font.render(f'Score: {score}', True, 'black')
        screen.blit(score_surf, (score_rect))

        high_score_surf = minecraft_font2.render(f'High Score: {high_score}', True, 'black')
        screen.blit(high_score_surf, (high_score_rect))
        if score > high_score:
            high_score = score

        #Game over on
        first_round = False

        #game over
        if bird_rect.colliderect(pipe1_up_rect):
            game_active = False
        if bird_rect.colliderect(pipe1_down_rect):
            game_active = False
        if bird_rect.colliderect(pipe2_up_rect):
            game_active = False
        if bird_rect.colliderect(pipe2_down_rect):
            game_active = False
        if bird_rect.colliderect(pipe3_up_rect):
            game_active = False
        if bird_rect.colliderect(pipe3_down_rect):
            game_active = False
        if bird_rect.colliderect(pipe4_up_rect):
            game_active = False
        if bird_rect.colliderect(pipe4_down_rect):
            game_active = False
        if bird_rect.colliderect(pipe5_up_rect):
            game_active = False
        if bird_rect.colliderect(pipe5_down_rect):
            game_active = False
        if bird_rect.colliderect(pipe6_up_rect):
            game_active = False
        if bird_rect.colliderect(pipe6_down_rect):
            game_active = False
        if bird_rect.colliderect(pipe7_up_rect_1):
            game_active = False
        if bird_rect.colliderect(pipe7_down_rect_1):
            game_active = False
        if bird_rect.colliderect(pipe7_up_rect_2):
            game_active = False
        if bird_rect.colliderect(pipe7_down_rect_2):
            game_active = False
        if bird_rect.colliderect(pipe7_up_rect_3):
            game_active = False
        if bird_rect.colliderect(pipe7_down_rect_3):
            game_active = False
        if bird_rect.y == 700:
            game_active = False

        # refresh i FPS
        pygame.display.update()
        clock.tick(60)
    elif game_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_rect.y = 500
                    score = 0
                    pipe1_up_rect.x = 10000
                    pipe1_down_rect.x = 10000
                    pipe2_up_rect.x = 10000
                    pipe2_down_rect.x = 10000
                    pipe3_up_rect.x = 10000
                    pipe3_down_rect.x = 10000
                    pipe4_up_rect.x = 10000
                    pipe4_down_rect.x = 10000
                    pipe5_up_rect.x = 10000
                    pipe5_down_rect.x = 10000
                    pipe6_up_rect.x = 10000
                    pipe6_down_rect.x = 10000
                    pipe7_up_rect_1.x = 10000
                    pipe7_down_rect_1.x = 10000
                    pipe7_up_rect_2.x = 10000
                    pipe7_down_rect_2.x = 10000
                    pipe7_up_rect_3.x = 10000
                    pipe7_down_rect_3.x = 10000
                    pipe1_act = False
                    pipe2_act = False
                    pipe3_act = False
                    pipe4_act = False
                    pipe5_act = False
                    pipe6_act = False
                    pipe7_act = False
                    bird_gravity = -10
                    game_active = True

        for i in range(len(Act_pipes)):
            Act_pipes.remove(Act_pipes[0])

        screen.blit(sky_surf, (sky_surf_x, 0))

        screen.blit(pipe1_up, (pipe1_up_rect))
        screen.blit(pipe1_down, (pipe1_down_rect))

        screen.blit(pipe2_up, (pipe2_up_rect))
        screen.blit(pipe2_down, (pipe2_down_rect))

        screen.blit(pipe3_up, (pipe3_up_rect))
        screen.blit(pipe3_down, (pipe3_down_rect))

        screen.blit(pipe4_up, (pipe4_up_rect))
        screen.blit(pipe4_down, (pipe4_down_rect))

        screen.blit(pipe5_up, (pipe5_up_rect))
        screen.blit(pipe5_down, (pipe5_down_rect))

        screen.blit(pipe6_up, (pipe6_up_rect))
        screen.blit(pipe6_down, (pipe6_down_rect))

        screen.blit(pipe7_up_1, (pipe7_up_rect_1))
        screen.blit(pipe7_down_1, (pipe7_down_rect_1))
        screen.blit(pipe7_up_2, (pipe7_up_rect_2))
        screen.blit(pipe7_down_2, (pipe7_down_rect_2))
        screen.blit(pipe7_up_3, (pipe7_up_rect_3))
        screen.blit(pipe7_down_3, (pipe7_down_rect_3))

        screen.blit(ground_surf, (ground_surf_x, 750))
        screen.blit(score_surf, (score_rect))
        screen.blit(high_score_surf, (high_score_rect))
        screen.blit(bird_surf, bird_rect)

        if first_round == False:
            screen.blit(game_over_surf,(game_over_rect))

        pygame.display.update()
        clock.tick(60)