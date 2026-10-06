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


def format_items(items, title):
    """Return items as a readable table with a title, for printing in the terminal."""
    width = 44
    lines = [title, "-" * width]
    if not items:
        lines.append("(no items)")
    for item in items:
        lines.append(f"{item.name:<18}{'$' + format(item.price, '.2f'):>8}   {item.category:<10}★{item.popularity}")
    return "\n".join(lines)


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

    def display(self, items=None, title="ByteBites Menu"):
        """Return the menu (or a filtered/sorted list of its items) as a readable table."""
        return format_items(self.items if items is None else items, title)


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

    def receipt(self):
        """Return the order as a readable receipt ending with the total."""
        width = 44
        lines = ["Your Order", "-" * width]
        lines += [f"{item.name:<34}{'$' + format(item.price, '.2f'):>10}" for item in self.items] or ["(no items)"]
        lines += ["-" * width, f"{'Total':<34}{'$' + format(self.compute_total(), '.2f'):>10}"]
        return "\n".join(lines)


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
    print(menu.display())
    print()
    print(menu.display(menu.filter_by_category("drinks"), "Drinks only"))
    print()
    print(menu.display(menu.sort_by_price(), "Sorted by price (cheapest first)"))
    print()
    print(menu.display(menu.sort_by_popularity(), "Sorted by popularity (most popular first)"))
    print()

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print(order.receipt())
    print()

    customer = Customer("Nour")
    print(f"{customer.name} verified before purchase: {customer.is_verified()}")
    customer.add_purchase(order)
    print(f"{customer.name} verified after purchase:  {customer.is_verified()}")
