import random


# class Human:
#     def __init__(self, name='Human'):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human):
#         self.passengers.append(human)
#
#     def print_passengers_names(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
#
# petya = Human('Petya')
# mari = Human('Mari')
# car = Auto('Mercedes')
#
# car.add_passenger(petya)
# car.add_passenger(mari)
# car.print_passengers_names()


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    'Java developer': {'salary': 50, 'gladness_less': 10},
    'Python developer': {'salary': 40, 'gladness_less': 3},
    'C++ developer': {'salary': 45, 'gladness_less': 25},
    'Rust developer': {'salary': 70, 'gladness_less': 1},
}
brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
    'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
    'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']
