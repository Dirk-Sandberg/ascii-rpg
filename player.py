from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class Creature(Widget):
    current_health = NumericProperty(100)
    max_health = 100
    number_of_attacks = 1
    attack = 1
    defense = 0
    crit_chance = 0
    crit_multiplier = 0
    lifesteal = 0
    evasion = 0
    accuracy = 100
    gold = 0
    name = ''
    element = ''

    def take_damage(self, damage):
        self.current_health -= damage

class Player(Creature):
    name = 'you'
    attack = 26

class Monster(Creature):
    def __init__(self, name='Monster'):
        self.name = name

class Weapon:
    element = '' # Water | Earth | Fire
    damage = ''
    accuracy = ''
    name = ''

class Armor:
    element = ''
    defense = ''
    bonus_health = ''


