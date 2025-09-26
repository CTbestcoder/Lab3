from constants import TABLES, MENU_ITEMS


class Restaurant:

    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]
        # TODO: uncomment next line
        self.menu_items = [MenuItem(name, price) for name, price in MENU_ITEMS]


class Table:

    def __init__(self, seats, location):

        table = []



        self.n_seats = seats
        self.location = location
        # TODO: Uncomment next line
        self.orders = [Order() for _ in range(seats)]


class Order:

    def __init__(self):

        self.items = []


    def add_item(self, menu_item):
        item = OrderItem(menu_item)
        self.items.append(item)

    def unordered_items(self):
        unordered = []
        for item in self.items:
            if item.ordered is False:
                unordered.append(item)
        return unordered

    def place_new_orders(self):
        unordered = self.unordered_items()
        for item in unordered:
            item.mark_as_ordered()





    def remove_unordered_items(self):
        unordered = self.unordered_items()
        for item in unordered:
            self.items.remove(item)

    def total_cost(self):
        pass





class OrderItem:
    def __init__(self,menu_item):
        self.ordered = False
        self.menu_item = menu_item

    def mark_as_ordered(self):
        self.ordered = True




class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price


