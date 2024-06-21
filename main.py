import pgzrun
from pgzhelper import *
import math
import random

WIDTH = 1024
HEIGHT = 768

player = Actor("player")
player.pos = (WIDTH / 2, HEIGHT / 2)
player.pre_angles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

leaves = []
leaf_CD = 0

prev_mouse_pos = [0, 0]

leaf_num = 15
blow_range = 150
blow_power = 10

leaf_money = 0

range_btn = Actor("range_btn")
range_btn.scale = 0.1
range_btn.bottom = HEIGHT + 15
range_btn.left = 0
range_btn.cost = 100

power_btn = Actor("power_btn")
power_btn.scale = 0.1
power_btn.left = 105
power_btn.bottom = HEIGHT + 16
power_btn.cost = 100

add_leaf_btn = Actor("add_leaf_btn")
add_leaf_btn.scale = 0.1
add_leaf_btn.left = 210
add_leaf_btn.bottom = HEIGHT + 15
add_leaf_btn.cost = 100



def update():
    global leaf_CD
    global leaf_money
    global blow_range
    global blow_power


    leaf_CD += 1
    if leaf_CD >= 240:
        for i in range(leaf_num):
            leaf = Actor("leaf_shadow")
            leaf.final_size = random.randint(5,9)/10
            leaf.scale = leaf.final_size/2
            leaf.x = random.randint(0, WIDTH)
            leaf.y = random.randint(0, HEIGHT)
            leaf.pe = 0

            

            leaves.append(leaf)

        leaf_CD = 0
    
    for leaf in leaves:
        if player.distance_to(leaf) <= blow_range:
            leaf.point_towards(player)
            leaf.pe = blow_power
        if leaf.scale < leaf.final_size:
            leaf.scale += 0.05
            

                                                                                                                                

        if leaf.pe > 0:
            leaf.move_forward(-leaf.pe)
            leaf.pe -= 0.5
        



        if leaf.right <= 0:
            leaves.remove(leaf)
            leaf_money += 1
            break
        if leaf.left >= WIDTH:
            leaves.remove(leaf)
            leaf_money += 1
            break
        if leaf.bottom <= 0:
            leaves.remove(leaf)
            leaf_money += 1
            break
        if leaf.top >= HEIGHT:
            leaves.remove(leaf)
            leaf_money += 1
            break


def on_mouse_move(pos):
    player.pos = pos
    player.pre_angles.append(player.angle_to(prev_mouse_pos) - 180)
    player.pre_angles = player.pre_angles[1:]
    player.angle = sum(player.pre_angles)/len(player.pre_angles)
    # player.angle = int((player.angle_to(prev_mouse_pos) - 180)/45)*45
    prev_mouse_pos[0] = pos[0]
    prev_mouse_pos[1] = pos[1]
    
def on_mouse_down(pos):
    if HEIGHT-50<pos[1]<HEIGHT:
        if 0<pos[0]<100:
            print(f'{pos}, clicking range')
        elif 100<pos[0]<200:
            print(f'{pos}, clicking power')
        elif 200<pos[0]<300:
            print(f'{pos}, clicking add leaf')
        

    
    
def draw():
    screen.clear()
    screen.blit('bg', (0, 0))
    range_btn.draw()
    power_btn.draw()
    add_leaf_btn.draw()

    player.draw()
    for leaf in leaves:
        leaf.draw()

    screen.draw.text(str(leaf_money), (10, 30), fontsize = 60)



pgzrun.go()