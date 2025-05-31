from apt import Apt
ADDITIONAL_VIEW_FEE_PER_FLOOR = 600

# 1)
class SpecialApt(Apt):
    # 2)
    def __init__(self, floor, area ,has_view):
        super().__init__(floor, area)
        self._has_view = has_view

    # 3)
    def get_has_view(self):
        return self._has_view

    # 4)
    def __eq__(self, other):
        if not isinstance(other, SpecialApt):
            return NotImplemented
        return super().__eq__(other) and self._has_view == other._has_view

    # 5)
    def __str__(self):
        return f"{super().__str__()}, has_view: {self._has_view}"

    # B)
    def get_price(self):
        view_price = 0
        if self._has_view:
            view_price = self._floor * ADDITIONAL_VIEW_FEE_PER_FLOOR
        return super().get_price() + view_price