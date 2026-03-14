import pygame
from random import randint
from math import sqrt

pygame.init()

screen = pygame.display.set_mode((750,750))
screen_width, screen_height = screen.get_size()
screen.fill((255, 255, 255))

class Capitol:
    def __init__(self, X, Y, COL, point_col = "BLACK",point_radius = 5):
        self.x = X
        self.y = Y
        self.col = COL
        self.point_col = self.col
        self.point_radius = point_radius
    def draw(self):
        pygame.draw.circle(screen,self.point_col,(self.x,self.y),self.point_radius)

paris = Capitol(25,50,(255,255,255))
paris.draw()
enemy = Capitol(725,700,"WHITE")
enemy.draw()

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

capitols = [paris]
for i in range(5):
    x = randint(0,screen_width)
    y = randint(0,screen_height)
    #colour = (randint(0,255),randint(0,255),randint(0,255))
    colour = (0, 0,0)
    cap = Capitol(x,y,colour)
    capitols.append(cap)

def draw_caps(l):
    assert type(l) == list
    for e in l:
        e.draw()

def update_caps(step):
    for x in range(0,screen_width,step):
        for y in range(0,screen_height,step):
            #draw_caps(capitols)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    print("a")
                    return
            closest_cap = Capitol(screen_width*2,screen_height*2,"BLACK")
            for e in capitols:
                dist = distance((x,y),(e.x,e.y))
                if dist < distance((x,y),(closest_cap.x,closest_cap.y)):
                    closest_cap = e
            square = pygame.Rect(x,y,step,step)
            pygame.draw.rect(screen, closest_cap.col, square)
            #pygame.Surface.set_at(screen,(x,y),closest_cap.col)

#update_caps()
pygame.display.flip()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: paris.y+=10
            if event.key == pygame.K_UP: paris.y -= 10
            if event.key == pygame.K_RIGHT: paris.x += 10
            if event.key == pygame.K_LEFT: paris.x -= 10
            paris.draw()

    #mouse_x, mouse_y = pygame.mouse.get_pos()
    paris.x, paris.y = pygame.mouse.get_pos()
    paris.draw()

    #pygame.time.wait(1000)
    """
    enemy.x = randint(0,screen_width)
    enemy.y = randint(0, screen_height)
    paris.x = randint(0, screen_width)
    paris.y = randint(0, screen_height)
    enemy.col = (randint(0,255),randint(0,255),randint(0,255))
    paris.col = (randint(0, 255), randint(0, 255), randint(0, 255))
    """
    update_caps(7)
    pygame.display.flip()
