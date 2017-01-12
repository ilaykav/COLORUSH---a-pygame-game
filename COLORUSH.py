#COLORUSH -  a game for kids who want to learn the colors and the relatives between them
import os

import pygame
import math
from pygame.locals import *
from sys import exit
import random
total_score = 0
winmessage = "WIN = 25"
setlose2 = True
youwin, youlose= False, False
zvikiCounter = 0
pause = False
screen = 0

def update_presents():
    global total_score, setlose2, youlose, youwin, zvikiCounter, screen, fillbox2, fillbox, i, rushsize, spacebar, zviki_has_been_found, counter, text, font
    global bar1_x, bar1_y, circle_x, circle_y, bar1_move, bar2_move, speed_x, speed_circ, speed_y, clock, clock_presents, index_of_color, right, left, presents, balls
    global index_of_color2, try1, winmessage, pause
    if len(presents)!=0:
        for ex_present in presents:
            if ex_present.color!=(255,255,255):
                if youlose and setlose2:
                    ex_present.set_lose()
                    setlose2 = False
                if ex_present.color[0] == 0 and ex_present.color[1] == 0 and ex_present.color[2] == 0:
                    presents.remove(ex_present)

                ex_present.update()
                rt = pygame.Surface((50,50))
                rectpresent = rt.convert()
                rectpresent.fill(ex_present.color)
                #print bar1_y
                if not youlose and not youwin and ex_present.y < bar1_y and ex_present.y+50 > bar1_y  and bar1_x-50 < ex_present.x and bar1_x +50 > ex_present.x:
                    if realcolor == [100, 100, 100]:
                        presents.remove(ex_present)
                        try:
                            presents.remove(ex_present)
                        except:
                            ValueError
                        if not ex_present.zviki:
                            if not youlose:
                                total_score+=1
                    if realcolor[0] == ex_present.color[0] and realcolor[1] == ex_present.color[1] and realcolor[2] == ex_present.color[2]:
                        #print(realcolor, ex_present.color)
                        try:
                            presents.remove(ex_present)
                        except:
                            ValueError
                        if not ex_present.zviki:
                            if not youlose:
                               total_score+=1
                    if ex_present.zviki == True:
                        try:
                            presents.remove(ex_present)
                        except:
                            ValueError
                        zviki_has_been_found = True
                        zvikiCounter = 1

            screen.blit(rectpresent,(ex_present.x,ex_present.y+i))

def update_death_balls():
    if len(balls)!=0:
        for ball in balls:
            circ_sur = pygame.Surface((30,30))
            #bgdtile = 'background.gif'
            circ = pygame.draw.circle(circ_sur,(220, 0, 20),(15,15),15)
            circ2 = pygame.draw.circle(circ_sur,(0, 0, 0),(15,15),12)
            circle = circ_sur.convert()
            circle.set_colorkey((0,0,0))
            screen.blit(circle,(ball.x,ball.y+i))
            ball.update()

            global youlose
            if not youlose and not youwin and ball.y < bar1_y and ball.y+30 > bar1_y  and bar1_x-50 < ball.x and bar1_x +50 > ball.x:
                balls.remove(ball)
                youlose =  True

def seem_impresive():
     bla = 1
     bla2 = random.randint(1, 1000000000)
     for i in range(1, 10):
        bla += math.pow(10, i) * random.randint(0, 1)
     print bin(bla2*bla2), bla, bla+bla2

def draw_pause_menu():
    
    pause_box = pygame.Surface((500,300))
    load_shape(screen, (50, 50, 50), 75, 100, pause_box)

    #load the texts of the pause menu
    load_text(screen, (255, 255, 255), font, 327, 320, "+   =")

    #load pause menu object
    pause_box = pygame.Surface((50,50))
    load_shape(screen, (100,100,100), 400, 245, pause_box)

    #load pause menu object
    pause_box = pygame.Surface((20,20))
    load_shapes(screen, ((0 ,0, 255), (0, 255, 0), (0, 255, 255)), (300, 330, 350, 330, 400, 330), pause_box)

    #draws the circle
    circ_sur = pygame.Surface((30,30))
    circ = pygame.draw.circle(circ_sur,(220, 0, 20),(15,15),15)
    circ2 = pygame.draw.circle(circ_sur,(0, 0, 0),(15,15),13)
    circle = circ_sur.convert()
    circle.set_colorkey((0,0,0))
    screen.blit(circle,(205,255))

    #load the texts of the pause menu
    font2 = pygame.font.SysFont("calibri",25)
    colors1 = [(100, 255, 100), (100, 255, 100), (255,100,100), (100,100,255), (100,255,100), (255,100,100), (100,100,255), (255,100,100), (100,100,255), (255,255,255)]
    xys = [80, 225, 80, 355, 270, 100, 80, 125, 80, 150, 80, 175, 80, 200, 80, 305, 80, 330, 80, 375]
    texts = ["Hit R to restart", "To change:                   A      D      Your color", "Game Rules:", "Reach to 25 points, earn points by selecting ", "presents- you can only select presents while the", "present's color and your color are the same!", "Avoid the red loops! Take the gray presents!", "Your color is the mix of the colors in the", "top-left corner:", "Hit the spacebar to change your color to white"]
    load_texts(screen, colors1, font2, xys, texts)

def load_shapes(screen, colors, xys, surface):
    converted_surface = surface.convert()
    for i in range (0, len(colors)):
        converted_surface.fill(colors[i])
        screen.blit(converted_surface, (xys[i*2], xys[i*2+1]))

def load_shape(screen, color, x, y, surface):
    converted_surface = surface.convert()
    converted_surface.fill(color)
    screen.blit(converted_surface,(x,y))

def restart():
    global total_score, setlose2, youlose, youwin, zvikiCounter, screen, fillbox2, fillbox, i, rushsize, spacebar, zviki_has_been_found, counter, text, font
    global bar1_x, bar1_y, circle_x, circle_y, bar1_move, bar2_move, speed_x, speed_circ, speed_y, clock, clock_presents, index_of_color, right, left, presents, balls
    global index_of_color2, try1, winmessage, pause
    winmessage = "WIN = 25"
    total_score= 0
    setlose2 = True
    youwin, youlose= False, False
    zvikiCounter = 0
    pygame.init()
    screen=pygame.display.set_mode((640,480),0,32)
    pygame.display.set_caption("COLORUSH")
    fillbox= (255, 0, 0)
    fillbox2= (255, 0, 0)
    i =0
    rushsize = 20
    spacebar = False
    zviki_has_been_found =False

    counter, text = 60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    back = pygame.Surface((640,480))
    background = back.convert()
    background.fill((0,0,0))
    bar = pygame.Surface((50,10))
    bar1 = bar.convert()
    bar1.fill((0,0,255))
    bar1_x=300.
    bar1_y=440.
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0. , 0.
    speed_x, speed_y, speed_circ = 250., 250., 450.
    clock = pygame.time.Clock()
    clock_presents = pygame.time.Clock()
    font = pygame.font.SysFont("calibri",40)
    index_of_color = 0
    right = False
    left = False
    del presents[:]
    del balls[:]
    index_of_color2 = 0
    try1 = 0

def load_text(screen, color, font, x, y, text):
    loaded_text = font.render((text), True, color)
    screen.blit(loaded_text, (x, y))

def load_texts(screen, colors, font, xys, texts):
    for i in range (0, len(texts)):
        loaded_text = font.render((texts[i]), True, colors[i])
        screen.blit(loaded_text, (xys[i*2], xys[i*2+1]))

def game_handler():
    global total_score, setlose2, youlose, youwin, zvikiCounter, screen, fillbox2, fillbox, i, rushsize, spacebar, zviki_has_been_found, counter, text, font
    global bar1_x, bar1_y, circle_x, circle_y, bar1_move, bar2_move, speed_x, speed_circ, speed_y, clock, clock_presents, index_of_color, right, left, presents, balls
    global index_of_color2, try1, winmessage, pause
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_r:
                    restart()
                if event.key == K_p:
                    pause = True
            if False == youwin and False == youlose:
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    clock.tick(60)
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        spacebar = True
                    if event.key == K_r:
                        restart()
                    elif event.key == K_d:
                        index_of_color2 = (index_of_color2+1)%3
                        if index_of_color2 == 0:
                            fillbox2 = (255, 0, 0)
                        elif index_of_color2 == 1:
                            fillbox2 = (0, 255,0)
                        elif index_of_color2 == 2:
                            fillbox2 =(0, 0, 255)
                    if event.key == K_a:
                        index_of_color = (index_of_color+1)%3
                        if index_of_color == 0:
                            fillbox = (255, 0, 0)
                        elif index_of_color == 1:
                            fillbox = (0, 255, 0)
                        elif index_of_color == 2:
                            fillbox =(0, 0, 255)
                    if event.key == K_LEFT:
                        try:
                            bar1_move = -ai_speed
                        except:
                            print("except")
                            UnboundLocalError
                        left = True
                    elif event.key == K_RIGHT:
                        try:
                            bar1_move = ai_speed
                        except:
                            print("except")
                            UnboundLocalError
                        right = True
                elif event.type == KEYUP:
                    if event.key == K_SPACE:
                        spacebar = False
                    if event.key == K_LEFT:
                        bar1_move = 0.
                        if right:
                            try:
                                bar1_move = ai_speed
                            except:
                                print("except")
                                UnboundLocalError
                        left = False
                    elif event.key == K_RIGHT:
                        bar1_move = 0.
                        if left:
                            try:
                                bar1_move = -ai_speed
                            except:
                                print("except")
                                UnboundLocalError
                        right = False

        if bar1_x < 0:
            if bar1_move<0:
                bar1_move = 0

        if bar1_x > 585:
            if bar1_move>0:
                bar1_move = 0

        bar1_x += bar1_move

        #print (try1)
        # movement of circle
        time_passed = clock.tick(30)
        i =0
        #seem_impresive()
        mom = (random.randint(0, 1000))
        chance = 33

        if zviki_has_been_found:
            chance = 100

        if mom < chance:
            i+=1
            presents.append(present())

        if not zviki_has_been_found and mom < chance-28:#take the chance whether to make a death ball or noy
            # including if there is colorush
            i+=1
            balls.append(death_ball())

        time_sec = time_passed / 1000.0
        print((time_passed))
        print(time_sec)
        ai_speed = speed_circ * 0.034####################

        if total_score == 25:#checks win-case
            youwin = True

        if counter == 0:#checks lose-case: if the timer reaches the 0
            youlose = True

        update_screen(i)

        while pause: #makes the pause menu and freezes the game
            draw_pause_menu() #I think it's pretty clear...
            for event in pygame.event.get():#gets events from the user in the pause 'mode'
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        pause = False
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_r:
                        restart()

            pygame.display.update()

        pygame.display.update()

def prepare_game_workspace():
    global screen
    screen = pygame.display.set_mode((640,480),0,32)
    pygame.init()
    pygame.display.set_caption("COLORUSH")
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    file = os.path.join(main_dir, 'icon.png')
    surfaceicon = pygame.image.load(file)
    icon = pygame.transform.scale(surfaceicon, (32, 32))
    pygame.display.set_icon(icon)

class death_ball():
    speed = random.randint(5, 15)
    x = 0
    y = 20
    rectpresent = 0


    def __init__(self):
        self.speed = random.randint(5, 12)#random.randint(5, 20)
        self.x = random.randint(0, 600)

    def update(self):
        self.y +=self.speed

class present():
    zviki = False
    speed = random.randint(3, 10)
    x = 0
    y = 20
    rectpresent = 0

    def __init__(self):
        global zviki_has_been_found
        self.color = [0,0,0]
        self.speed = random.randint(3, 10)#random.randint(5, 20)
        self.x = random.randint(0, 600)
        zvikiChance = 25
        if zviki_has_been_found:
            zvikiChance = 70
        if 6==random.randint(0, zvikiChance):
            self.zviki = True
            self.color = [100, 100, 100]

        if not self.zviki:
            if 5>(random.randint(1, 10)):
                self.color[2]=255
            if 5>(random.randint(1, 10)):
                self.color[1]=255
            if 5>(random.randint(1, 10)):
                self.color[0]=255

    def rerand(self):
        speed = random.randint(0, 5)
        x = random.randint(0, 600)
        if True==bool(random.getrandbits(1)):
            self.color[2]=255
        if True==bool(random.getrandbits(1)):
            self.color[1]=0
        if True==bool(random.getrandbits(1)):
            self.color[0]=0

    def update(self):
        self.y +=self.speed

    def set_lose(self):
        self.speed = random.randint(-10, -1)
        self.y = 500

prepare_game_workspace()

fillbox= (255, 0, 0)
fillbox2= (255, 0, 0)
i =0
rushsize = 20
spacebar = False
zviki_has_been_found =False
counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

def update_screen(i):
    global rushsize
    global zvikiCounter
    global total_score
    global zviki_has_been_found
    global bar1_move
    global winmessage


    screen.blit(background,(0,0))
    screen.blit(bar1,(bar1_x,bar1_y))
    global realcolor

    realcolor = [0,0,0]
    if 0<(fillbox2[0]+fillbox[0]):
        realcolor[0] = 255
    if 0<(fillbox2[1]+fillbox[1]):
        realcolor[1] = 255
    if 0<(fillbox2[2]+fillbox[2]):
        realcolor[2] = 255
    bar1.fill(realcolor)
    if spacebar:
        realcolor = [255,255,255]
        bar1.fill([255,255,255])
    if zviki_has_been_found:
        realcolor = [100,100,100]
        bar1.fill([100,100,100])
        zvikiCounter +=1
        if zvikiCounter == 150:
            zvikiCounter = False
            zviki_has_been_found = False
            if 0<(fillbox2[0]+fillbox[0]):
                realcolor[0] = 255
            if 0<(fillbox2[1]+fillbox[1]):
                realcolor[1] = 255
            if 0<(fillbox2[2]+fillbox[2]):
                realcolor[2] = 255
            bar1.fill(realcolor)
            if spacebar:
                realcolor = [255,255,255]
                bar1.fill([255,255,255])
            i = 0
    # print(realcolor)
    global setlose2

    update_death_balls()
    update_presents()

    if youlose:
        winmessage = ":'("
        bar1_move = 0
        load_text(screen, (255, 0, 0), font, 250, 100, "YOU LOSE")
        lose_present = present()
        lose_present.set_lose()
        presents.append(lose_present)


    if youwin:
        bar1_move = 0
        load_text(screen, (255, 255, 0), font, 250, 100, "YOU WIN")
        presents.append(present())

    if zvikiCounter == 0:
        rushsize = 10
        zviki_has_been_found = False

    index_box = pygame.Surface((20,20))

    load_texts(screen,  [(255, 255, 255), (255, 255, 255)], font, [40, 5, 10, 28], ["+     =", "A    D "])
    font2 = pygame.font.SysFont("calibri",20)
    global levelnum
    load_text(screen, (255, 255, 255), font2, 10, 62, "P = Instructions/Pause")

    load_texts(screen, [(100, 255, 255), (255, 255, 255)], font, [580, 10, 484, 10], [str(counter).rjust(3), "Timer:"])#Loads the texts of the timer

    if zvikiCounter:
        font2 = pygame.font.SysFont("calibri",rushsize)
        load_text(screen, (100, 100, 255), font2, 310-2.5*rushsize, 120-rushsize/2, "COLORUSH!")
        if zvikiCounter%2 == 0:
            rushsize +=1

    colors = [fillbox, fillbox2, realcolor]
    xys = [10, 10, 70, 10, 130, 10]
    load_shapes(screen, colors, xys, index_box)

    score1 = font.render(str(total_score), True,(0,255,255))
    screen.blit(score1,(280.,10.))
    score6 = font.render(winmessage, True,(255,0,255))
    screen.blit(score6,(320.,10.))

back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))
bar = pygame.Surface((50,10))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar1_x=300
bar1_y=440.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 450.
clock = pygame.time.Clock()
clock_presents = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)
index_of_color = 0
right = False
left = False
presents, balls = [], []
index_of_color2 = 0
try1 = 0

game_handler()
