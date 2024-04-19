class ZeroQuantityException(Exception):
    """Обработка попытки добавить товар с нулевым количеством."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return "ZeroQuantityException, {0}".format(self.message)
        else:
            return "Ошибка при обработке добавления товара"
