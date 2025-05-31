"""
Test module for verifying functionality of Apt system from MMN15.
"""

from apt import Apt
from special_apt import SpecialApt
from garden_apt import GardenApt
from roof_apt import RoofApt
from mmn15 import average_price, how_many_rooftop, top_price, only_valid_apts, how_many_apt_type


def test_apt_classes():
    print("=== Testing Apt Class ===")

    # Basic Apartments
    apt1 = Apt(1, 60)
    apt2 = Apt(3, 80)
    print("apt1 is (testing the __str__() method):")
    print(apt1)
    print(f"testing the get_floor() method returns: {apt1.get_floor()} where it should be 1")
    print(f"testing the get_area() method returns: {apt1.get_area()} where it should be 60")
    print(f"testing the get_price() method returns: {apt1.get_price()} where it should be 1200000")
    print(f"testing the __eq__() method returns: {apt1==apt2} where it should return False\n")

    print("=== Testing SpecialApt Class ===")
    sapt1 = SpecialApt(2, 100, True)
    sapt2 = SpecialApt(5, 70, False)
    print("sapt1 is (testing the __str__() method):")
    print(sapt1)
    print(f"testing the get_floor() method returns: {sapt1.get_floor()} where it should be 2")
    print(f"testing the get_area() method returns: {sapt1.get_area()} where it should be 100")
    print(f"testing the get_has_view() method returns: {sapt1.get_has_view()} where it should be True")
    print(f"testing the get_price() method returns: {sapt1.get_price()} where it should be 2011200")
    print(f"testing the __eq__() method returns: {sapt1==sapt2} where it should return False\n")

    # Garden Apartments (always floor 0 and no view)
    print("=== Testing GardenApt Class ===")
    gapt1 = GardenApt(85, 30)
    gapt2 = GardenApt(95, 40)
    print("gapt1 is (testing the __str__() method):")
    print(gapt1)
    print(f"testing the get_floor() method returns: {gapt1.get_floor()} where it should be 0")
    print(f"testing the get_area() method returns: {gapt1.get_area()} where it should be 85")
    print(f"testing the get_has_view() method returns: {gapt1.get_has_view()} where it should be False")
    print(f"testing the get_garden_area() method returns: {gapt1.get_garden_area()} where it should be 30")
    print(f"testing the get_price() method returns: {gapt1.get_price()} where it should be 1700000")
    print(f"testing the __eq__() method returns: {gapt1==gapt2} where it should return False\n")

    # Rooftop Apartments (always have view, may have pool)
    print("=== Testing RoofApt Class ===")
    rapt1 = RoofApt(10, 90, True)
    rapt2 = RoofApt(7, 65, False)
    print("rapt1 is (testing the __str__() method):")
    print(rapt1)
    print(f"testing the get_floor() method returns: {rapt1.get_floor()} where it should be 10")
    print(f"testing the get_area() method returns: {rapt1.get_area()} where it should be 90")
    print(f"testing the get_has_view() method returns: {rapt1.get_has_view()} where it should be True")
    print(f"testing the get_has_pool() method returns: {rapt1.get_has_pool()} where it should be True")
    print(f"testing the get_price() method returns: {rapt1.get_price()} where it should be 1926000")
    print(f"testing the __eq__() method returns: {rapt1==rapt2} where it should return False\n")

def test_mmn15_functions():
    print("\n=== Testing mmn15.py Functions ===")

    # Construct a test list with at least 2 of each type
    apts = [
        Apt(1, 60), Apt(3, 80),
        SpecialApt(2, 100, True), SpecialApt(5, 70, False),
        GardenApt(85, 30), GardenApt(95, 40),
        RoofApt(10, 90, True), RoofApt(7, 65, False)
    ]
    ind=1
    print("The list of apartments is:")
    for apt in apts:
        print(f"apartment number {ind} ==> {apt}")
        ind+=1

    # Test average_price
    avg = average_price(apts)
    print(f"\nAverage price: {avg} while should print  Average price: 1644550.0")

    # Test how_many_rooftop
    rooftop_count = how_many_rooftop(apts)
    print(f"\nRooftop apartments with pool: {rooftop_count} while should print Rooftop apartments with pool: 1")

    # Test how_many_apt_type
    type_counts = how_many_apt_type(apts)
    print(f"\nApartment type counts: {type_counts}\nwhile should print:\nApartment type counts: {{'Apt': 2, 'SpecialApt': 2, 'GardenApt': 2, 'RoofApt': 2}}")

    # Test top_price
    top = top_price(apts)
    print(f"\nTop priced apartment: {top} | Price: {top.get_price()}\nwhile should print:\nTop priced apartment: floor: 2, area: 100, has_view: True | Price: 2011200")

    # Test only_valid_apts
    valid_apts = only_valid_apts(apts)
    if valid_apts is not None:
        print("\nValid apartments (view or pool, price > 1,000,000):")
        for apt in valid_apts:
            print(f"{apt} | Price: {apt.get_price()}")
    else:
        print("\nNo valid apartments found.")
    print("while should print:")
    print("Valid apartments(view or pool, price > 1, 000, 000):\n"
          "floor: 2, area: 100, has_view: True | Price: 2011200\n"
          "floor: 10, area: 90, has_view: True, has_pool: True | Price: 1926000\n"
          "floor: 7, area: 65, has_view: True, has_pool: False | Price: 1379200")


if __name__ == "__main__":
    test_apt_classes()
    test_mmn15_functions()
