from player import Creature
from elements import elements
import random
from kivy.properties import NumericProperty
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

    def __init__(self, element='ice', art='(>".")>', *args, **kwargs):
        self.element = element
        self.art = art
        super().__init__(*args, **kwargs)

    def choose_new_monster(self, floor):
        element = random.choice(list(elements.keys()))
        name = random.choice(list(monsters_and_art.keys()))
        self.attack = random.choice(range(100))
        self.max_health = random.choice(range(100))
        self.current_health = self.max_health
        self.name = name
        self.element = element
        self.art = load_txt_art(monsters_and_art[name]['art'])

def load_txt_art(name):
    with open(f"art/monsters/{name}.txt", "r") as f:
        return f.read()
