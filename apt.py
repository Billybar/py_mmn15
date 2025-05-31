PRICE_PER_SQR_METER = 20000
ADDITIONAL_PRICE_PER_FLOOR = 5000

# 1)
class Apt:
    # 2)
    def __init__(self,floor, area):
        self._floor = floor
        self._area = area

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

    # B )
    def get_price(self):
        area_price = self._area * PRICE_PER_SQR_METER
        floor_price = self._floor * ADDITIONAL_PRICE_PER_FLOOR

        if self._floor == 1:
            floor_price = 0

        return area_price + floor_price

