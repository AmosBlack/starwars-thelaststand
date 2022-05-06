import pygame
import random
import math
from pygame import mixer
import time
# initialize
elap_min = 0
elap_time = 0
pygame.init()
from threading import Timer

tutorial = False
movement = True
game_run = True
# screen
score_file = open('scores.txt', 'a')
xiz = 0
xi = 0
y1 = 45
y2 = 55
y3 = 75
screen = pygame.display.set_mode((800, 700))
rank = ''

# bgmusic
mixer.music.load('background.mp3')
mixer.music.play(-1)

to_play = True

# title&icon
pygame.display.set_caption("Star Wars : The Last Stand")
icon = pygame.image.load("sw_logo.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("background_sw.png")

# player
playerImg = pygame.image.load('basic.png')
player_x = 350
player_y = 480
changex_player = 0
chew = pygame.image.load('chew.png')
#for ensuring ammo works n changes only once post ava change
det1 = False
det2 = False
det3 = False
ship = 'basic'
ammo_max = 5
ship_v = 0.8
# enemy
enemy_img = []
enemy_x = []
enemy_y = []
changey_enemy = []
changex_enemy = []
enemy_num = 6
enemy_bomber_index = []
enemy_bomber_is = []
enemy_laser = pygame.image.load('laser_bomber.png')
#boss

boss = pygame.image.load('dn_boss.png')
boss = pygame.transform.scale(boss,(240,240))
# bullet
bullet_img = pygame.image.load('laser_basic.png')
bullet_x = 0
bullet_y = 480
changex_bullet = 0
changey_bullet = 1
bullet_firing = False
ammo = 5
out_of_ammo = False
bullet_noise = mixer.Sound('laser.wav')

tut_font = pygame.font.Font("STARWARS.ttf", 16)
move = tut_font.render('    Movement : Arrow Keys -- Shooting : Spacebar -- Threats : Empire T-Fighters', True,
                       (255, 255, 255))
comms = tut_font.render('               MusicToggle:M  -  Quit:Q  -  Replay:R  -  TutorialDisplay:T', True,
                        (255, 255, 255))
ammo_timer = 0
#user-info
info_font = pygame.font.Font('STARWARS.ttf',24)
# score_value
score_val = 0
font = pygame.font.Font('Starjedi.ttf', 32)
font_end = pygame.font.Font('Starjout.ttf', 80)

def bomber_sel(index):
    enemy_x.append(random.randint(5, 736))
    enemy_y.append(random.randint(50, 150))
    changex_enemy.append(0.4)
    bomber_rng = random.randint(1, 8)
    if (bomber_rng == 1):
        enemy_img.append(pygame.image.load("tie_bomber.png"))
        enemy_bomber_index.append(i)
        changey_enemy.append(40)
        changex_enemy.append(0.7)
        enemy_bomber_is.append(True)
        return True

    else:
        enemy_img.append(pygame.image.load("tie.png"))
        changey_enemy.append(30)
        enemy_bomber_is.append(False)
        return False

for i in range(enemy_num):
    bomber_sel(i)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def bullet_fire(x, y):
    global bullet_firing
    bullet_firing = True
    screen.blit(bullet_img, (x + 32.5, y + 10))


score_x = 5
score_y = 0


def is_collis(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))

    if distance <= 30:

        print(distance)
        return True
    else:
        return False


ammo_sign = "Ammo:"


def show_score(x, y, out_of_ammo):
    if out_of_ammo:
        ammo_txt = ammo_sign + str((round(ammo_timer, 1) * ammo_max))
    else:
        ammo_txt = 'Ammo:' + str(ammo)
    score = font.render(" Score:" + str(score_val) + "       Star Wars        " + ammo_txt, True, (255, 232, 31))
    screen.blit(score, (x, y))


def bomber_shoot():
    for index in range(len(enemy_bomber_index)):
        bomber_shoot = random.randint(1, 3000)
        if (bomber_shoot == 3000):
            bomber_kill = True
        else:
            bomber_kill = False


def game_over(x, y, x1, y1):
    global rank
    if (score_val < 15):
        rank = "Rookie"
    elif (score_val >= 15 and score_val < 30):
        rank = 'Novice'
    elif (score_val >= 30 and score_val < 50):
        rank = 'Expert'
    elif (score_val >= 50):
        rank = 'Legend'

    over = font_end.render('game over', True, (255, 255, 255))
    ranktxt = font_end.render(rank, True, (255, 255, 255))
    screen.blit(over, (x, y))
    screen.blit(ranktxt, (x1, y1))

bombers = 0
# gameloop
run = True

count_down_timer = 0

alpha_lim = 0.001
allow_shooting = True
# THE BIG LOOP THING
t_begin = time.time()
boss_txt = info_font.render('BOSS',True,(200.8, 20, 20))
while run:

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (255, 232, 31), pygame.Rect(0, 0, 800, 610), 2,5)
    # loading-boss
    screen.blit(boss, (260, -48))
    pygame.draw.rect(screen, (255,232,255), pygame.Rect(0, 620, 800, 60), 2,5)
    count_down_timer += 0.0005
    if tutorial or count_down_timer <= 1.2:
        screen.blit(move, (28, y1))
        screen.blit(comms, (28, y1 + 20))

    #no of bombers




    # player avatars

    if score_val >= 15 and score_val < 30:
        playerImg = pygame.image.load('cyclo.png')
        ship = 'cyclo'
        if not det1:
            det1 = True
            bullet_img = pygame.image.load('laser.png')
            ammo = 8
            ammo_max = 8
            ship_v = 0.7

    elif score_val >= 30 and score_val < 31:
        playerImg = pygame.image.load('mill.png')
        ship = 'mill'
        bullet_img = pygame.image.load('laser_mill.png')
        if not det2:
            det2 = True
            ammo = 15
            ammo_max = 15
            ship_v = 0.8


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # make speed variable for various ships.....
            if event.key == pygame.K_LEFT and movement:
                changex_player = -ship_v
            if event.key == pygame.K_RIGHT and movement:
                changex_player = ship_v
            if event.key == pygame.K_SPACE:
                if not bullet_firing and allow_shooting and not out_of_ammo:
                    bullet_x = player_x
                    if to_play:
                        bullet_noise.play()
                    bullet_fire(bullet_x, bullet_y)
                    ammo -= 1
            if event.key == pygame.K_m:
                if to_play:
                    to_play = False
                    mixer.music.stop()


                else:
                    to_play = True
                    mixer.music.play(-1)
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_r:
                import sys

                print("argv was", sys.argv)
                print("sys.executable was", sys.executable)
                print("restart now")

                import os

                os.execv(sys.executable, ['python'] + sys.argv)
            if event.key == pygame.K_t:
                tutorial = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changex_player = 0
            if event.key == pygame.K_t:
                tutorial = False



    #enemy_bombers


    # enemy moves
    score_upd = False
    for i in range(enemy_num):
        # game over

        if (enemy_y[i] > 440):
            for j in range(enemy_num):
                enemy_y[j] = 2000

            game_over(150, 200, 250, 280)
            mixer.music.fadeout(2000)
            allow_shooting = False
            player_x = 350
            movement = False
            game_run = False
            break

        enemy_x[i] += changex_enemy[i]
        if enemy_x[i] <= 0:
            enemy_y[i] += changey_enemy[i]
            enemy_x[i] = 0
            if enemy_bomber_is[i]:
                changex_enemy[i] = 0.7
            else:
                changex_enemy[i] = 0.4

        elif enemy_x[i] >= 736:
            enemy_y[i] += changey_enemy[i]
            enemy_x[i] = 736
            if enemy_bomber_is[i]:
                changex_enemy[i] = -0.7
            else:
                changex_enemy[i] = -0.4

        # is_collis
        collis = is_collis(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collis:
            if enemy_bomber_is[i]:
                score_val += 2
            else:
                score_val += 1

            bullet_y = 480

            explosion = mixer.Sound('crash.wav')
            explosion.set_volume(0.1)
            explosion.fadeout(1000)
            if to_play:
                explosion.play()
            bullet_firing = False
            print(score_val)
            enemy_x[i] = random.randint(5, 736)
            enemy_y[i] = random.randint(50, 150)

            if not enemy_bomber_is[i]:

                bomber_rng_reset = random.randint(1, 5)
                print(str(bomber_rng_reset) + "rng")
                if bomber_rng_reset == 1:
                    enemy_bomber_is[i] = True
                    enemy_img[i] = pygame.image.load('tie_bomber.png')
                    print("CHANGE")
                else:
                    enemy_bomber_is[i] = False
                    enemy_img[i] = pygame.image.load('tie.png')
            else:
                bomber_rng_reset = random.randint(1, 8)
                print(str(bomber_rng_reset) + "rng" + 'bomb')
                if bomber_rng_reset == 1:
                    enemy_bomber_is[i] = False
                    enemy_img[i] = pygame.image.load('tie.png')

        enemy(enemy_x[i], enemy_y[i], i)

    if player_x <= 0:
        player_x = 0
    elif player_x >= 704:
        player_x = 704

    # keystroke mechanics

    # bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_firing = False
    if bullet_firing is True:
        bullet_fire(bullet_x, bullet_y)
        bullet_y -= changey_bullet
    if ammo == 0:
        out_of_ammo = True
    if out_of_ammo:

        ammo_timer += 0.0008
        if (ammo_timer >= 1):
            out_of_ammo = False
            ammo_timer = 0
            if ship == 'basic':
                ammo = 5
            elif ship == 'cyclo':
                ammo = 8
            elif ship == 'mill':
                ammo = 15
            elif ship == 'star_dn':
                ammo = 30

    player_x += changex_player
    enemy_x += changex_enemy
    bomber_shoot()
    show_score(score_x, score_y, out_of_ammo)
    player(player_x, player_y)
#   info-bar (0, 0, 800, 610)
    if game_run:
        elap_time = round(time.time() - t_begin, 1)


    else :
        elap_time =str(elap_time)

    info = info_font.render('Ship: ' + ship.upper()  + " " +'AmmoCap: ' + str(ammo_max) +" " + "Enemies: " + str(enemy_num)  + " " + "Time(s): "  + str(elap_time)  ,True,(255,255,255))
    hp = info_font.render('HP           Tension',True,(255,255,255))
    screen.blit(info,(70,650))
    screen.blit(chew,(19,630))
    screen.blit(hp,(70,625))
    pygame.draw.circle(screen, (255, 234, 0),
                      [35, 648], 25, 3)
    #hp
    threat_lvl = pygame.draw.polygon(screen,(50,255,50),[(760,625),(740,670),(780,670)])
    health_in = pygame.draw.rect(screen,(255,0,0),pygame.Rect(120,625,100,20),0,6)
    health_out = pygame.draw.rect(screen,(0,200,0),pygame.Rect(120,625,100,20),0,6)
    #tension
    tens_in = pygame.draw.rect(screen,(0,0,150),pygame.Rect(350,625,100,20),0,6)
    tens_out = pygame.draw.rect(screen,(254, 150, 0),pygame.Rect(350,625,100,20),0,6)
    #boss-hp
    boss_hp_in = pygame.draw.rect(screen,(178, 127, 127),pygame.Rect(530,625,200,20),0,6)
    boss_hp_in = pygame.draw.rect(screen,(200.8, 20, 20),pygame.Rect(530,625,150,20),0,6)
    screen.blit(boss_txt,(460,625))
    #pygame.draw.lines(screen,(255, 232, 31),(150,630),(600,630))


    #lvling



    pygame.display.update()
    pygame.display.flip()