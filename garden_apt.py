"""
Garden apartment module for the apartment management system.

This module defines the GardenApt class that represents apartments with gardens.
Garden apartments are always located on the ground floor and have no view,
but include a garden area attribute.
"""

__author__ = "Bar-chaim Aminadav"
__student_id__ = "305413247"

from special_apt import SpecialApt

GROUND_FLOOR = 0


class GardenApt(SpecialApt):
    """
    Represents a garden apartment with ground-level garden area.

    This class extends SpecialApt but with fixed characteristics:
    - Always located on ground floor (floor 0)
    - Never has a view (has_view = False)
    - Includes additional garden area attribute

    Attributes:
        _floor (int): Always 0 (ground floor)
        _area (int): The indoor area in square meters
        _has_view (bool): Always False
        _garden_area (int): The garden area in square meters
    """

    def __init__(self,area, garden_area):
        """
        Initialize a new GardenApt instance.

        Garden apartments are automatically set to ground floor with no view.

        Args:
            area (int): The indoor area of the apartment in square meters
            garden_area (int): The garden area in square meters
        """
        super().__init__(GROUND_FLOOR, area, has_view = False)
        self._garden_area = garden_area


    def get_garden_area(self):
        """
        Returns:
            int: The garden area in square meters
        """
        return self._garden_area


    def __eq__(self, other):
        """
        Compare two garden apartments for equality.

        Two garden apartments are equal if they have the same floor, area,
        view status, and garden area.

        Args:
            other: The object to compare with

        Returns:
            bool: True if apartments are equal, False otherwise
            NotImplemented: If other is not a GardenApt instance
        """
        if not isinstance(other, GardenApt):
            return NotImplemented

        return (self._floor == other._floor and # for clarity only
                self._area == other._area and
                self._has_view == other._has_view and # for clarity only
                self._garden_area == other._garden_area)


    def __str__(self):
        """
        Return string representation of the garden apartment.
        Returns:
            str: String including parent class info and garden area
        """
        return f"{super().__str__()}, garden_area: {self._garden_area}"
