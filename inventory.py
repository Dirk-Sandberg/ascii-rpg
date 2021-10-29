from kivy.uix.screenmanager import Screen


class InventoryScreen(Screen):
    inventory = []

    def add_item(self, item):
        if len(self.inventory) > 2:
            self.inventory.pop(0)
        self.inventory.append(item)
        ids = self.ids
        for i, item in enumerate(self.inventory):
            print("HAA", ids)
            ids['item'+str(i)].text = item.name
