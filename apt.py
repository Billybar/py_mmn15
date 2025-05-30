# 1)
class Apt:
    # 2)
    def __init__(self, area , floor):
        self._area = area
        self._floor = floor

    # Getters
    # 3)
    def get_floor(self):
        return self._floor
    def get_area(self):
        return self._area

    # 4)
    def __eq__(self, other):
        if not isinstance(other, Apt):
            return NotImplemented
        return self._floor == other._floor and self._area == other._area

    # 5)
    def __str__(self):
        return f"floor: {self._floor}, area: {self._area}"

    # B)
    def get_price(self):
        return self._area * 20000 + self._floor * 5000

