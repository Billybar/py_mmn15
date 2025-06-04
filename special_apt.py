"""
Special apartment module for the apartment management system.

This module defines the SpecialApt class that extends the basic Apt class
with an additional view feature that affects the apartment pricing.
"""

__author__ = "Bar-chaim Aminadav"
__student_id__ = "305413247"

from apt import Apt
ADDITIONAL_VIEW_FEE_PER_FLOOR = 600


class SpecialApt(Apt):
    """
    Represents a special apartment with optional view feature.

    This class extends the basic Apt class by adding a view attribute.
    Apartments with a view have additional pricing based on the floor number.

    Attributes:
        _floor (int): Inherited from Apt - the floor number
        _area (int): Inherited from Apt - the area in square meters
        _has_view (bool): Whether the apartment has a view
    """

    def __init__(self, floor, area ,has_view):
        """
        Initialize a new SpecialApt instance.

        Args:
            floor (int): The floor number where the apartment is located
            area (int): The area of the apartment in square meters
            has_view (bool): Whether the apartment has a view
        """
        super().__init__(floor, area)
        self._has_view = has_view


    def get_has_view(self):
        """
        Returns:
            bool: True if apartment has a view, False otherwise
        """
        return self._has_view


    def __eq__(self, other):
        """
        Compare two special apartments for equality.

        Two special apartments are equal if they have the same floor, area,
        and view status. Comparison with basic Apt considers view as False.

        Args:
            other: The object to compare with

        Returns:
            bool: True if apartments are equal, False otherwise
            NotImplemented: If other is not a SpecialApt instance or is a subclass
        """
        if not isinstance(other, SpecialApt):
            return NotImplemented

        if type(other) is Apt:
            return self._floor == other._floor and self._area == other._area and not self._has_view

        if type(other) is SpecialApt:
            return (self._floor == other._floor and
                    self._area == other._area and
                    self._has_view == other._has_view)

        # it's a subclass, let subclass handle the comparison
        return NotImplemented


    def __str__(self):
        """
        Return string representation of the special apartment.
        Returns:
            str: String including parent class info and view status
        """
        return f"{super().__str__()}, has_view: {self._has_view}"


    def get_price(self):
        """
        Calculate the price of the special apartment.

        Price calculation includes the base apartment price plus view surcharge:
        - Base price from parent class (area and floor costs)
        - View surcharge: floor * ADDITIONAL_VIEW_FEE_PER_FLOOR (if has_view)

        Returns:
            int: The calculated price in currency units
        """
        view_price = 0
        if self._has_view:
            view_price = self._floor * ADDITIONAL_VIEW_FEE_PER_FLOOR
        return super().get_price() + view_price