import random

class Weapon:
    name = 'sword'
    element = '' # Water | Earth | Fire
    damage = ''
    accuracy = ''
    name = ''

    def __init__(self, name='', element='ice', accuracy=100, damage=1):
        self.name = name
        self.element = element
        self.accuracy = accuracy
        self.damage = damage

class Armor:
    name = 'armor'
    element = ''
    defense = ''
    bonus_health = ''

    def __init__(self, name='', element='ice', defense=1, bonus_health=0):
        self.name = name
        self.element = element
        self.defense = defense
        self.bonus_health = bonus_health


def choose_item(floor):
    if random.randint(1, 2) == 1:
        item = Armor(name='shield')
    else:
        item = Weapon(name='sword')
    return item