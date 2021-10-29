from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
kv = Builder.load_string("""
<InventoryScreen@Screen>:
    on_pre_enter:
        print("Entered inventory screen")
    BoxLayout:
        Button:
            text: "Back"
            on_release: app.root.current = 'home_screen'
        BoxLayout:
            orientation: 'vertical'
            GridLayout:
                cols: 2
                Label:
                    id: weapon
                Label:
                    id: armor
            GridLayout:
                id: inventory
                rows: 1
                Label:
                    id: item0
                Label:
                    id: item1
                Label:
                    id: item2
""")

class InventoryScreen(Screen):
    inventory = []

    def build(self):
        return kv
    def add_item(self, item):
        if len(self.inventory) > 3:
            self.inventory.pop(0)
        self.inventory.append(item)
        for i, item in enumerate(self.inventory):
            ids = self.ids
            print("HAA", ids)
            ids['item'+str(i)].text = item.name
