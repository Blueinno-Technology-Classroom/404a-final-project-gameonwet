import pgzrun
import random
import math
from pgzhelper import *


WIDTH = 1024
HEIGHT = 768

player = Actor("leaf.png")
player.pos = (WIDTH / 2, HEIGHT / 2)

mouse_pos = [0, 0]
def draw():
    
    player.draw