from player import Creature
from elements import elements
import random
import os

monsters_folder = "art/monsters"
monster_files = os.listdir(monsters_folder)
monsters = []
for monster_file in monster_files:
    with open(f"{monsters_folder}/{monster_file}", "r") as f:
        monster_name = monster_file.replace('.txt', '')
        file_contents = f.read()
        monsters.append({
            'name': monster_name,
            'art': file_contents[:file_contents.find('credit')],
            'credit': file_contents[file_contents.find('credit')+len('credit\n'):]
        })

class Monster(Creature):
    element = ''
    art = '(>".")>'

    def __init__(self, element='ice', art='(>".")>', *args, **kwargs):
        self.element = element
        self.art = art
        super().__init__(*args, **kwargs)

    def choose_new_monster(self, floor):
        element = random.choice(list(elements.keys()))
        monster = random.choice(monsters)
        self.attack = random.choice(range(1, 100))
        self.max_health = random.choice(range(1, 100))
        self.current_health = self.max_health
        self.name = monster['name']
        self.element = element
        self.art = monster['art']
