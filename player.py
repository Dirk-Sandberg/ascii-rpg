from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class Creature(Widget):
    name = ''
    max_health = NumericProperty(100)
    current_health = NumericProperty(100)
    current_health_possibly_negative = NumericProperty(100) # Used to not let people get HP by swapping shields at low HP
    experience = NumericProperty(0)

    traits = []  # List of all traits that modify damage

    # Offensive stats, modifiable by weapons
    number_of_attacks = NumericProperty(1)
    attack = NumericProperty(19)
    crit_chance = NumericProperty(0)
    crit_multiplier = NumericProperty(0)
    lifesteal = NumericProperty(0)
    accuracy = NumericProperty(100)

    # Defensive stats, modifiable by armor
    bonus_health = NumericProperty(0)
    old_bonus_health = NumericProperty(0) # Used to find difference between new and old bonus health stats
    defense = NumericProperty(0)
    evasion = NumericProperty(0)

    def on_bonus_health(self, *args):
        self.max_health = self.max_health + (self.bonus_health - self.old_bonus_health)
        self.current_health = self.current_health_possibly_negative + (self.bonus_health - self.old_bonus_health)
        self.current_health_possibly_negative = self.current_health
        if self.current_health <= 0:
            self.current_health = 1
        self.old_bonus_health = self.bonus_health

    def take_damage(self, damage):
        self.current_health -= damage
        self.current_health_possibly_negative = self.current_health



