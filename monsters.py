from player import Creature
from elements import elements
import random
# with open("art/spider.txt", "r") as f:
#     spider_art = "".join(line for line in f.readlines())
monsters_and_art = {
    'spider': {
        'art': 'spider',
        'credit': 'Joan Stark',
    },
    # 'yeti': 'i am a rat',
    # 'golem': 'i am a rat',
    # 'colossus': 'i am a rat',
    # 'titan': 'i am a rat',
    # 'demon': 'i am a rat'
}
class Monster(Creature):
    element = ''
    art = '(>".")>'

    def __init__(self, element='ice', art='(>".")>', **kwargs):
        self.element = element
        self.art = art
        super().__init__(**kwargs)
        self.attack = 40

def choose_monster(floor):
    element = random.choice(list(elements.keys()))
    name = random.choice(list(monsters_and_art.keys()))
    return Monster(name=name, art= load_txt_art(monsters_and_art[name]['art']), element=element)

def load_txt_art(name):
    with open(f"art/monsters/{name}.txt", "r") as f:
        return f.read()
