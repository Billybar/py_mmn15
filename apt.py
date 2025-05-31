PRICE_PER_SQR_METER = 20000
ADDITIONAL_PRICE_PER_FLOOR = 5000
FIRST_FLOOR = 1


class Apt:

    def __init__(self,floor, area):
        self._floor = floor
        self._area = area

    def get_floor(self):
        return self._floor
    def get_area(self):
        return self._area


    def __eq__(self, other):
        if not isinstance(other, Apt):
            return NotImplemented

        if type(other) is Apt:
            return self._floor == other._floor and self._area == other._area

        # it's a subclass, let subclass handle the comparison
        return NotImplemented


    def __str__(self):
        return f"floor: {self._floor}, area: {self._area}"


    def get_price(self):
        area_price = self._area * PRICE_PER_SQR_METER
        floor_price = self._floor * ADDITIONAL_PRICE_PER_FLOOR

        # No additional payment for apartments on first floor
        if self._floor <= FIRST_FLOOR:
            floor_price = 0

        return area_price + floor_price

