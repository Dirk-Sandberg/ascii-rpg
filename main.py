from kivy.app import App
from kivy.core.window import Window
from player import Player, Monster

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
    showing_map = BooleanProperty(False)

    def add_line_to_text_log(self, line):
        # This could go in a separate class for the Log text area
        lines = []
        colors = ['CCCCCC', '999999', '666666', '333333']
        current_lines = self.root.ids.log.text.splitlines()[::-1]
        for i, text in enumerate(current_lines):
            if i < 4:
                text = text[text.find(']')+1:text.find('[/')]
                text = f'[color={colors[i]}]{text}[/color]'
                lines.append(text)
        while len(lines) < 2:
            lines = ['\n'] + lines
        lines = lines[::-1]
        lines.append(f'[color=FFFFFF]{line}[/color]')
        self.root.ids.log.text = '\n'.join(x for x in lines)

    def toggle_overlay_map(self):
        self.showing_map = not self.showing_map

    def embark(self):
        widget = self.root.ids.combat
        monsters = [Monster('Monster1'), Monster('Monster3'), Monster('Monster2')]
        monster = random.choice(monsters)
        self.root.ids.monster_toolbar.opacity = 1
        self.monster = monster
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

    def on_start(self):
        ids = self.root.ids
        widgets = [ids.combat, ids.actions]
        for widget in widgets:
            widget.bind(on_ref_press=self.ref_press)

    def render(self, object):
        if object.element == 'water':
            color = 'ff3333'
        else:
            color = '3333ff'
        return f"[color{color}][ref]{object.text}[/ref][/color]"

    def ref_press(self, widget, ref):
        if ref == 'zz':
            self.add_line_to_text_log('omg wow')
        if ref == 'addMap':
            self.toggle_overlay_map()
        # print("REF", ref)


MainApp().run()
