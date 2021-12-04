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
from monsters import Monster
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
    player = Creature()
    monster = Monster()
    weapon = items.Weapon(element='normal')
    armor = None
    is_home = BooleanProperty(True)

    def on_start(self):
        self.show_homescreen(text=self.render("You're sitting in front of a campfire"))

    def show_homescreen(self, text="You're back at the campfire"):
        self.root.ids.combat.text = self.render(HOME_ART)
        self.add_line_to_text_log(self.render(text))

    def add_line_to_text_log(self, line):
        self.root.ids.log.add_line(line)

    def embark(self):
        widget = self.root.ids.combat
        self.root.ids.monster_toolbar.opacity = 1
        self.monster.choose_new_monster(self.floor)
        widget.text = self.render(self.monster.art, self.monster.element)
        self.is_home = False

    def disembark(self):
        self.show_homescreen()
        self.root.ids.monster_toolbar.opacity = 0
        item = items.choose_item(self.floor)
        self.root.ids.traits_screen.add_trait(Attacker())
        self.root.ids.inventory.add_item_to_inventory(item)
        a_or_an = 'an' if item.name[0].lower() in ['a','e','i','o','u'] else 'a'
        self.add_line_to_text_log(f"You looted {a_or_an} {self.render(item.name, item.element)} off the {self.monster.name}'s dead body.")
        # self.add_line_to_text_log("You made it to the next floor.")
        self.floor += 1
        self.is_home = True

    def render(self, text, element='normal'):
        return f"[font=RobotoMono-Regular][color={element_colors[element]}]{text}[/color][/font]"

    @mainthread
    def change_screen(self, new_screen):
        self.root.current = new_screen

    def calculate_crit_stats(self):
        """Do any necessary calculations based on traits."""
        crit = random.randint(1, 100) <= self.player.crit_chance
        if crit:
            crit_multiplier = self.player.crit_multiplier
        else:
            crit_multiplier = 1.0
        return {
            'crit': crit,
            'crit_multiplier': crit_multiplier
        }

    def attack(self):
        player = self.player
        damages_dealt = []

        for attack_number in range(int(player.number_of_attacks/player.number_of_attacks)):
            # Calculate elemental bonus
            element_modifier = elements.calculate_modifier(self.weapon.element, self.monster.element)

            # Calculate crit bonus. multiplier is 1.0 if no crit
            crit_stats = self.calculate_crit_stats()

            # Calculate additive trait bonus
            base_damage_bonus = 0
            multiplicative_bonus = 1
            for trait in player.traits:
                base_damage_bonus = trait.modify_base_damage(base_damage_bonus) # attack_number as argument for poison
                multiplicative_bonus = trait.modify_multiplicative_damage(multiplicative_bonus)

            # Calculate multiplicative trait bonus
            damage_dealt = self.player.attack + base_damage_bonus
            damage_dealt *= crit_stats['crit_multiplier']
            damage_dealt *= multiplicative_bonus
            damage_dealt *= element_modifier
            damage_dealt -= self.monster.defense
            damages_dealt.append(damage_dealt)


        # Display text log
        self.add_line_to_text_log(f"Crit? {crit_stats['crit']}. Damage dealt: {damages_dealt}")
        # self.add_line_to_text_log(f"Your elemental bonus was {element_modifier}. You CRIT the monster for {damage_dealt}. Took {received_damage} damage from {self.monster.name}")

        # Subtract monster HP
        self.monster.take_damage(damage_dealt)
        if self.monster.current_health <= 0:
            self.add_line_to_text_log(
                self.render(f"You killed the {self.monster.name}"))
            self.disembark()
            return

        # Player takes damage
        received_damage = self.monster.attack - self.player.defense
        if received_damage < 0:
            # Shield can't block so much damage that you take negative damage
            received_damage = 0

        for trait in player.traits:
            received_damage += trait.modify_damage_received(sum(damages_dealt))

        self.player.take_damage(received_damage)



MainApp().run()
