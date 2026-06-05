from dataclasses import dataclass


@dataclass
class Item:
    product_name: str
    quantity: int
    price: int


@dataclass
class Cart:
    items: list[Item]

    def total_price(self) -> int:
        '''Вохвращает полную стоимость товаров в корзине.'''
        return sum([i.price * i.quantity for i in self.items])

    def add_item(self, item: Item) -> None:
        '''Если такой Item уже есть, то нужно увеличить его кол-во, если цены разные то нужно упасть.'''
        for item1 in self.items:
            if item1.product_name == item.product_name:
                # TODO: Нужен тест на ошибку
                if item1.price != item.price:
                    raise ValueError(
                        f"Несовпадение цен '{item1.product_name}': "
                        f"старая цена {item1.price}, "
                        f"новая цена {item.price}"
                    )
                item1.quantity += item.quantity
                return
        self.items.append(item)

    # TODO: Написать тесты
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
        
