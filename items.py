import random
import os

weapons_folder = "art/weapons"
weapon_files = os.listdir(weapons_folder)
weapons = {}
for weapon_file in weapon_files:
    with open(f"{weapons_folder}/{weapon_file}", "r") as f:
        weapon_name = weapon_file.replace('.txt', '')
        weapons[weapon_name] = f.read()

armor_folder = "art/armor"
armor_files = os.listdir(armor_folder)
armor = {}
for armor_file in armor_files:
    with open(f"{armor_folder}/{armor_file}", "r") as f:
        armor_name = armor_file.replace('.txt', '')
        armor[armor_name] = f.read()


STARTING_WEAPON = 'Stick'
STARTING_ARMOR = 'Rags'
class Weapon:
    name = ''
    type = 'weapon'
    element = '' # Water | Earth | Fire
    attack = ''
    defense = 0
    accuracy = ''
    art = ''

    def __init__(self, name=STARTING_WEAPON, element='ice', art=weapons[STARTING_WEAPON], accuracy=100, attack=1):
        self.name = name
        self.element = element
        self.accuracy = accuracy
        self.attack = attack
        self.art = art

class Armor:
    name = '??armor'
    type = 'armor'
    element = '' # Water | Earth | Fire
    attack = 0
    defense = ''
    bonus_health = ''
    art = ''

    def __init__(self, name=STARTING_ARMOR, element='ice', art=armor[STARTING_ARMOR], defense=1, bonus_health=0):
        self.name = name
        self.element = element
        self.defense = defense
        self.bonus_health = bonus_health
        self.art = art


def choose_item(floor):
    if random.randint(1, 2) == 1:
        item_name = random.choice(list(armor.keys()))
        item_art = armor[item_name]
        item = Armor(name=item_name, art=item_art, defense=5)
    else:
        item_name = random.choice(list(weapons.keys()))
        item_art = weapons[item_name]
        item = Weapon(name=item_name, art=item_art, attack=5)
    return item