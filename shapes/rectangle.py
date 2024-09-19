class Rectangle:
    def __init__(self, length: int, width: int):
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("Length and width must be integers")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers")
        self.length = length
        self.width = width

    def __iter__(self):
        self._iter_data = iter([
            {'length': self.length},
            {'width': self.width}
        ])
        return self

    def __next__(self):
        return next(self._iter_data)
