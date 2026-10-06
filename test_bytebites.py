from models import Customer, Menu, MenuItem, Order
import pytest


@pytest.fixture
def items():
    return {
        "burger": MenuItem("Spicy Burger", 10.00, "Entrees", 4.5),
        "soda": MenuItem("Large Soda", 5.00, "Drinks", 3.9),
        "tea": MenuItem("Iced Tea", 3.50, "Drinks", 4.2),
        "cake": MenuItem("Chocolate Cake", 6.25, "Desserts", 4.8),
    }


@pytest.fixture
def menu(items):
    return Menu(items.values())


# --- Order totals ---

def test_calculate_total_with_multiple_items(items):
    """A $10 burger and a $5 soda should total $15."""
    order = Order([items["burger"], items["soda"]])
    assert order.compute_total() == 15.00


def test_order_total_is_zero_when_empty():
    """An order with no items totals $0 instead of crashing."""
    assert Order().compute_total() == 0


def test_total_counts_duplicate_items(items):
    """Ordering the same item twice charges for it twice."""
    order = Order()
    order.add_item(items["soda"])
    order.add_item(items["soda"])
    assert order.compute_total() == 10.00


def test_total_has_no_float_rounding_noise():
    """Prices like 0.10 + 0.20 total exactly 0.30."""
    order = Order([MenuItem("Gum", 0.10, "Snacks", 1), MenuItem("Mint", 0.20, "Snacks", 1)])
    assert order.compute_total() == 0.30


# --- Filtering ---

def test_filter_drinks_returns_only_drinks(menu):
    """Filtering 'Drinks' returns only drink items."""
    names = {item.name for item in menu.filter_by_category("Drinks")}
    assert names == {"Large Soda", "Iced Tea"}


def test_filter_is_case_insensitive(menu):
    """'drinks' and 'Drinks' give the same results."""
    assert menu.filter_by_category("drinks") == menu.filter_by_category("Drinks")


def test_filter_unknown_category_returns_empty_list(menu):
    """A category with no items returns an empty list."""
    assert menu.filter_by_category("Breakfast") == []


# --- Sorting ---

def test_sort_by_price_cheapest_first(menu):
    """Sorting by price lists the cheapest item first."""
    prices = [item.price for item in menu.sort_by_price()]
    assert prices == [3.50, 5.00, 6.25, 10.00]


def test_sort_by_price_descending(menu):
    """descending=True lists the most expensive item first."""
    assert menu.sort_by_price(descending=True)[0].name == "Spicy Burger"


def test_sort_by_popularity_most_popular_first(menu):
    """The most popular item comes first."""
    assert menu.sort_by_popularity()[0].name == "Chocolate Cake"


def test_sorting_does_not_change_menu_order(menu):
    """Sorting returns a new list and leaves the menu itself unchanged."""
    original = list(menu.items)
    menu.sort_by_price()
    assert menu.items == original


# --- Customer verification ---

def test_new_customer_is_not_verified():
    """A customer with no purchase history is not verified yet."""
    assert not Customer("Nour").is_verified()


def test_customer_verified_after_purchase(items):
    """Recording a purchase makes the customer verified."""
    customer = Customer("Nour")
    customer.add_purchase(Order([items["burger"]]))
    assert customer.is_verified()
    assert len(customer.purchase_history) == 1
