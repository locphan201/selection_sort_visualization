import pygame as pg
import random

pg.init()
WIDTH, HEIGHT = 330, 175
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Selection Sort Visualization')

def button_setup():
    rect = []
    rect.append([pg.Rect(15, 100, 90, 50), 'Run'])
    rect.append([pg.Rect(115, 100, 90, 50), 'Random'])
    rect.append([pg.Rect(215, 100, 90, 50), 'Step'])
    return rect

def create(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0,99))
    return arr

def sort(arr, left, right):
    if arr[left] > arr[right]:
        return right, right + 1
    return left, right + 1

def draw_cursor(window, arr, font, index, min, cur):
    txt = pg.font.SysFont('Arial', 15)
    x, y, s = 15, 30, 30

    pg.draw.rect(window, (0, 0, 0), (x + s*index, y, 22, 22), 1)

    ts = font.render(str(arr[min]), True, (0, 255, 0))
    window.blit(ts, (x + s*min, y))
    ts = txt.render('min', True, (0, 0, 0))
    window.blit(ts, (x + s*min, y+y))

    ts = font.render(str(arr[cur]), True, (255, 0, 0))
    window.blit(ts, (x + s*cur, y))
    ts = txt.render('cur', True, (0, 0, 0))
    window.blit(ts, (x + s*cur, y+y))

def draw(window, arr, index, min, cur):
    window.fill((255, 255, 255))
    font = pg.font.SysFont('Arial', 20)
    x, y, s = 15, 30, 30
    for i in range(len(arr)):
        textsurface = font.render(str(arr[i]), True, (0, 0, 0))
        window.blit(textsurface, (x + s*i, y))
    if cur < len(arr):
        draw_cursor(window, arr, font, index, min, cur)

def draw_button(window, rect):
    font = pg.font.SysFont('Arial', 20)
    
    for r in rect:
        pg.draw.rect(window, (0, 0, 0), r[0], 3)
        ts = font.render(r[1], True, (0, 0, 0))
        window.blit(ts, (r[0].x+15, r[0].y+15))

def step(arr, index, min):
    return arr[index], arr[min], index + 1, index + 1, index + 2

def main(window):
    running = True
    clock = pg.time.Clock()
    frame, fps = 0, 60
    SIZE = 10
    arr = create(SIZE)
    index, min, cur = 0, 0, 1
    rect = button_setup()
    run = False

    while running:
        clock.tick(fps)
        x, y = pg.mouse.get_pos()

        draw(window, arr, index, min, cur)
        draw_button(window, rect)

        if run:
            if frame >= fps:
                if index < SIZE-1:
                    min, cur = sort(arr, min, cur)
                    if cur == SIZE:
                        arr[min], arr[index], index, min, cur = step(arr, index, min)
                else:
                    run = False
                frame = 0
            else:
                frame += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect[0][0].collidepoint(x, y):
                    run = True
                    frame = 0
                if  rect[1][0].collidepoint(x, y):
                    arr = create(SIZE)
                    run = False
                    index, min, cur = 0, 0, 1
                if rect[2][0].collidepoint(x, y):
                    run = False
                    if index < SIZE-1:
                        min, cur = sort(arr, min, cur)
                    if cur == SIZE:
                        arr[min], arr[index], index, min, cur = step(arr, index, min)
                
        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main(window)