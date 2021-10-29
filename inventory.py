from kivy.uix.screenmanager import Screen
from kivy.app import App
from items import Weapon, Armor
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import mainthread
from kivy.uix.label import Label


class InventoryScreen(Screen):
    inventory = ListProperty([])
    armor = ObjectProperty(Armor())
    weapon = ObjectProperty(Weapon())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_item_to_inventory(self, item):
        if len(self.inventory) > 2:
            self.inventory.pop(0)
        self.inventory.append(item)

    def add_trait(self, trait):
        self.ids.traits_scrollview.add_widget(Label(text=trait.name+'\n'+trait.description))

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

        self.ids['item'+str(old_item_inventory_slot)].text = old_item.name
        player.attack = player.attack + new_item.attack - old_item.attack
        player.defense = player.defense + new_item.defense - old_item.defense

        if new_item.type == 'weapon':
            self.weapon = new_item
        if new_item.type == 'armor':
            self.armor = new_item
        print("New values", player.attack, player.defense)




