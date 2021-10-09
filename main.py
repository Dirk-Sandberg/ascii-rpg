from kivy.app import App
from kivy.core.window import Window
import monsters
from player import Player

from kivy.core.audio import SoundLoader
from kivy.properties import BooleanProperty, ObjectProperty, Property
import random
# sound = SoundLoader.load('mixkit-retro-arcade-game-over-470.wav')
# if sound:
#     print("Sound found at %s" % sound.source)
#     print("Sound is %.3f seconds" % sound.length)
#     sound.play()


class MainApp(App):
    floor = 0
    player = Player()
    monster = None

    def add_line_to_text_log(self, line):
        self.root.ids.log.add_line(line)

    def embark(self):
        widget = self.root.ids.combat
        self.root.ids.monster_toolbar.opacity = 1
        self.monster = monsters.choose_monster(self.floor)
        widget.text = "You are fighting a " + self.monster.name

    def attack(self):
        received_damage = self.monster.attack - self.player.defense
        dealt_damage = self.player.attack - self.monster.defense
        self.monster.take_damage(dealt_damage)
        self.root.ids.monster_toolbar.text = f"{self.monster.name}\n--------\nHP: {self.monster.current_health} ATK: {self.monster.attack}"
        if self.monster.current_health <= 0:
            self.add_line_to_text_log(f"You killed the {self.monster.name}")
            self.disembark()
            return
        self.player.take_damage(received_damage)
        self.add_line_to_text_log(f"You took {self.monster.attack - self.player.defense} damage from {self.monster.name}")

    def disembark(self):
        self.root.ids.combat.text = ''
        self.root.ids.monster_toolbar.opacity = 0
        self.add_line_to_text_log("You are back at the village.")

    def render(self, object):
        if object.element == 'water':
            color = 'ff3333'
        else:
            color = '3333ff'
        return f"[color{color}][ref]{object.text}[/ref][/color]"


MainApp().run()
