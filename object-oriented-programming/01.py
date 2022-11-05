class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.total_quantity = 0

    def add_item(self, name, price, quantity):
        if name in self.items or (quantity + self.total_quantity) > self.max_capacity:
            return False
        self.items[name] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.total_quantity += quantity
        return True

    def delete_item(self, name):
        if name in self.items:
            self.total_quantity -= self.items[name]['quantity']
            del self.items[name]
            return True
        return False

    def get_items_in_price_range(self, min_price, max_price):
        items_by_price_range = []
        for item in self.items.values():
            if item['price'] >= min_price and item['price'] <= max_price:
                items_by_price_range.append(item['name'])
        return items_by_price_range

    def get_most_stocked_item(self):
        highest = 0
        item_name = None
        for item in self.items.values():
            if item['quantity'] > highest:
                highest = item['quantity']
                item_name = item['name']
        return item_name


inventory = Inventory(4)
inventory.add_item('Chocolate', 4.99, 4)
inventory.delete_item('Chocolate')
inventory.delete_item('Chocolate')
inventory.delete_item('Bread')
inventory.add_item('Chocolate', 4.99, 2)
inventory.add_item('Bread', 4.99, 2)
inventory.get_most_stocked_item()
