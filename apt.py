
"""
Apartment management system - Basic Apartment class.

This module defines the base Apt class that represents a basic apartment
with floor and area attributes, and provides price calculation functionality.
"""

__author__ = "Bar-chaim Aminadav"

PRICE_PER_SQR_METER = 20000
ADDITIONAL_PRICE_PER_FLOOR = 5000
FIRST_FLOOR = 1


class Apt:
    """
    Represents a basic apartment with floor and area.

    This is the base class for all apartment types in the building management system.
    Each apartment has a floor number and area in square meters, and the price
    is calculated based on these attributes.

    Attributes:
        _floor (int): The floor number where the apartment is located
        _area (int): The area of the apartment in square meters
    """

    def __init__(self,floor, area):
        """
        Initialize a new Apt instance.
        Args:
            floor (int): The floor number where the apartment is located
            area (int): The area of the apartment in square meters
        """
        self._floor = floor
        self._area = area

    def get_floor(self):
        """
        Returns:
            int: The floor number
        """
        return self._floor

    def get_area(self):
        """
        Returns:
            int: The area in square meters
        """
        return self._area


    def __eq__(self, other):
        """
        Compare two apartments for equality.

        Two apartments are considered equal if they have the same floor and area.
        For subclasses, the comparison is delegated to the subclass.
        Args:
            other: The object to compare with
        Returns:
            bool: True if apartments are equal, False otherwise
            NotImplemented: If other is not an Apt instance or is a subclass
        """
        if not isinstance(other, Apt):
            return NotImplemented

        if type(other) is Apt:
            return self._floor == other._floor and self._area == other._area

        # it's a subclass, let subclass handle the comparison
        return NotImplemented


    def __str__(self):
        """
        Return string representation of the apartment.
        """
        return f"floor: {self._floor}, area: {self._area}"


    def get_price(self):
        """
        Calculate the price of the apartment.

        Price calculation:
        - Base price: area * PRICE_PER_SQR_METER
        - Floor surcharge: floor * ADDITIONAL_PRICE_PER_FLOOR
        - No additional payment for apartments <= floor 1

        Returns:
            int: The calculated price in currency units
        """
        area_price = self._area * PRICE_PER_SQR_METER
        floor_price = self._floor * ADDITIONAL_PRICE_PER_FLOOR

        # No additional payment for apartments on first floor
        if self._floor <= FIRST_FLOOR:
            floor_price = 0

        return area_price + floor_price

