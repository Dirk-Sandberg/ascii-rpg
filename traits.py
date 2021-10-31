from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class Trait:
    def __init__(self, name, description, attack_modifier=0, defense_modifier=0):
        self.name = name
        self.description = description
        self.attack_modifier = attack_modifier
        self.defense_modifier = defense_modifier


class Attacker(Trait):
    def __init__(self):
        super().__init__('Attacker', 'deal 5 more damage', 5)

class TraitsScreen(Screen):
    def add_trait(self, trait):
        self.ids.traits_scrollview.add_widget(Label(text=trait.name+'\n'+trait.description))
