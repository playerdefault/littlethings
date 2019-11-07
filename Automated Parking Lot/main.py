import sys
import click
import pickle

@click.group()
def main():
    """ Simple CLI parking lot application"""
    pass

class Car():
    def __init__(self, reg_no, color):
        self.reg_no = reg_no
        self.color = color

@main.command()
@click.argument('number_of_parking_spaces')
def create_parking_lot(number_of_parking_spaces):
    total_lot_space = int(number_of_parking_spaces)
    parking_lot = [None]*total_lot_space

    dataObj = DataObject(parking_lot, total_lot_space);
    dataObj.write_data_to_file();

    print("Created a parking lot with {} slots".format(total_lot_space))

@main.command()
@click.argument('car_reg_no')
@click.argument('car_color')
def park(car_reg_no, car_color):
    car = Car(car_reg_no, car_color)

    parking_lot, total_lot_space = DataObject.read_data_from_file();

    if (all(lot != None for lot in parking_lot)):
        print("Sorry, parking lot is full")
    else:
         closest_empty_lot_index = parking_lot.index(None)
         parking_lot[closest_empty_lot_index] = Car(car_reg_no, car_color)

         dataObj = DataObject(parking_lot, total_lot_space)
         dataObj.write_data_to_file()

         print("Allocated slot number: " + str(closest_empty_lot_index + 1))

@main.command()
@click.argument('lot_to_empty')
def leave(lot_to_empty):

    parking_lot, total_lot_space = DataObject.read_data_from_file()

    # lists in python start with index 0, while parking lots start with index 1
    parking_lot[int(lot_to_empty) - 1] = None

    dataObj = DataObject(parking_lot, total_lot_space)
    dataObj.write_data_to_file()

    print("Slot number {} is free".format(lot_to_empty))

@main.command()
@click.argument('color')
def registration_numbers_for_cars_with_colour(color):

    parking_lot = DataObject.read_data_from_file('parking_lot')

    reg_nos = []
    for car in parking_lot:
        if (car != None and car.color == color):
            reg_nos.append(car.reg_no)

    print(*reg_nos)

@main.command()
@click.argument('color')
def slot_numbers_for_cars_with_colour(color):

    parking_lot = DataObject.read_data_from_file('parking_lot')

    slot_nos = []
    for slot_no, car in enumerate(parking_lot):
        if (car != None and car.color == color):
            slot_nos.append(slot_no + 1)

    print(*slot_nos)

@main.command()
@click.argument('reg_no')
def slot_number_for_registration_number(reg_no):

    parking_lot = DataObject.read_data_from_file('parking_lot')

    for array_index, car in enumerate(parking_lot):
        if (car != None and car.reg_no == reg_no):
            # slot_no = array_index + 1 as arrays start with index 0
            print(array_index + 1)
            return

    print('Not found')


@main.command()
def status():
    result_table = []

    parking_lot, total_lot_space = DataObject.read_data_from_file()

    result_table.append(['Slot No.', 'Registration No.', 'Color'])

    if (parking_lot == [None]*total_lot_space):
        result_table.append(['Empty', 'Empty', 'Empty'])
    else:
        for slot_no, car in enumerate(parking_lot):
            if (car != None):
                result_table.append([slot_no + 1, car.reg_no, car.color])

    for row in result_table:
        print("{: >20} {: >20} {: >20}".format(*row))

class DataObject:
    def __init__(self, parking_lot, total_lot_space):
        self.parking_lot = parking_lot
        self.total_lot_space = total_lot_space

    def set_parking_lot(self, current_parking_lot):
        self.parking_lot = current_parking_lot

    def set_total_lot_space(self, total_lot_space):
        self.total_lot_space = total_lot_space

    def write_data_to_file(self):
        with open('parking_lot.pickle', 'wb') as parking_lot_file:
            pickle.dump(self.parking_lot, parking_lot_file)
        with open('total_lot_space.pickle', 'wb') as lot_space_file:
            pickle.dump(self.total_lot_space, lot_space_file)

    @staticmethod
    def read_data_from_file(specific_data=None):
        parking_lot = []
        total_lot_space = 0

        with open('parking_lot.pickle', 'rb') as parking_lot_file:
            parking_lot = pickle.load(parking_lot_file)
        with open('total_lot_space.pickle', 'rb') as lot_space_file:
            total_lot_space = pickle.load(lot_space_file)

        if (specific_data == 'parking_lot'):
            return parking_lot
        elif (specific_data == 'total_lot_space'):
            return total_lot_space
        else:
            return parking_lot, total_lot_space


if __name__ == '__main__':
    main()
