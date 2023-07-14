import office_furniture_class


class Desk(office_furniture_class.OfficeFurniture):
    # Initializer
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_drawers):
        office_furniture_class.OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    # str Method
    def __str__(self):
        return f'Category: {self.get_category()} \nMaterial: {self.get_material()} \nLength: {self.get_length()}' \
               f'\nWidth: {self.get_width()} \nHeight: {self.get_height()} \nPrice: {self.get_price()}' \
               f'\nLocation Of Drawers: {self.__location_of_drawers} \nNumber Of Drawers: {self.__number_drawers}'

    # Mutators
    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    # Accessors
    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers
