class Controller:
    """
    Do not modify this class, just its subclasses. Represents common behaviour of all
    Controllers. Python has a mechanism for explicitly dealing with abstract classes,
    which we haven't seen yet; raising RuntimeError gives a similar effect.
    """

    def __init__(self, view, restaurant):
        self.view = view
        self.restaurant = restaurant

    def add_item(self, item):
        raise RuntimeError('add_item: some subclasses must implement')

    def cancel(self):
        raise RuntimeError('cancel: some subclasses must implement')

    def create_ui(self):
        raise RuntimeError('create_ui: all subclasses must implement')

    def done(self):
        raise RuntimeError('done: some subclasses must implement')

    def place_order(self):
        raise RuntimeError('place_order: some subclasses must implement')

    def seat_touched(self, seat_number):
        raise RuntimeError('seat_touched: some subclasses must implement')

    def table_touched(self, table_index):
        raise RuntimeError('table_touched: some subclasses must implement')


class RestaurantController(Controller):

    def __init__(self, view, restaurant):
        super().__init__(view, restaurant)


    def create_ui(self):
        self.view.create_restaurant_ui()

    def table_touched(self, table_number):

        table = self.restaurant.tables[table_number]
        self.view.table_touched(table_number)


class TableController(Controller):
    def __init__(self, view, restaurant, table):
        self.table = table
        super().__init__(view, restaurant)

    def create_ui(self):
        self.view.create_table_ui(table=self.table)



class OrderController(Controller):
    def __init__(self, view, restaurant, table, seat_number):
        self.table = table
        self.order = table.order
        super().__init__(view, restaurant)

    def create_ui(self):
        self.view.create_order_ui(order=self.order)

    def add_item(self, menu_item):
        self.order.add_item(menu_item)
        self.create_ui()

    def update_order(self):
        self.order.place_new_orders()
        tc = TableController(self.view, self.restaurant, self.table)
        self.view.set_controller(tc)

    def cancel(self):
        self.order.remove_unordered_items()
        tc = TableController(self.view, self.restaurant, self.table)
        self.view.set_controller(tc)






    #super().create_ui()




