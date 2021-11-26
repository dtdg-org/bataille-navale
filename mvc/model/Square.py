class Square:
    def __init__(self) -> None:
        self.has_boat = False
        self.is_hit = False
        self.is_miss = False
        self.is_flag = False

    def set_boat(self, has_boat):
        self.has_boat = has_boat

    def set_hit(self, is_hit):
        self.is_hit = is_hit

    def set_miss(self, miss):
        self.is_miss = miss

    def set_flag(self, flag):
        self.is_flag = flag

    def __str__(self) -> str:
        return f'{{boat: {self.has_boat}, hit: {self.is_hit}}}'

    def __repr__(self) -> str:
        return self.__str__()
