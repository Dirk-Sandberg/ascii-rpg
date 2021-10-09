from player import Creature
from elements import elements
import random

monsters = [
    'rat',
    'yeti',
    'golem',
    'colossus',
    'titan',
    'demon'
]
class Monster(Creature):
    pass

def choose_monster(floor):
    element = random.choice(list(elements.keys()))
    name = element + ' ' + random.choice(monsters)
    return Monster(name=name, element=element)
