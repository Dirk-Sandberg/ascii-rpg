from player import Creature
from elements import elements
import random

monsters_and_art = {
    'rat': 'i am a rat',
    'yeti': 'i am a rat',
    'golem': 'i am a rat',
    'colossus': 'i am a rat',
    'titan': 'i am a rat',
    'demon': 'i am a rat'
}
class Monster(Creature):
    element = ''
    art = '(>".")>'

    def __init__(self, element='ice', art='(>".")>', **kwargs):
        self.element = element
        self.art = art
        super().__init__(**kwargs)

def choose_monster(floor):
    element = random.choice(list(elements.keys()))
    name = random.choice(list(monsters_and_art.keys()))
    return Monster(name=name, art= monsters_and_art[name], element=element)
