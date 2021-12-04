from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.app import App


class Trait:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def modify_damage_received(self, damage, *args, **kwargs):
        """Meant to be overridden by each trait. This adds to damage received."""
        return damage

    def modify_base_damage(self, damage, *args, **kwargs):
        #
        # SHOULD modifying base damage just be as simple as adding to a players attack instead
        # of doing this weird function?
        #
        """Meant to be overrided by each trait. This adds to base damage in an
        additive manner. It will be multiplied by multiplicative traits later by
        the modify_multiplicative_damage function.
        """
        return damage

    def modify_multiplicative_damage(self, percent_bonus, *args, **kwargs):
        """Meant to be overrided by each trait. This adds to base damage in an
        additive manner. It will be multiplied by multiplicative traits later by
        the modify_damage_multiplier function.
        """
        return percent_bonus


class Attacker(Trait):
    def __init__(self):
        super().__init__('Attacker', 'Add 5 to base damage')

    def modify_base_damage(self, damage):
        return damage + 5

class Vampire(Trait):
    lifesteal_factor = 10 # Percent
    def modify_damage_received(self, damage_dealt):
        """Lessen damage received by how much damage was dealt, with possibility
        of healing the player."""
        return damage_dealt * self.lifesteal_factor / 100



class TraitsScreen(Screen):
    def add_trait(self, trait):
        self.ids.traits_scrollview.add_widget(Label(text=trait.name+'\n'+trait.description))
        App.get_running_app().player.traits.append(trait)
