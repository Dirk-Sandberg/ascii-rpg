from player import Creature
import random

class Monster(Creature):
    pass
def choose_monster(floor):
    monsters = [Monster('Monster1'), Monster('Monster3'), Monster('Monster2')]
    return random.choice(monsters)
