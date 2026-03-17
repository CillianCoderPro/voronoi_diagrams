import pygame
from random import randint
from math import sqrt

pygame.init()

screen = pygame.display.set_mode((750,750))
screen_width, screen_height = screen.get_size()

step = 5

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

class Capitol:
    def __init__(self, X, Y, COL):
        self.x = X
        self.y = Y
        self.col = COL
        self.point_col = "BLACK"
        self.point_radius = 20
        self.selected = False
    def draw(self):
        pygame.draw.circle(screen,self.point_col,(self.x,self.y),self.point_radius)



cap_list = []
for i in range(step):
    x = randint(0,screen_width//2)
    y = randint(0,screen_height)
    blue_cap = Capitol(x,y,"BLUE")
    cap_list.append(blue_cap)
    red_cap = Capitol(screen_width-x,y,"RED")
    cap_list.append(red_cap)

def draw_caps(l):
    assert type(l) == list
    for e in l:
        e.draw()

def update_caps(step,team):
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
            for e in team:
                dist = distance((x,y),(e.x,e.y))
                if dist < distance((x,y),(closest_cap.x,closest_cap.y)):
                    closest_cap = e
            square = pygame.Rect(x,y,step,step)
            pygame.draw.rect(screen, closest_cap.col, square)
            #pygame.Surface.set_at(screen,(x,y),closest_cap.col)

#update_caps()
pygame.display.flip()
selected_cap = None

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("a")
                pygame.quit()
                exit()
            """
            if event.key == pygame.K_DOWN: paris.y+=10
            if event.key == pygame.K_UP: paris.y -= 10
            if event.key == pygame.K_RIGHT: paris.x += 10
            if event.key == pygame.K_LEFT: paris.x -= 10
            paris.draw()
            """

    """
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    paris.x, paris.y = pygame.mouse.get_pos()
    paris.draw()
    if pygame.mouse.get_pressed()[0]:
        e = Capitol(paris.x,paris.y, "WHITE")
        capitols.append(e)
    """

    if pygame.mouse.get_pressed()[0]:
        if selected_cap != None:
            cap_list.append(selected_cap)
            selected_cap = None
        else:
            for i,cap in enumerate(cap_list):
                if distance((cap.x,cap.y),pygame.mouse.get_pos()) <= 20:
                    selected_cap = cap
                    cap_list.pop(i)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    try:
        selected_cap.x, selected_cap.y = pygame.mouse.get_pos()
        selected_cap.draw()
    except:
        print("a")


    update_caps(step-2, cap_list)
    draw_caps(cap_list)
    pygame.display.flip()
