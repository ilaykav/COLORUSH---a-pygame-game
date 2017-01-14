# COLORUSH -  a game for kids who want to learn the colors and the relatives between them
import math
import os
import random
from sys import exit

import pygame
from pygame.locals import *

total_score = 0
win_message = "WIN = 25"
set_lose_2 = True
you_win, you_lose = False, False
grey_counter = 0
pause = False
screen = 0

class Variables():
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (100, 100, 100),
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    light_blue = (0, 255, 255)
    yellow = (255, 255, 0)
    pink = (255, 0, 255)
    light_green = (100, 255, 100)
    light_red = (255, 100, 100)
    light_blue_2 = (100, 100, 255)
    light_blue_3 = (100, 255, 255)


def update_presents():
    global total_score, set_lose_2, you_lose, you_win, grey_counter, screen, fill_box_2, fill_box_1, i, \
        rush_title_size, space_bar, grey_has_been_found, counter, text, font
    global bar1_x, bar1_y, circle_x, circle_y, bar1_move, bar2_move, speed_x, speed_y, clock, clock_presents, \
        index_of_color, right, left, presents, balls
    global index_of_color2, try1, win_message, pause
    if len(presents) != 0:
        for ex_present in presents:
            if ex_present.color != Variables.white:
                if you_lose and set_lose_2:
                    ex_present.set_lose()
                    set_lose_2 = False
                if ex_present.color[0] == 0 and ex_present.color[1] == 0 and ex_present.color[2] == 0:
                    presents.remove(ex_present)

                ex_present.update()
                rt = pygame.Surface((50, 50))
                rectangle_present = rt.convert()
                rectangle_present.fill(ex_present.color)
                # print bar1_y

                if not you_lose and not you_win and bar1_y - 50 < ex_present.y < bar1_y and \
                                                bar1_x - 50 < ex_present.x < bar1_x + 50:
                    if grey_has_been_found:
                        try:
                            presents.remove(ex_present)
                        except ValueError:
                            pass
                        if not ex_present.is_grey:
                            if not you_lose:
                                total_score += 1

                    if real_color[0] == ex_present.color[0] and real_color[1] == ex_present.color[1] and real_color[2] \
                            == ex_present.color[2]:
                        try:
                            presents.remove(ex_present)
                        except ValueError:
                            pass
                        if not ex_present.is_grey:
                            if not you_lose:
                                total_score += 1
                    if ex_present.is_grey:
                        try:
                            presents.remove(ex_present)
                        except ValueError:
                            pass
                        grey_has_been_found = True
                        grey_counter = 1

            screen.blit(rectangle_present, (ex_present.x, ex_present.y + i))


def update_death_balls():
    if len(balls) != 0:
        for ball in balls:
            circle_surface = pygame.Surface((30, 30))
            circle_outside = pygame.draw.circle(circle_surface, (220, 0, 20), (15, 15), 15)
            circle_inside = pygame.draw.circle(circle_surface, Variables.black, (15, 15), 12)
            circle = circle_surface.convert()
            circle.set_colorkey(Variables.black)
            screen.blit(circle, (ball.x, ball.y + i))
            ball.update()

            global you_lose
            if not you_lose and not you_win and bar1_y - 30 < ball.y < bar1_y and \
                                            bar1_x - 30 < ball.x < bar1_x + 50:
                balls.remove(ball)
                you_lose = True


def seem_impressive():
    bla = 1
    bla2 = random.randint(1, 1000000000)
    for seem_counter in range(1, 10):
        bla += math.pow(10, seem_counter) * random.randint(0, 1)
    print bin(bla2 * bla2), bla, bla + bla2


def draw_pause_menu():
    pause_box = pygame.Surface((500, 300))
    pause_box.set_alpha(20)
    load_shape(screen, (50, 50, 50), 75, 100, pause_box)

    # load the texts of the pause menu
    load_text(screen, Variables.white, font, 327, 320, "+   =")

    # load pause menu object
    pause_box = pygame.Surface((50, 50))
    load_shape(screen, Variables.grey, 400, 245, pause_box)

    # load pause menu object
    pause_box = pygame.Surface((20, 20))
    load_shapes(screen, (Variables.blue, Variables.green, Variables.light_blue), (300, 330, 350, 330, 400, 330),
                pause_box)

    # draws the circle
    circle_surface = pygame.Surface((30, 30))
    circle_outside = pygame.draw.circle(circle_surface, (220, 0, 20), (15, 15), 15)
    circle_inside = pygame.draw.circle(circle_surface, Variables.black, (15, 15), 13)
    circle = circle_surface.convert()
    circle.set_colorkey(Variables.black)
    screen.blit(circle, (205, 255))

    # load the texts of the pause menu
    font2 = pygame.font.SysFont("calibri", 25)
    colors1 = [Variables.light_green, Variables.light_green, Variables.light_red, Variables.light_blue_2,
               Variables.light_green, Variables.light_red,
               Variables.light_blue_2, Variables.light_red, Variables.light_blue_2, Variables.white]
    xys = [80, 225, 80, 355, 270, 100, 80, 125, 80, 150, 80, 175, 80, 200, 80, 305, 80, 330, 80, 375]
    texts = ["Hit R to restart", "To change:                   A      D      Your color", "Game Rules:",
             "Reach to 25 points, earn points by selecting ", "presents- you can only select presents while the",
             "present's color and your color are the same!", "Avoid the red loops! Take the gray presents!",
             "Your color is the mix of the colors in the", "top-left corner:",
             "Hit the space-bar to change your color to white"]
    load_texts(screen, colors1, font2, xys, texts)


def load_shapes(load_screen, load_colors, load_xys, load_surface):
    converted_surface = load_surface.convert()
    for shape_counter, loaded_color in enumerate(load_colors):
        converted_surface.fill(loaded_color)
        load_screen.blit(converted_surface, (load_xys[shape_counter * 2], load_xys[shape_counter * 2 + 1]))


def load_shape(load_screen, load_color, load_x, load_y, load_surface):
    converted_surface = load_surface.convert()
    converted_surface.fill(load_color)
    load_screen.blit(converted_surface, (load_x, load_y))


def restart():
    global total_score, set_lose_2, you_lose, you_win, grey_counter, screen, fill_box_2, fill_box_1, i, \
        rush_title_size, space_bar, grey_has_been_found, counter, text, font
    global bar1_x, bar1_y, circle_x, circle_y, bar1_move, bar2_move, speed_x, speed_y, clock, clock_presents, \
        index_of_color, right, left, presents, balls
    global index_of_color2, try1, win_message, pause
    win_message = "WIN = 25"
    total_score = 0
    set_lose_2 = True
    you_win, you_lose = False, False
    grey_counter = 0
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption("COLORUSH")
    fill_box_1 = Variables.red
    fill_box_2 = Variables.red
    rush_title_size = 20
    space_bar = False
    grey_has_been_found = False

    counter, text = 60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    back = pygame.Surface((640, 480))
    background = back.convert()
    background.fill(Variables.black)
    bar = pygame.Surface((50, 10))
    bar1 = bar.convert()
    bar1.fill(Variables.blue)
    bar1_x = 300
    bar1_y = 440
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0, 0
    speed_x, speed_y = 250, 250
    clock = pygame.time.Clock()
    clock_presents = pygame.time.Clock()
    font = pygame.font.SysFont("calibri", 40)
    index_of_color = 0
    right = False
    left = False
    del presents[:]
    del balls[:]
    index_of_color2 = 0
    try1 = 0


def load_text(load_screen, load_color, load_font, load_x, load_y, load_text):
    loaded_text = load_font.render(load_text, True, load_color)
    load_screen.blit(loaded_text, (load_x, load_y))


def load_texts(load_screen, load_colors, load_font, load_xys, loaded_texts):
    for load_texts_counter, text in enumerate(loaded_texts):
        loaded_text = load_font.render(text, True, load_colors[load_texts_counter])
        load_screen.blit(loaded_text, (load_xys[load_texts_counter * 2], load_xys[load_texts_counter * 2 + 1]))


def game_handler():
    global total_score, set_lose_2, you_lose, you_win, grey_counter, screen, fill_box_2, fill_box_1, i, \
        rush_title_size, space_bar, grey_has_been_found, counter, text, font
    global bar1_x, bar1_y, circle_x, circle_y, bar1_move, bar2_move, speed_x, speed_y, clock, clock_presents, \
        index_of_color, right, left, presents, balls
    global index_of_color2, try1, win_message, pause
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
            if not you_win and not you_lose:
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    clock.tick(60)
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        space_bar = True
                    if event.key == K_r:
                        restart()
                    elif event.key == K_d:
                        index_of_color2 = (index_of_color2 + 1) % 3
                        if index_of_color2 == 0:
                            fill_box_2 = Variables.red
                        elif index_of_color2 == 1:
                            fill_box_2 = Variables.green
                        elif index_of_color2 == 2:
                            fill_box_2 = Variables.blue
                    if event.key == K_a:
                        index_of_color = (index_of_color + 1) % 3
                        if index_of_color == 0:
                            fill_box_1 = Variables.red
                        elif index_of_color == 1:
                            fill_box_1 = Variables.green
                        elif index_of_color == 2:
                            fill_box_1 = Variables.blue
                    if event.key == K_LEFT:
                        try:
                            bar1_move = -ai_speed
                        except UnboundLocalError:
                            print("except")

                        left = True
                    elif event.key == K_RIGHT:
                        try:
                            bar1_move = ai_speed
                        except UnboundLocalError:
                            print("except")

                        right = True
                elif event.type == KEYUP:
                    if event.key == K_SPACE:
                        space_bar = False
                    if event.key == K_LEFT:
                        bar1_move = 0.
                        if right:
                            try:
                                bar1_move = ai_speed
                            except UnboundLocalError:
                                pass

                        left = False
                    elif event.key == K_RIGHT:
                        bar1_move = 0.
                        if left:
                            try:
                                bar1_move = -ai_speed
                            except UnboundLocalError:
                                pass

                        right = False

        if bar1_x < 0:
            if bar1_move < 0:
                bar1_move = 0

        if bar1_x > 585:
            if bar1_move > 0:
                bar1_move = 0

        bar1_x += bar1_move

        # movement
        time_passed = clock.tick(30)

        # seem_impressive()
        mom = (random.randint(0, 1000))
        chance = 33

        if grey_has_been_found:
            chance = 100

        if mom < chance:
            presents.append(Present())

        if not grey_has_been_found and mom < chance - 28:  # take the chance whether to make a death ball or noy
            # including if there is color rush
            i += 1
            balls.append(DeathBall())

        ai_speed = 15
        if total_score == 25:  # checks win-case
            you_win = True

        if counter == 0:  # checks lose-case: if the timer reaches the 0
            you_lose = True

        update_screen()

        while pause:  # makes the pause menu and freezes the game
            draw_pause_menu()  # I think it's pretty clear...
            for event in pygame.event.get():  # gets events from the user in the pause 'mode'
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
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.init()
    pygame.display.set_caption("COLORUSH")
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    file_of_icon = os.path.join(main_dir, 'icon.png')
    surface_icon = pygame.image.load(file_of_icon)
    icon = pygame.transform.scale(surface_icon, (32, 32))
    pygame.display.set_icon(icon)


class DeathBall:
    speed = random.randint(5, 15)
    x = 0
    y = 20
    rectangle_present = 0

    def __init__(self):
        self.speed = random.randint(5, 12)  # random.randint(5, 20)
        self.x = random.randint(0, 600)

    def update(self):
        self.y += self.speed


class Present:
    is_grey = False
    speed = random.randint(3, 10)
    x = 0
    y = 20
    rectangle_present = 0

    def __init__(self):
        global grey_has_been_found
        self.color = [0, 0, 0]
        self.speed = random.randint(3, 10)  # random.randint(5, 20)
        self.x = random.randint(0, 600)
        grey_chance = 25
        if grey_has_been_found:
            grey_chance = 70
        if 6 == random.randint(0, grey_chance):
            self.is_grey = True
            self.color = [100, 100, 100]

        if not self.is_grey:
            if 5 > (random.randint(1, 10)):
                self.color[2] = 255
            if 5 > (random.randint(1, 10)):
                self.color[1] = 255
            if 5 > (random.randint(1, 10)):
                self.color[0] = 255

    def reset_random(self):
        self.speed = random.randint(0, 5)
        self.x = random.randint(0, 600)
        if bool(random.getrandbits(1)):
            self.color[2] = 255
        if bool(random.getrandbits(1)):
            self.color[1] = 0
        if bool(random.getrandbits(1)):
            self.color[0] = 0

    def update(self):
        self.y += self.speed

    def set_lose(self):
        self.speed = random.randint(-10, -1)
        self.y = 500


prepare_game_workspace()

fill_box_1 = Variables.red
fill_box_2 = Variables.red
i = 0
rush_title_size = 20
space_bar = False
grey_has_been_found = False
counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)


def update_screen():
    global rush_title_size
    global grey_counter
    global total_score
    global grey_has_been_found
    global bar1_move
    global win_message

    screen.blit(background, (0, 0))
    screen.blit(bar1, (bar1_x, bar1_y))
    global real_color

    real_color = [0, 0, 0]
    if 0 < (fill_box_2[0] + fill_box_1[0]):
        real_color[0] = 255
    if 0 < (fill_box_2[1] + fill_box_1[1]):
        real_color[1] = 255
    if 0 < (fill_box_2[2] + fill_box_1[2]):
        real_color[2] = 255
    bar1.fill(real_color)
    if space_bar:
        real_color = Variables.white
        bar1.fill(Variables.white)
    if grey_has_been_found:
        real_color = [100, 100, 100]
        bar1.fill([100, 100, 100])
        grey_counter += 1
        if grey_counter == 150:
            grey_counter = False
            grey_has_been_found = False
            if 0 < (fill_box_2[0] + fill_box_1[0]):
                real_color[0] = 255
            if 0 < (fill_box_2[1] + fill_box_1[1]):
                real_color[1] = 255
            if 0 < (fill_box_2[2] + fill_box_1[2]):
                real_color[2] = 255
            bar1.fill(real_color)
            if space_bar:
                real_color = Variables.white
                bar1.fill(Variables.white)

    global set_lose_2

    update_presents()
    update_death_balls()

    if you_lose:
        win_message = ":'("
        bar1_move = 0
        load_text(screen, Variables.red, font, 250, 100, "YOU LOSE")
        lose_present = Present()
        lose_present.set_lose()
        presents.append(lose_present)

    if you_win:
        bar1_move = 0
        load_text(screen, Variables.yellow, font, 250, 100, "YOU WIN")
        presents.append(Present())

    if grey_counter == 0:
        rush_title_size = 10
        grey_has_been_found = False

    index_box = pygame.Surface((20, 20))

    load_texts(screen, [Variables.white, Variables.white], font, [40, 5, 10, 28], ["+     =", "A    D "])
    font2 = pygame.font.SysFont("calibri", 20)
    load_text(screen, Variables.white, font2, 10, 62, "P = Instructions/Pause")

    # Loads the texts of the timer
    load_texts(screen, [Variables.light_blue_3, Variables.white],
               font, [580, 10, 484, 10], [str(counter).rjust(3), "Timer:"])

    if grey_counter:
        font2 = pygame.font.SysFont("calibri", rush_title_size)
        load_text(screen, Variables.light_blue_2, font2, 310 - 2.5 *
                  rush_title_size, 120 - rush_title_size / 2, "COLORUSH!")
        if grey_counter % 2 == 0:
            rush_title_size += 1

    colors = [fill_box_1, fill_box_2, real_color]
    xys = [10, 10, 70, 10, 130, 10]
    load_shapes(screen, colors, xys, index_box)

    score1 = font.render(str(total_score), True, Variables.light_blue)
    screen.blit(score1, (280, 10))
    score6 = font.render(win_message, True, Variables.pink)
    screen.blit(score6, (320, 10))


back = pygame.Surface((640, 480))
background = back.convert()
background.fill(Variables.black)
bar = pygame.Surface((50, 10))
bar1 = bar.convert()
bar1.fill(Variables.blue)
bar1_x = 300
bar1_y = 440
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0., 0.
speed_x, speed_y = 250., 250.
clock = pygame.time.Clock()
clock_presents = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)
index_of_color = 0
right = False
left = False
presents, balls = [], []
index_of_color2 = 0
try1 = 0

game_handler()
