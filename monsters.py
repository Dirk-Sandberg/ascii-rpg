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
    element = ''
    def __init__(self, element='ice', **kwargs):
        self.element = element
        super().__init__(**kwargs)

def choose_monster(floor):
    element = random.choice(list(elements.keys()))
    name = element + ' ' + random.choice(monsters)
    return Monster(name=name, element=element)
