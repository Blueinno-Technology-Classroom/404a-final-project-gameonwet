import pgzrun
import random
import math
from pgzhelper import *

WIDTH = 1024
HEIGHT = 768

player = Actor("playership1_blue")
player.pos = (WIDTH / 2, HEIGHT / 2)
player.hp = 100
laser_count = 0
enemies = []
lasers = []
elasers = []

mouse_pos = [0, 0]

def update():
    global laser_count
    if player.hp > 0:

        player.angle = player.angle_to(mouse_pos) - 90

        if random.randint(0, 100) < 2:
            enemy = Actor("enemyred2")
            
            from_dir = random.randint(0, 3)
            if from_dir == 0:
                enemy.x = random.randint(0, WIDTH)
                enemy.y = 0
            elif from_dir == 1:
                enemy.x = 0
                enemy.y = random.randint(0, HEIGHT)
            elif from_dir == 2:
                enemy.x = random.randint(0, WIDTH)
                enemy.y = HEIGHT
            elif from_dir == 3:
                enemy.x = WIDTH
                enemy.y = random.randint(0, HEIGHT)

            enemy.point_towards(player)
            enemies.append(enemy)
        




        for e in enemies:
            e.move_forward(2)
            if e.left > WIDTH or e.right < 0 or e.top > HEIGHT or e.bottom < 0:
                enemies.remove(e)
            if player.colliderect(e):
                player.hp -= 5
                enemies.remove(e)
                continue
            if random.randint(0, 100) <2:
                elaser = Actor('laserred07')
                elaser.pos = e.pos
                elaser.point_towards(player)
                elasers.append(elaser)

        if keyboard.space:
            laser_count += 1
        if laser_count >= 30:
                laser = Actor('laserblue07')
                laser.pos = player.pos
                laser.angle = player.angle + 90
                lasers.append(laser)
                laser_count = 0

        if keyboard.a:
            player.x -= 5
        if keyboard.d:
            player.x += 5
        if keyboard.w:
            player.y -= 5
        if keyboard.s:
            player.y += 5

        if player.left <= 0:
            player.left = 0
        if player.right >= WIDTH:
            player.right = WIDTH
        if player.top <= 0:
            player.top = 0
        if player.bottom >= HEIGHT:
            player.bottom = HEIGHT

        for l in lasers:
            l.move_forward(10)
            if l.bottom < 0:
                lasers.remove(l)
                continue
            for e in enemies:
                if l.colliderect(e):
                    lasers.remove(l)
                    enemies.remove(e)
                    break

        for el in elasers:
            el.move_forward(5)
            if el.top >= HEIGHT:
                elasers.remove(el)
                continue
            if player.colliderect(el):
                player.hp -= 1
                elasers.remove(el)
                break

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((0, 0), (WIDTH * player.hp / 100, 20)), 'green')
    player.draw()
    
    for e in enemies:
        e.draw()

    for l in lasers:
        l.draw()

    for el in elasers:
        el.draw()
pgzrun.go()
