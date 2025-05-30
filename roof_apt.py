from special_apt import SpecialApt
ROOF_PRICE = 40000
POOL_PRICE = 30000
# 1)
class RoofApt(SpecialApt):

    # 2)
    def __init__(self, area, floor, has_pool):
        super().__init__(area, floor, has_view = True)
        self._has_pool = has_pool

    # 3)
    def get_has_pool(self):
        return self._has_pool

    # 4)
    def __eq__(self, other):
        if not isinstance(other, RoofApt):
            return NotImplemented
        return super().__eq__(other) and self._has_pool == other._has_pool

    # 5)
    def __str__(self):
        return f"{super().__str__()}, has_pool: {self._has_pool}"

    # B)
    def get_price(self):
        if self._has_pool:
            return super().get_price() + ROOF_PRICE + POOL_PRICE
        else:
            return super().get_price() + ROOF_PRICE