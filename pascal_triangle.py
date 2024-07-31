import matplotlib.pyplot
import pygame
import random
import math
import matplotlib as plt


pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
angles = []



WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (100,130,54)


def draw_triangle():
    pygame.draw.polygon(screen, (200,200,200), [(100, 500), (700, 500), (400, 100)])

    # نوشتن اعداد بر روی مثلث
    font = pygame.font.Font(None, 36)
    text = font.render(str(1), True, BLUE)
    screen.blit(text, (390, 130))
    txt1 = "1            1"
    txt1 = font.render(txt1,True,BLUE)
    screen.blit(txt1, (345, 180))
    txt1 = "1           2           1"
    txt1 = font.render(txt1, True, BLUE)
    screen.blit(txt1, (305, 230))
    txt1 = "1        3            3         1"
    txt1 = font.render(txt1, True, BLUE)
    screen.blit(txt1, (275, 280))
    txt1 = "1         4         6         4          1"
    txt1 = font.render(txt1, True, BLUE)
    screen.blit(txt1, (240, 330))
    txt1 = "1         5         10        10       5        1"
    txt1 = font.render(txt1, True, BLUE)
    screen.blit(txt1, (205, 380))
    txt1 = "1         6       15        20        15       6         1"
    txt1 = font.render(txt1, True, BLUE)
    screen.blit(txt1, (170, 430))
    txt1 = "1         7       21        35        35       21         7       1"
    txt1 = font.render(txt1, True, BLUE)
    screen.blit(txt1, (130, 470))



class Ball:
    def __init__(self):
        self.x = 400
        self.y = 100
        self.angle = random.uniform(0.95, 2.15)
        angles.append(self.angle)
        self.speed = 2
        r = random.randint(0,225)
        g = random.randint(0,225)
        b = random.randint(0,225)
        self.color = (r,g,b)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        if not (100 < self.x < 700 and 100 < self.y < 500):
            self.speed = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)



balls = [Ball() for _ in range(40)]

while running:
    screen.fill((130,190,190))
    draw_triangle()
    for ball in balls:
        ball.move()
        ball.draw()


    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

matplotlib.pyplot.figure("Pascal Triangle")
ranges = [0.95, 1.1, 1.25, 1.45, 1.65, 1.85, 2, 2.15]
labels = ['1', '7', '21','35', '35', '21', '7','1']
matplotlib.pyplot.hist(angles, bins=[0.95,1.1,1.25,1.45,1.65,1.85,2,2.15],range = (0.95,2.15),color='c', edgecolor='black')
matplotlib.pyplot.xticks(ranges,labels)
matplotlib.pyplot.xlabel("Range")
matplotlib.pyplot.ylabel("Ball Count")
matplotlib.pyplot.show()


pygame.quit()
