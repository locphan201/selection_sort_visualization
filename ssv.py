import pygame as pg
import random

pg.init()
WIDTH, HEIGHT = 330, 175
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Selection Sort Visualization')

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

    ts = txt.render('cur', True, (0, 0, 0))
    window.blit(ts, (x + s*index, y-20))
    pg.draw.rect(window, (0, 0, 0), (x + s*index, y, 22, 22), 1)

    ts = font.render(str(arr[min]), True, (0, 255, 0))
    window.blit(ts, (x + s*min, y))
    ts = txt.render('min', True, (0, 0, 0))
    window.blit(ts, (x + s*min, y+y))

    ts = font.render(str(arr[cur]), True, (255, 0, 0))
    window.blit(ts, (x + s*cur, y))

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
    pg.draw.rect(window, (0, 0, 0), rect, 3)
    ts = font.render('Restart', True, (0, 0, 0))
    window.blit(ts, (rect.x+15, rect.y+15))

def main(window):
    running = True
    clock = pg.time.Clock()
    frame, fps = 0, 60
    SIZE = 10
    arr = create(SIZE)
    index, min, cur = 0, 0, 1
    rect = pg.Rect(115, 100, 100, 50)

    while running:
        clock.tick(fps)
        x, y = pg.mouse.get_pos()

        draw(window, arr, index, min, cur)
        draw_button(window, rect)

        if frame >= fps:
            if index < SIZE-1:
                min, cur = sort(arr, min, cur)
                if cur == SIZE:
                    temp = arr[min]
                    arr[min] = arr[index]
                    arr[index] = temp
                    index += 1
                    min = index
                    cur = min + 1
            frame = 0
        else:
            frame += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if rect.collidepoint(x, y):
                    arr = create(SIZE)
                    index, min, cur = 0, 0, 1

        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main(window)