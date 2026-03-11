class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        self.inventory[item] = quantity
        print(f"{item} added with quantity {quantity}")