
"""
Apartment management utility functions.

This module provides utility functions for analyzing and processing
lists of apartments in the building management system. It includes
functions for calculating averages, counting specific apartment types,
and filtering apartments based on various criteria.
"""

from apt import Apt
from special_apt import SpecialApt
from garden_apt import GardenApt
from roof_apt import RoofApt

MILLION = 1000000

# section c
def average_price(apts):
    """
    Calculate the average price of apartments in the given list.

    Args:
        apts (list): List of apartment objects

    Returns:
        float: The average price of all apartments, or 0 if list is empty
    """
    sum_price = 0
    if not apts:
        return sum_price # avg price = sum_price  = 0

    apt_amount = len(apts)
    for apt in apts:
        sum_price += apt.get_price()

    return sum_price / apt_amount  # avg price



# section D
def how_many_rooftop(apts):
    """
    Count the number of roof apartments with pools in the given list.

    Args:
        apts (list): List of apartment objects

    Returns:
        int: Number of roof apartments that have pools, 0 if none found
    """
    rooftop_counter = 0
    if not apts:
        return rooftop_counter #  = 0

    for apt in apts:
        if isinstance(apt, RoofApt) and apt.get_has_pool():
                rooftop_counter += 1

    return rooftop_counter



# section E
def how_many_apt_type(apts):
    """
    Count apartments by type and return a dictionary with counts.

    Args:
        apts (list): List of apartment objects

    Returns:
        dict: Dictionary with apartment type names as keys and counts as values.
              Keys are: 'Apt', 'SpecialApt', 'GardenApt', 'RoofApt'
              Returns all counts as 0 if list is empty.
    """
    apt_counts  ={
        'Apt': 0,
        'SpecialApt': 0,
        'GardenApt': 0,
        'RoofApt': 0
    }

    if not apts:
        return apt_counts

    # classified apt and update count
    for apt in apts:
        apt_type = type(apt).__name__
        apt_counts[apt_type] += 1

    return apt_counts



# section F
def top_price(apts: list):
    """
    Find the apartment with the highest price in the given list.

    Args:
        apts (list): List of apartment objects

    Returns:
        Apt or None: The apartment object with the highest price,
                     or None if the list is empty.
                     If multiple apartments have the same highest price,
                     returns the first one found.
    """
    if not apts:
        return None

    max_price_apt = apts[0]
    max_price = max_price_apt.get_price()   # holds top apt price

    for apt in apts[1:]:    # Start from second apartment
        current_apt_price = apt.get_price()

        # check if current apt more expensive
        if current_apt_price > max_price:
            max_price = current_apt_price
            max_price_apt = apt

    return max_price_apt



# section G
def only_valid_apts(apts):
    """
    Filter apartments to find those with view or pool and price over 1 million.

    This function returns apartments that:
    - Have a view (SpecialApt or RoofApt with has_view=True)
    - Have a price greater than 1,000,000
    - Are not basic Apt or GardenApt (which don't have views/pools)

    Args:
        apts (list): List of apartment objects

    Returns:
        list or None: List of qualifying apartments, or None if no apartments
                      meet the criteria or if the input list is empty.
    """
    valid_apts = []

    for apt in apts:
        apt_type = type(apt).__name__

        # Apt and GardenApt have no view -> continue
        if apt_type == "Apt" or apt_type == "GardenApt":
            continue

        # if apt has view and price > million -> add to valid list
        if apt.get_has_view() and apt.get_price() > MILLION:
            valid_apts.append(apt)

    if not valid_apts:
        return None

    return valid_apts





