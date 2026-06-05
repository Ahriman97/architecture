import pytest

from cart import Item, Cart


class TestCart:
    @pytest.mark.parametrize(
        "quantity1, price1, quantity2, price2, expected",
        [
            (2, 100, 1, 200, 400),
            (1, 200, 2, 100, 400),
            (1, 100, 1, 100, 200),
        ],
    )
    def test_total_price(self, quantity1: int, price1: int, quantity2: int, price2: int, expected: int) -> None:
        cart = Cart(
            [
                Item("Product 1", quantity1, price1),
                Item("Product 2", quantity2, price2),
            ],
        )

        got = cart.total_price()

        assert got == expected

    @pytest.mark.parametrize(
        "items, expected",
        [
            ([], 0),
            ([Item("Product 1", 1, 100)], 1),
            ([Item("Product 1", 1, 100), Item("Product 2", 1, 100)], 2),
        ],
    )
    def test_count_items(self, items: list[Item], expected: int) -> None:
        cart = Cart(items)

        got = cart.count_items()

        assert got == expected

    def test_add_item(self) -> None:
        cart = Cart([])

        cart.add_item(Item("Product 1", 1, 100))

        assert cart == Cart([Item("Product 1", 1, 100)])

    def test_add_item_if_same_item_already_exist(self) -> None:
        cart = Cart([Item("Product 1", 1, 100)])

        cart.add_item(Item("Product 1", 2, 100))

        assert cart == Cart([Item("Product 1", 3, 100)])

    def test_add_item_if_other_item_exist(self) -> None:
        cart = Cart([Item("Product 1", 1, 100)])

        cart.add_item(Item("Product 2", 2, 100))

        assert cart == Cart([Item("Product 1", 1, 100), Item("Product 2", 2, 100)])
