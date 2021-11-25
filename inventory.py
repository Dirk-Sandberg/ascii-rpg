from kivy.uix.screenmanager import Screen
from kivy.app import App
from items import Weapon, Armor
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import mainthread
from kivy.uix.label import Label
import json

class InventoryScreen(Screen):
    inventory = ListProperty([])
    armor = ObjectProperty(Armor())
    weapon = ObjectProperty(Weapon())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compare_stats(self, item):
        print("Comparing stats with ", item)
        all_stat_strings = []
        for stat in item.modifiable_stats:
            all_stat_strings.append(self.stat_string(item, stat))
        stat_strings = []
        for stat_string in all_stat_strings:
            if stat_string:
                stat_strings.append(stat_string)

        return "\n".join(line for line in stat_strings)

    def stat_string(self, item, attribute):
        if item.type == 'weapon':
            print("weapon stat")
            current_item = self.weapon
        if item.type == 'armor':
            current_item = self.armor
            print("armor stat")
        try:
            value = getattr(item, attribute)
        except:
            # stat doesn't exist on this piece of equipment
            return ''
        diff = value - getattr(current_item, attribute)
        if diff > 0:
            # Green
            color = "32CD32"
            operator = '+'
        elif diff < 0:
            # Red
            color = "FF0000"
            operator = '-'
        elif diff == 0:
            color = "FFFFFF"
            operator = ''
        if diff:
            return f"{attribute.replace('_',' ').title()}: {value} [color={color}]({operator}{abs(diff)})[/color]"
        else:
            return f"{attribute.replace('_', ' ').title()}: {value} [color={color}][/color]"

    def add_item_to_inventory(self, item):
        if len(self.inventory) > 2:
            self.inventory.pop(0)
        self.inventory.append(item)

    @mainthread
    def equip_item(self, new_item, old_item_inventory_slot):
        player = App.get_running_app().player

        if new_item.type == 'weapon':
            old_item = self.weapon
        if new_item.type == 'armor':
            old_item = self.armor
        print("Equipping", new_item.name, "replacing", old_item.name)
        print("New, old atk", new_item.attack, old_item.attack)
        print("New, old def", new_item.defense, old_item.defense)

        if new_item.type == 'weapon':
            self.weapon = new_item
        if new_item.type == 'armor':
            self.armor = new_item

        self.inventory[old_item_inventory_slot] = old_item
        player.attack = player.attack + new_item.attack - old_item.attack
        player.defense = player.defense + new_item.defense - old_item.defense
        print("New values", player.attack, player.defense)




