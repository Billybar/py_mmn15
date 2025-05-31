from special_apt import SpecialApt
GROUND_FLOOR = 0

# 1)
class GardenApt(SpecialApt):

    # 2)
    def __init__(self,area, garden_area):
        super().__init__(GROUND_FLOOR, area, has_view = False)
        self._garden_area = garden_area

    # 3)
    def get_garden_area(self):
        return self._garden_area

    # 4)
    def __eq__(self, other):
        if not isinstance(other, GardenApt):
            return NotImplemented

        return (self._floor == other._floor and
                self._area == other._area and
                self._has_view == other._has_view and
                self._garden_area == other._garden_area)

    # 5)
    def __str__(self):
        return f"{super().__str__()}, garden_area: {self._garden_area}"
