from apt import Apt
from garden_apt import GardenApt
from roof_apt import RoofApt

MILLION = 1000000

# section c
def average_price(apts):
    """Calculate average price of apartments."""
    total_price = 0
    if not apts:
        return total_price # avg price = total price  = 0

    apt_amount = len(apts)
    for apt in apts:
        total_price += apt.get_price()

    return total_price / apt_amount  # avg price



# section D
def how_many_rooftop(apts):
    rooftop_amount = 0
    if not apts:
        return rooftop_amount

    for apt in apts:
        if isinstance(apt, RoofApt) and apt.get_has_pool():
                rooftop_amount += 1

    return rooftop_amount



# section E
def how_many_apt_type(apts): # dict { type of apt: amount of apts }
    apt_counts  ={
        'Apt': 0,
        'SpecialApt': 0,
        'GardenApt': 0,
        'RoofApt': 0
    }

    if not apts:
        return apt_counts

    for apt in apts:
        apt_type = type(apt).__name__
        apt_counts[apt_type] += 1

    return apt_counts



# section F
def top_price(apts: list):

    if not apts:
        return None

    apt_max_price = Apt(0,0)
    apt_price = 0
    max_price = 0
    for apt in apts:
        apt_price = apt.get_price()
        if apt_price > max_price:
            max_price = apt_price
            apt_max_price = apt

    return apt_max_price



# section H
def only_valid_apts(apts):
    valid_apts = []

    for apt in apts:
        apt_type = type(apt).__name__
        if apt_type == "Apt" or "GardenApt":
            continue  # they have no view or pool

        if apt.get_has_view() and apt.get_price() > MILLION:
            valid_apts.append(apt)

    if not valid_apts:
        return None

    return valid_apts





