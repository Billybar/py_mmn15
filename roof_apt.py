from special_apt import SpecialApt
ROOF_PRICE = 40000
POOL_PRICE = 30000


class RoofApt(SpecialApt):


    def __init__(self, floor,  area, has_pool):
        super().__init__(floor,area, has_view = True)
        self._has_pool = has_pool


    def get_has_pool(self):
        return self._has_pool


    def __eq__(self, other):
        if not isinstance(other, RoofApt):
            return NotImplemented

        return (self._floor == other._floor and
                self._area == other._area and
                self._has_view == other._has_view and
                self._has_pool == other._has_pool)


    def __str__(self):
        return f"{super().__str__()}, has_pool: {self._has_pool}"


    def get_price(self):
        if self._has_pool:
            return super().get_price() + ROOF_PRICE + POOL_PRICE

        return super().get_price() + ROOF_PRICE