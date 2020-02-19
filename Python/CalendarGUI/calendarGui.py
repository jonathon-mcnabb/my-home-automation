import pygame
import pygame.color
import pygame as pg
import datetime
from datetime import date
from inputBox import InputBox


pygame.init()
pygame.font.init()
pygame.display.set_caption('Calendar')

gameIcon = pygame.image.load('rec/calendar.png')
pygame.display.set_icon(gameIcon)

# define colors
WHITE = pygame.Color(255, 255, 255, 255)
BLUE = pygame.Color(66, 133, 244, 255)
BLUE2 = pygame.Color(50, 107, 166, 255)
RED = pygame.Color(219, 68, 55, 255)
YELLOW = pygame.Color(244, 160, 0, 255)
GREEN = pygame.Color(15, 157, 88, 255)
GREY = pygame.Color(127, 127, 127, 255)
DARK_GREY = pygame.Color(89, 89, 89, 255)

# set the month to the current month
month = datetime.datetime.now().strftime("%m")
month_y = int(month)
print(month_y)

button_font = pygame.font.SysFont('Century Gothic', 20, 1)

# Sets up the screen size... that the point (0, 0) is at the upper left hand corner of the screen
# need to add ability to change screen size
screen_width = 1300
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))


def draw_calendar():
    # define fonts

    # month
    month_font = pygame.font.SysFont('Century Gothic', 48, 1)
    if month_y == 1:
        month_surface = month_font.render('January', False, BLUE2)
    if month_y == 2:
        month_surface = month_font.render('February', False, BLUE2)
    if month_y == 3:
        month_surface = month_font.render('March', False, BLUE2)
    if month_y == 4:
        month_surface = month_font.render('April', False, BLUE2)
    if month_y == 5:
        month_surface = month_font.render('May', False, BLUE2)
    if month_y == 6:
        month_surface = month_font.render('June', False, BLUE2)
    if month_y == 7:
        month_surface = month_font.render('July', False, BLUE2)
    if month_y == 8:
        month_surface = month_font.render('August', False, BLUE2)
    if month_y == 9:
        month_surface = month_font.render('September', False, BLUE2)
    if month_y == 10:
        month_surface = month_font.render('October', False, BLUE2)
    if month_y == 11:
        month_surface = month_font.render('November', False, BLUE2)
    if month_y == 12:
        month_surface = month_font.render('December', False, BLUE2)

    month_width = month_surface.get_width()

    # year
    year_font = pygame.font.SysFont('Century Gothic', 48, 1)
    year_surface = year_font.render('2019', False, GREY)
    year_width = year_surface.get_width()

    # day
    day_font = pygame.font.SysFont('Century Gothic', 12, 1)

    day_surface1 = day_font.render('Sunday', False, WHITE)
    day_surface2 = day_font.render('Monday', False, WHITE)
    day_surface3 = day_font.render('Tuesday', False, WHITE)
    day_surface4 = day_font.render('Wednesday', False, WHITE)
    day_surface5 = day_font.render('Thursday', False, WHITE)
    day_surface6 = day_font.render('Friday', False, WHITE)
    day_surface7 = day_font.render('Saturday', False, WHITE)

    offset = 30
    space = 15
    # fill the screen with white
    screen.fill(WHITE)

    # draw the month/year at the top of the screen
    screen.blit(month_surface, (screen_width - offset - month_width - space - year_width, offset))
    screen.blit(year_surface, (screen_width - year_width - offset, offset))

    # draw line underneath month/year
    pygame.draw.line(screen, GREY, (offset, 100), (screen_width - offset, 100), 1)

    # draw verticle lines of calendar
    pygame.draw.line(screen, GREY, (offset, 130), (offset, 650), 1)
    pygame.draw.line(screen, GREY, (offset + 177, 130), (offset + 177, 650), 1)
    pygame.draw.line(screen, GREY, (offset + 2 * 177, 130), (offset + 2 * 177, 650), 1)
    pygame.draw.line(screen, GREY, (offset + 3 * 177, 130), (offset + 3 * 177, 650), 1)
    pygame.draw.line(screen, GREY, (offset + 4 * 177, 130), (offset + 4 * 177, 650), 1)
    pygame.draw.line(screen, GREY, (offset + 5 * 177, 130), (offset + 5 * 177, 650), 1)
    pygame.draw.line(screen, GREY, (offset + 6 * 177, 130), (offset + 6 * 177, 650), 1)
    pygame.draw.line(screen, GREY, (screen_width - offset, 130), (screen_width - offset, 650), 1)

    # draw horizontal lines of calendar
    pygame.draw.line(screen, GREY, (offset, 130), (offset + 1240, 130), 1)
    pygame.draw.line(screen, GREY, (offset, 150), (offset + 1240, 150), 1)
    pygame.draw.line(screen, GREY, (offset, 150 + 1 * 83), (offset + 1240, 150 + 1 * 83), 1)
    pygame.draw.line(screen, GREY, (offset, 150 + 2 * 83), (offset + 1240, 150 + 2 * 83), 1)
    pygame.draw.line(screen, GREY, (offset, 150 + 3 * 83), (offset + 1240, 150 + 3 * 83), 1)
    pygame.draw.line(screen, GREY, (offset, 150 + 4 * 83), (offset + 1240, 150 + 4 * 83), 1)
    pygame.draw.line(screen, GREY, (offset, 150 + 5 * 83), (offset + 1240, 150 + 5 * 83), 1)
    pygame.draw.line(screen, GREY, (offset, 150 + 6 * 83 + 2), (offset + 1240, 150 + 6 * 83 + 2), 1)

    # draw rectangles for day background
    pygame.draw.rect(screen, BLUE2, (offset + 1 * 177 + 2, 130, 177 - 3, 20))
    pygame.draw.rect(screen, BLUE2, (offset + 2 * 177 + 2, 130, 177 - 3, 20))
    pygame.draw.rect(screen, BLUE2, (offset + 3 * 177 + 2, 130, 177 - 3, 20))
    pygame.draw.rect(screen, BLUE2, (offset + 4 * 177 + 2, 130, 177 - 3, 20))
    pygame.draw.rect(screen, BLUE2, (offset + 5 * 177 + 2, 130, 177 - 3, 20))

    pygame.draw.rect(screen, DARK_GREY, (offset, 130, 177 - 1, 20))
    pygame.draw.rect(screen, DARK_GREY, (offset + 6 * 177 + 2, 130, 177, 20))

    # draw the days on top of the rectangles
    screen.blit(day_surface1, (offset + 70, 130 + 2))
    screen.blit(day_surface2, (offset + 70 + 1 * 177, 130 + 2))
    screen.blit(day_surface3, (offset + 70 + 2 * 177, 130 + 2))
    screen.blit(day_surface4, (offset + 70 + 3 * 177 - 15, 130 + 2))
    screen.blit(day_surface5, (offset + 70 + 4 * 177 - 15, 130 + 2))
    screen.blit(day_surface6, (offset + 70 + 5 * 177, 130 + 2))
    screen.blit(day_surface7, (offset + 70 + 6 * 177, 130 + 2))


def draw_dates():
    first = datetime.date(2019, month_y, 1)  # year, month, day
    weekday = first.strftime("%w")
    week_offset = int(weekday)
    if month_y == 12:
        total_days = (date(2020, (month_y % 12) + 1, 1) - date(2019, month_y, 1)).days
    else:
        total_days = (date(2019, (month_y % 12) + 1, 1) - date(2019, month_y, 1)).days
    day_font = pygame.font.SysFont('Century Gothic', 12, 1)

    date_text = []

    for i in range(week_offset):
        date_text.append(day_font.render('', False, BLUE))

    i = 0

    for c in range(7):
        for r in range(6):
            if i < total_days + week_offset:
                if i < 10:
                    date_text.append(day_font.render(' '+str(i+1), False, GREY))
                else:
                    date_text.append(day_font.render(str(i + 1), False, GREY))
                i += 1
    i = 0
    for c in range(7):
        for r in range(7):
            if i < total_days + week_offset:
                screen.blit(date_text[i], (30 + 160 + r * 177, 70 + 83*(c+1)))
                i += 1


# load input boxes
input_boxes0 = []
temp_text = ['', '', '', '']

load_file = open('rec/0.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        # temp_text[0] = str(c)
        # temp_text[1] = str(r)
        if c == 6 and r == 5:
            input_boxes0.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes0.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes0.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes0.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))


input_boxes1 = []
load_file = open('rec/1.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes1.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2,temp_text))
        elif c == 6:
            input_boxes1.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes1.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2,temp_text))
        else:
            input_boxes1.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83,temp_text))

input_boxes2 = []
load_file = open('rec/2.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes2.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2,temp_text))
        elif c == 6:
            input_boxes2.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83,temp_text))
        elif r == 5:
            input_boxes2.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes2.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes3 = []
load_file = open('rec/3.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes3.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes3.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes3.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes3.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes4 = []
load_file = open('rec/4.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes4.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes4.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes4.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes4.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes5 = []
load_file = open('rec/5.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes5.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes5.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes5.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes5.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes6 = []
load_file = open('rec/6.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes6.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes6.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes6.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes6.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes7 = []
load_file = open('rec/7.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes7.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes7.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83,temp_text))
        elif r == 5:
            input_boxes7.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes7.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes8 = []
load_file = open('rec/8.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes8.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes8.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes8.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes8.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes9 = []
load_file = open('rec/9.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes9.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes9.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes9.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes9.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes10 = []
load_file = open('rec/10.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes10.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2, temp_text))
        elif c == 6:
            input_boxes10.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes10.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes10.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))

input_boxes11 = []
load_file = open('rec/11.txt', 'r')

for c in range(7):
    for r in range(6):
        for i in range(4):
            temp_text[i] = load_file.readline().strip('\n')
        if c == 6 and r == 5:
            input_boxes11.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83 + 2,temp_text))
        elif c == 6:
            input_boxes11.append(InputBox(30 + 177 * c, 150 + 83 * r, 177 + 1, 83, temp_text))
        elif r == 5:
            input_boxes11.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83 + 2, temp_text))
        else:
            input_boxes11.append(InputBox(30 + 177 * c, 150 + 83 * r, 177, 83, temp_text))


def save_dates():

    f = open('rec/0.txt', 'w+')
    for b in input_boxes0:
        f.write(b.get_text())

    f = open('rec/1.txt', 'w+')
    for b in input_boxes1:
        f.write(b.get_text())

    f = open('rec/2.txt', 'w+')
    for b in input_boxes2:
        f.write(b.get_text())

    f = open('rec/3.txt', 'w+')
    for b in input_boxes3:
        f.write(b.get_text())

    f = open('rec/4.txt', 'w+')
    for b in input_boxes4:
        f.write(b.get_text())

    f = open('rec/5.txt', 'w+')
    for b in input_boxes5:
        f.write(b.get_text())

    f = open('rec/6.txt', 'w+')
    for b in input_boxes6:
        f.write(b.get_text())

    f = open('rec/7.txt', 'w+')
    for b in input_boxes7:
        f.write(b.get_text())

    f = open('rec/8.txt', 'w+')
    for b in input_boxes8:
        f.write(b.get_text())

    f = open('rec/9.txt', 'w+')
    for b in input_boxes9:
        f.write(b.get_text())

    f = open('rec/10.txt', 'w+')
    for b in input_boxes10:
        f.write(b.get_text())

    f = open('rec/11.txt', 'w+')
    for b in input_boxes11:
        f.write(b.get_text())


running = 1

next_button = pygame.Rect(700, 40, 150, 50)
previous_button = pygame.Rect(500, 40, 150, 50)

next_string = button_font.render('Next', False, GREY)
previous_string = button_font.render('Previous', False, GREY)

while running:
    clock = pg.time.Clock()
    draw_calendar()

    for event in pg.event.get():
        if event.type == pygame.QUIT:
            save_dates()
            running = 0

        if month_y == 1:
            for box in input_boxes0:
                box.handle_event(event)
        elif month_y == 2:
            for box in input_boxes1:
                box.handle_event(event)
        elif month_y == 3:
            for box in input_boxes2:
                box.handle_event(event)
        elif month_y == 4:
            for box in input_boxes3:
                box.handle_event(event)
        elif month_y == 5:
            for box in input_boxes4:
                box.handle_event(event)
        elif month_y == 6:
            for box in input_boxes5:
                box.handle_event(event)
        elif month_y == 7:
            for box in input_boxes6:
                box.handle_event(event)
        elif month_y == 8:
            for box in input_boxes7:
                box.handle_event(event)
        elif month_y == 9:
            for box in input_boxes8:
                box.handle_event(event)
        elif month_y == 10:
            for box in input_boxes9:
                box.handle_event(event)
        elif month_y == 11:
            for box in input_boxes10:
                box.handle_event(event)
        elif month_y == 12:
            for box in input_boxes11:
                box.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position
            # checks if mouse position is over the button
            if next_button.collidepoint(mouse_pos):
                # updates month_y
                month_y += 1
                if month_y > 12:
                    month_y = 12
            if previous_button.collidepoint(mouse_pos):
                # updates month_y
                month_y -= 1
                if month_y < 1:
                    month_y = 1

    if month_y == 1:
        for box in input_boxes0:
            box.draw(screen)
    elif month_y == 2:
        for box in input_boxes1:
            box.draw(screen)
    elif month_y == 3:
        for box in input_boxes2:
            box.draw(screen)
    elif month_y == 4:
        for box in input_boxes3:
            box.draw(screen)
    elif month_y == 5:
        for box in input_boxes4:
            box.draw(screen)
    elif month_y == 6:
        for box in input_boxes5:
            box.draw(screen)
    elif month_y == 7:
        for box in input_boxes6:
            box.draw(screen)
    elif month_y == 8:
        for box in input_boxes7:
            box.draw(screen)
    elif month_y == 9:
        for box in input_boxes8:
            box.draw(screen)
    elif month_y == 10:
        for box in input_boxes9:
            box.draw(screen)
    elif month_y == 11:
        for box in input_boxes10:
            box.draw(screen)
    elif month_y == 12:
        for box in input_boxes11:
            box.draw(screen)

    pygame.draw.rect(screen, BLUE, next_button, 2)  # draw button
    pygame.draw.rect(screen, BLUE, previous_button, 2)  # draw button

    screen.blit(next_string, (700 + 50, 40 + 10))
    screen.blit(previous_string, (500 + 30, 40 + 10))

    # draw date overlays
    draw_dates()


    # update entire screen
    pg.display.flip()


