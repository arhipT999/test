import pygame   
import random
import time
from ctypes import windll
WIDTH = 500
HEIGHT = 300
FPS = 60
dis = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 55)

def Your_score(p, a, b, l):
   value = font_style.render(p, True, l)
   dis.blit(value, [a, b])
run = True
def moveWin(new_x, new_y):
    hwnd = pygame.display.get_wm_info()['window']
    w, h = pygame.display.get_surface().get_size()
    windll.user32.MoveWindow(hwnd, new_x, new_y, w, h, False)
def pon():
    screen.fill(BLACK)
    Your_score('Я так и знал', 150, 100, WHITE)
    pygame.display.flip()
    time.sleep(2)
def pon1():
    screen.fill(BLACK)
    Your_score('Э... я это не предусмотрел', 0, 100, WHITE)
    pygame.display.flip()
    time.sleep(2)
    screen.fill(BLACK)
    Your_score('Это типо пасхалка...', 50, 100, WHITE)
    pygame.display.flip()
    time.sleep(2)
    screen.fill(BLACK)
    Your_score('Error 0xc000007b', 100, 100, WHITE)
    pygame.display.flip()
    time.sleep(2)
    screen.fill(BLACK)
    pygame.display.flip()
    run1 = True
    WIDTH = 200
    HEIGHT = 200
    dis = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    pygame.display.flip()
    window_pos = [500, 200]
    moveWin(*window_pos)
    while run1:
        clock.tick(FPS)
        a = pygame.mouse.get_pos()
        x, y = a[0], a[1]
        #print(x, y)
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                run1 = False
            if x >= 69 and x <= 139 and y >=128 and y <= 158 and event.type == pygame.MOUSEBUTTONUP:
                run1 = False
        pygame.draw.rect(dis, WHITE, [70, 130, 70, 30])
        Your_score('Ок', 80, 127, BLACK)
        Your_score('Error', 60, 20, WHITE)
        pygame.display.flip()

while run:
    clock.tick(FPS)
    a = pygame.mouse.get_pos()
    x, y = a[0], a[1]
    err = 0
    prav = 0
    #print(x,y)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            screen.fill(BLACK)
            Your_score('Ты не выйдешь отсюда', 20, 0, WHITE)
            pygame.display.flip()
            time.sleep(2)
            screen.fill(BLACK)
            Your_score('Хотя...', 200, 0, WHITE)
            pygame.display.flip()
            time.sleep(2)
            run = False
        if x >= 99 and x <= 199 and y >=150 and y <= 198:
            n, m = random.randint(100, 600), random.randint(0, 400)
            window_pos = [n, m]
            moveWin(*window_pos)
        if x >= 299 and x <= 399 and y >=149 and y <= 198 and event.type == pygame.MOUSEBUTTONUP:
            prav = 1
        if x >= 99 and x <= 199 and y >=150 and y <= 198 and event.type == pygame.MOUSEBUTTONUP:
            err = 1
        if err == 1:
            err = 0
            pon1()
            run = False
        if prav == 1:
            prav = 0
            pon()
            run = False
        pygame.draw.rect(dis, WHITE, [100, 150, 100, 50])
        pygame.draw.rect(dis, WHITE, [300, 150, 100, 50])
        Your_score('Нет', 120, 155, BLACK)
        Your_score('Да', 320, 155, BLACK)
    Your_score('Программа топ?', 120, 0, WHITE)
    pygame.display.flip()