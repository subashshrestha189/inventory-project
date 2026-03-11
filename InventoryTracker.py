class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        self.inventory[item] = quantity
        print(f"{item} added with quantity {quantity}")

    def checkStockLevel(self, item):
        quantity = self.inventory.get(item, 0)
        print(f"{item} stock level: {quantity}")
        return quantity
    
    def alertLowStock(self, item, threshold=5):
        quantity = self.inventory.get(item, 0)
        if quantity < threshold:
            print(f"ALERT: {item} is low on stock! Only {quantity} left.")

