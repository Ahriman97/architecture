

class Item:
    def __init__(self, product_name: str, quantity: int, price: int) -> None:
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


class Cart:
    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def total_price(self) -> int:
        '''Вохвращает полную стоимость товаров в корзине.'''
        return sum([i.price * i.quantity for i in self.items])

    def add_item(self, item: Item) -> None:
        '''Если такой Item уже есть, то нужно увеличить его кол-во, если цены разные то нужно упасть.'''
        n = 0
        for item1 in self.items:
            if item1.product_name == item.product_name:
                n = 1
                if item1.price != item.price:
                    raise ValueError(
                        f"Несовпадение цен '{item1.product_name}': "
                        f"старая цена {item1.price}, "
                        f"новая цена {item.price}"
                    )
                item1.quantity += item.quantity
                return
        if n > 0:
            self.items.append(item)

    def remove_item(self, item: Item) -> None:
        '''Если Item не обнаружен, упасть, иначе удалить его из корзины.'''
        n = 0
        for item1 in self.items:
            if item1.product_name == item.product_name:
                n = 1
                self.items.remove(item1)
        if n == 0:
            raise Exception('Товар не найден в корзине')

    def count_items(self) -> int:
        '''Вернуть кол-во item(ов)'''
        return len(self.items)
        
