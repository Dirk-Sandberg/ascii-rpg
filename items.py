import random

class Weapon:
    name = '??weapon'
    type = 'weapon'
    element = '' # Water | Earth | Fire
    attack = ''
    defense = 0
    accuracy = ''

    def __init__(self, name='??weapon', element='ice', accuracy=100, attack=1):
        self.name = name
        self.element = element
        self.accuracy = accuracy
        self.attack = attack

class Armor:
    name = '??armor'
    type = 'armor'
    element = '' # Water | Earth | Fire
    attack = 0
    defense = ''
    bonus_health = ''

    def __init__(self, name='??armor', element='ice', defense=1, bonus_health=0):
        self.name = name
        self.element = element
        self.defense = defense
        self.bonus_health = bonus_health


def choose_item(floor):
    if random.randint(1, 2) == 1:
        item = Armor(name='shield', defense = 5)
    else:
        item = Weapon(name='sword', attack = 5)
    return item