from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class Creature(Widget):
    name = ''
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

    def __init__(self, name = '',
                 max_health=100,
                 number_of_attacks=1,
                 attack=1,
                 defense=0,
                 crit_chance=0,
                 crit_multiplier=2,
                 lifesteal=0,
                 evasion=0,
                 accuracy=100):
        self.name = name
        self.max_health = max_health
        self.number_of_attacks = number_of_attacks
        self.attack = attack
        self.defense = defense
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.lifesteal = lifesteal
        self.evasion = evasion
        self.accuracy = accuracy

    def take_damage(self, damage):
        self.current_health -= damage



