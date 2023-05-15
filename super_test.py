import pygame#pyinstaller --onefile super_test.py
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
while run:
    clock.tick(FPS)
    a = pygame.mouse.get_pos()
    x, y = a[0], a[1]
    prav = 0
    #print(x,y)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False
        if x >= 99 and x <= 199 and y >=150 and y <= 198:
            n, m = random.randint(100, 600), random.randint(0, 400)
            window_pos = [n, m]
            moveWin(*window_pos)
        if x >= 299 and x <= 399 and y >=149 and y <= 198 and event.type == pygame.MOUSEBUTTONUP:
            prav = 1
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