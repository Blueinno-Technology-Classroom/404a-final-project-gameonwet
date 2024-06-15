import pgzrun
from pgzhelper import *
import math
import random

WIDTH = 1024
HEIGHT = 768

player = Actor("player")
player.pos = (WIDTH / 2, HEIGHT / 2)

leaves = []
leaf_CD = 0

prev_mouse_pos = [0, 0]

leaf_num = 15

blow_range = 150
blow_power = 10

leaf_money = 0

def update():
    global leaf_CD
    global leaf_money
    global blow_range
    global blow_power


    leaf_CD += 1
    if leaf_CD >= 240:
        for i in range(leaf_num):
            leaf = Actor("gold_leaf")
            leaf.weight = 1

            leaf.x = random.randint(0, WIDTH)
            leaf.y = random.randint(0, HEIGHT)
            leaf.pe = 0

            

            leaves.append(leaf)

        leaf_CD = 0
    
    for leaf in leaves:
        if player.distance_to(leaf) <= blow_range:
            leaf.point_towards(player)
            leaf.pe = blow_power
            



        if leaf.pe > 0:
            leaf.move_forward(-leaf.pe)
            leaf.pe -= 1
        



        if leaf.right <= 0:
            leaves.remove(leaf)
            leaf_money += 1
        if leaf.left >= WIDTH:
            leaves.remove(leaf)
            leaf_money += 1
        if leaf.bottom <= 0:
            leaves.remove(leaf)
            leaf_money += 1
        if leaf.top >= HEIGHT:
            leaves.remove(leaf)
            leaf_money += 1


def on_mouse_move(pos):
    player.pos = pos
    player.angle = player.angle_to(prev_mouse_pos) - 180
    prev_mouse_pos[0] = pos[0]
    prev_mouse_pos[1] = pos[1]

    
    
def draw():
    screen.clear()
    screen.blit('bg', (0, 0))

    player.draw()
    for leaf in leaves:
        leaf.draw()

    screen.draw.text(str(leaf_money), (10, 30), fontsize = 60)



pgzrun.go()