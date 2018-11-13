import random as r

class Cars:
    """A simple class that models some
    of the attributes of cars.
    By Doug Purcell """

    speed = 0

    def car_type(self):
        car_lot = ["1957 Ferrari 250 GT California", "Model X P100D", "Lamborghini Egoista", "Bugatti Chiron",
        "Pagani Huayra BC"]
        return r.choice(car_lot)

    def car_color(self):
        colors = ["silver", "black", "white", "med dark blue", "med dark gray", "med red", "med dark green", "light brown"]
        return r.choice(colors)


    def accelerate(self, speed):
        """ increases speed of car by speed entered."""
        self.speed += speed

    def brake(self, speed):
        """slows down car by speed. """
        if speed > 0:
            self.speed -= speed
        else:
            print("Doesn't count...\nEnter a positive number!")

    def is_stoppped(self):
        """Checks to see if vehicle is motionless"""
        if self.speed == 0:
            return True
        else:
            return False

    def compute_miles_to_driven(self, mph):
        """ Accepts mph of car and returns total miles driven, mph, and total hours driven"""
        distance = mph
        count = 1
        gap = mph
        while gap > 0:
            count += 1
            distance *= count
            gap -= mph
        print("You drive {} miles driving at {} mph for {} hours".format(mph *count, mph, count))


    def get_speed(self):
        """ returns speed of car."""
        return "The speed is {} mph".format(self.speed)


if __name__ == '__main__':
    cars = Cars()
    print("Congrats! You got yourself a {} {}".format(cars.car_color(),cars.car_type()))
    cars.accelerate(20)
    cars.brake(10)
    print(cars.get_speed())
    print(cars.speed)
    cars.compute_miles_to_driven(53)
    print(cars.is_stoppped())