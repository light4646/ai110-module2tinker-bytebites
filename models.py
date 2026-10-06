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

    def add_item(self, item):
        """Add a MenuItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category):
        """Return items whose category matches (case-insensitive)."""
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_price(self, descending=False):
        """Return items sorted by price, cheapest first unless descending=True."""
        return sorted(self.items, key=lambda item: item.price, reverse=descending)

    def sort_by_popularity(self):
        """Return items sorted from most to least popular."""
        return sorted(self.items, key=lambda item: item.popularity, reverse=True)


class Order:
    """One transaction: the items a customer selected."""

    def __init__(self, items=None):
        self.items = list(items) if items else []

    def add_item(self, item):
        """Add a selected MenuItem to this order."""
        self.items.append(item)

    def compute_total(self):
        """Return the total cost of all items, rounded to cents (0.0 if empty)."""
        return round(sum(item.price for item in self.items), 2)


class Customer:
    """A user with a name and a history of past orders."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        """Record a completed order in this customer's purchase history."""
        self.purchase_history.append(order)

    def is_verified(self):
        """A customer is a real user if they have at least one past purchase."""
        return len(self.purchase_history) > 0


if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 10.00, "Entrees", 4.5)
    soda = MenuItem("Large Soda", 5.00, "Drinks", 3.9)
    tea = MenuItem("Iced Tea", 3.50, "Drinks", 4.2)
    cake = MenuItem("Chocolate Cake", 6.25, "Desserts", 4.8)

    menu = Menu([burger, soda, tea])
    menu.add_item(cake)
    print("Drinks:", menu.filter_by_category("drinks"))
    print("By price:", menu.sort_by_price())
    print("By popularity:", menu.sort_by_popularity())

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print("Order total:", order.compute_total())

    customer = Customer("Nour")
    print("Verified before purchase:", customer.is_verified())
    customer.add_purchase(order)
    print("Verified after purchase:", customer.is_verified())
