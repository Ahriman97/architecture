import pytest

from cart import Cart, Item


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
