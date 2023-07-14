"""Chapter 11 Practice 1 Program - Office Furniture

For this assignment, you will demonstrate class inheritance by creating a parent class for OfficeFurniture and a
child class for Desk. You will instantiate and display an object for each class."""

import office_furniture_class
import desk_class


def main():  # Define main
    # Create instance of OfficeFurniture and Desk classes setting the attributes
    office_furniture = office_furniture_class.OfficeFurniture("Filing Cabinet", "Metal",
                                                              "4 ft", "2 ft", "6 ft",
                                                              "$100")
    desk = desk_class.Desk(office_furniture.get_category(), office_furniture.get_material(),
                           office_furniture.get_length(), office_furniture.get_width(), office_furniture.get_height(),
                           office_furniture.get_price(), "Left and Right",
                           "4 drawers")

    # Display the state of the instances
    print("Here is the contents of the instance for the OfficeFurniture class:")
    print(office_furniture)

    print("\nHere is the contents of the instance for the Desk class:")
    print(desk)


main()  # Call main
