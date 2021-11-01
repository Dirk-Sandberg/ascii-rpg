from kivy.app import App
from kivy.core.window import Window
import monsters
from player import Creature
import elements
from kivy.core.audio import SoundLoader
from elements import element_colors
from inventory import InventoryScreen
from traits import TraitsScreen
from outlined_boxlayout import OutlinedBoxLayout
from kivy.properties import NumericProperty, BooleanProperty, ObjectProperty
import items
import random
from kivy.clock import mainthread
from traits import Attacker

with open("art/camp.txt", "r") as the_file:
    HOME_ART = the_file.read()


# sound = SoundLoader.load('sounds/mixkit-retro-arcade-game-over-470.wav')
# if sound:
#     print("Sound found at %s" % sound.source)
#     print("Sound is %.3f seconds" % sound.length)
#     sound.play()


class MainApp(App):
    floor = NumericProperty(0)
    player = Creature(attack=66, crit_chance=50)
    weapon = items.Weapon(element='normal')
    armor = None
    monster = Creature(attack=0, crit_chance=0)
    is_home = BooleanProperty(True)

    def on_start(self):
        self.show_homescreen(text="You're sitting in front of a campfire")

    def show_homescreen(self, text="You're back at the campfire"):
        self.root.ids.combat.text = HOME_ART
        self.add_line_to_text_log(text)

    def add_line_to_text_log(self, line):
        self.root.ids.log.add_line(line)

    def embark(self):
        widget = self.root.ids.combat
        self.root.ids.monster_toolbar.opacity = 1
        self.monster = monsters.choose_monster(self.floor)
        widget.text = self.render(self.monster.element, self.monster.art)
        # self.root.ids.monster_toolbar.text = f"{self.monster.element} {self.monster.name}--------HP: {self.monster.current_health} ATK: {self.monster.attack}"
        self.is_home = False

    def attack(self):
        # Calculate damage
        crit = random.randint(1, 100) <= self.player.crit_chance
        element_modifier = elements.calculate_modifier(self.weapon.element, self.monster.element)
        if crit:
            dealt_damage = self.player.crit_multiplier * self.player.attack * element_modifier - self.monster.defense
        else:
            dealt_damage = self.player.attack * element_modifier - self.monster.defense

        received_damage = self.monster.attack - self.player.defense
        self.monster.take_damage(dealt_damage)
        # self.root.ids.monster_toolbar.text = f"{self.monster.name}--------HP: {self.monster.current_health} ATK: {self.monster.attack}"
        if self.monster.current_health <= 0:
            self.add_line_to_text_log(f"You killed the {self.monster.name}")
            self.disembark()
            return
        self.player.take_damage(received_damage)
        if crit:
            self.add_line_to_text_log(f"Your elemental bonus was {element_modifier}. You crit the monster for {dealt_damage}. Took {self.monster.attack - self.player.defense} damage from {self.monster.name}")
        else:
            self.add_line_to_text_log(f"Your elemental bonus was {element_modifier}. You hurt the monster for {dealt_damage}. Took {self.monster.attack - self.player.defense} damage from {self.monster.name}")
        print("???", self.monster.current_health)

    def disembark(self):
        self.root.ids.combat.text = HOME_ART
        self.root.ids.monster_toolbar.opacity = 0
        item = items.choose_item(self.floor)
        self.root.ids.traits_screen.add_trait(Attacker())
        self.root.ids.inventory.add_item_to_inventory(item)
        self.add_line_to_text_log(f"You looted a {item.name} off the {self.monster.name}'s dead body.")
        self.add_line_to_text_log("You made it to the next floor.")
        self.floor += 1
        self.is_home = True

    def render(self, element, text):
        return f"[font=RobotoMono-Regular][color={element_colors[element]}]{text}[/color][/font]"

    @mainthread
    def change_screen(self, new_screen):
        self.root.current = new_screen



MainApp().run()
