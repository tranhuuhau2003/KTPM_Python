import pytest
from shoppingcart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.add_item("banana", 0.50, 2)
    items = cart.get_items()

    assert items["apple"]["price"] == 1.00
    assert items["apple"]["quantity"] == 3
    assert items["banana"]["price"] == 0.50
    assert items["banana"]["quantity"] == 2


def test_add_more_of_same_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.add_item("apple", 1.00, 2)
    items = cart.get_items()

    assert items["apple"]["quantity"] == 5


def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.remove_item("apple")
    items = cart.get_items()

    assert "apple" not in items


def test_get_total():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.add_item("banana", 0.50, 2)
    total = cart.get_total()

    assert total == 1.00 * 3 + 0.50 * 2


def test_empty_cart():
    cart = ShoppingCart()
    total = cart.get_total()
    items = cart.get_items()

    assert total == 0
    assert items == {}


def test_add_item_zero_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 0)
    items = cart.get_items()

    assert "apple" not in items


def test_add_item_none_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, "")
    items = cart.get_items()

    assert "apple" not in items


def test_add_item_negative_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, -2)
    items = cart.get_items()

    assert "apple" not in items


def test_view_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.add_item("banana", 0.50, 2)
    items = cart.get_items()

    assert items["apple"]["quantity"] == 3
    assert items["banana"]["quantity"] == 2
    assert len(items) == 2


def test_update_item_price():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.add_item("apple", 1.50, 2)
    items = cart.get_items()
    assert items["apple"]["price"] == 1.00


def test_remove_nonexistent_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 3)
    cart.remove_item("banana")
    items = cart.get_items()
    assert "banana" not in items


def test_large_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 1.00, 1000000)
    total = cart.get_total()
    assert total == 1.00 * 1000000


def test_item_price_zero():
    cart = ShoppingCart()
    cart.add_item("apple", 0, 3)
    total = cart.get_total()
    assert total == 0


def test_non_numeric_price():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("apple", "free", 3)