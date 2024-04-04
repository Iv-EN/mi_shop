from .category import Category


class ProductIterator:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index + 1 < len(self.category.goods):
            self.current_index += 1
            return self.category.goods[self.current_index]
        raise StopIteration
