# ByteBites models
# Customer - a user with a name and purchase history (used to verify real users)
# MenuItem - a food item with name, price, category, and popularity rating
# Menu     - the full collection of items; supports filtering by category
# Order    - one transaction grouping selected items and computing the total


class MenuItem:
    """A single food item for sale."""

    def __init__(self, name, price, category, popularity):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity

    def __repr__(self):
        return f"MenuItem({self.name!r}, ${self.price:.2f}, {self.category!r}, {self.popularity})"


class Menu:
    """The full collection of items the app sells."""

    def __init__(self, items=None):
        self.items = list(items) if items else []


class Order:
    """One transaction: the items a customer selected."""

    def __init__(self, items=None):
        self.items = list(items) if items else []


class Customer:
    """A user with a name and a history of past orders."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []
