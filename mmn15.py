from apt import Apt
from roof_apt import RoofApt

def average_price(apts: list[Apt]) -> int :
    """Calculate average price of apartments."""
    apt_amount = len(apts)
    total_price = 0
    for apt in apts:
        total_price += apt.get_price()

    return total_price / apt_amount  # avg price


def how_many_rooftop(apts: list) -> int:
    rooftop_amount = 0
    for apt in apts:
        if isinstance(apt, RoofApt) and apt.get_has_pool():
                rooftop_amount += 1

    return rooftop_amount

# dict: # dict { type of apt, amount of apts }