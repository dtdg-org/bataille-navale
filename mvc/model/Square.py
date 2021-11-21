class Square:
    def __init__(self) -> None:
        self.has_boat = False
        self.is_hit = False

    def set_boat(self, has_boat):
        self.has_boat = has_boat

    def set_hit(self, is_hit):
        self.is_hit = is_hit

    def __str__(self) -> str:
        return f'{{boat: {self.has_boat}, hit: {self.is_hit}}}'

    def __repr__(self) -> str:
        return self.__str__()
