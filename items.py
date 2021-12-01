import random
import os
from elements import elements

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
    crit_chance = 0
    crit_multiplier = 0
    lifesteal = 0
    accuracy = 0
    number_of_attacks = 1
    art = ''
    modifiable_stats = [
        'attack',
        'crit_chance',
        'crit_multiplier',
        'lifesteal',
        'accuracy',
        'number_of_attacks'
    ]

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
    evasion = 0
    defense = ''
    bonus_health = 0
    art = ''
    modifiable_stats = [
        'defense',
        'bonus_health',
        'evasion'
    ]

    def __init__(self, name=STARTING_ARMOR, element='ice', art=armor[STARTING_ARMOR], defense=1, bonus_health=0):
        self.name = name
        self.element = element
        self.defense = defense
        self.bonus_health = bonus_health
        self.art = art


def choose_item(floor):
    element = random.choice(list(elements.keys()))
    # Add some spice to the names, e.g. instead of "Stick" -> "Glacial Stick of freezing"
    # Change elements dict to have adjectives, prefixes, and postfixes?
    item_name_prefix = random.choice(elements[element]) # Choose a random prefix
    item_name_postfix = ''

    if random.randint(1, 2) == 1:
        # Armor item
        item_name = random.choice(list(armor.keys()))
        item_art = armor[item_name]
        stats = {}
        for stat in Armor.modifiable_stats:
            stats[stat] = random.choice(range(1, 100))
        item = Armor(name=item_name_prefix + ' ' + item_name, art=item_art)
        for stat in stats:
            setattr(item, stat, stats[stat])
    else:
        # Weapon item
        item_name = random.choice(list(weapons.keys()))
        item_art = weapons[item_name]
        stats = {}
        for stat in Weapon.modifiable_stats:
            stats[stat] = random.choice(range(1, 100))
        item = Weapon(name=item_name_prefix + ' ' + item_name, art=item_art)
        for stat in stats:
            setattr(item, stat, stats[stat])

    # Set elemental type
    item.element = element

    return item