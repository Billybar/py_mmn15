
"""
Roof apartment module for the apartment management system.

This module defines the RoofApt class that represents premium roof apartments.
Roof apartments always have a view and may include a pool, with additional
pricing for both roof location and pool features.
"""

__author__ = "Bar-chaim Billy"

from special_apt import SpecialApt

ROOF_PRICE = 40000
POOL_PRICE = 30000


class RoofApt(SpecialApt):
    """
    Represents a roof apartment with optional pool feature.

    This class extends SpecialApt with fixed view (always True) and adds
    pool functionality. Roof apartments have premium pricing.

    Attributes:
        _floor (int): The floor number of the roof apartment
        _area (int): The area in square meters
        _has_view (bool): Always True for roof apartments
        _has_pool (bool): Whether the apartment has a pool
    """

    def __init__(self, floor,  area, has_pool):
        """
        Initialize a new RoofApt instance.

        Roof apartments automatically have a view set to True.

        Args:
            floor (int): The floor number where the apartment is located
            area (int): The area of the apartment in square meters
            has_pool (bool): Whether the apartment has a pool
        """
        super().__init__(floor,area, has_view = True)
        self._has_pool = has_pool


    def get_has_pool(self):
        """
        Returns:
            bool: True if apartment has a pool, False otherwise
        """
        return self._has_pool


    def __eq__(self, other):
        """
        Compare two roof apartments for equality.

        Two roof apartments are equal if they have the same floor, area,
        view status, and pool status.

        Args:
            other: The object to compare with

        Returns:
            bool: True if apartments are equal, False otherwise
            NotImplemented: If other is not a RoofApt instance
        """
        if not isinstance(other, RoofApt):
            return NotImplemented

        return (self._floor == other._floor and
                self._area == other._area and
                self._has_view == other._has_view and # for clarity only
                self._has_pool == other._has_pool)


    def __str__(self):
        """
        Return string representation of the roof apartment.

        Returns:
            str: String including parent class info and pool status
        """
        return f"{super().__str__()}, has_pool: {self._has_pool}"


    def get_price(self):
        """
        Calculate the price of the roof apartment.

        Price calculation includes:
        - Base special apartment price (area, floor, and view costs)
        - Roof apartment surcharge: ROOF_PRICE
        - Pool surcharge: POOL_PRICE (if has_pool is True)

        Returns:
            int: The calculated price in currency units
        """
        if self._has_pool:
            return super().get_price() + ROOF_PRICE + POOL_PRICE
        else:
            return super().get_price() + ROOF_PRICE
