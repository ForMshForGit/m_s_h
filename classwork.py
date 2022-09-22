class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, human):
        self.passenger.append(human)

    def print_passenger(self):
        if self.passenger!=[]:
            print(f"Names of {self.brand} passenger:")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"There are no passenger in {self.brand}")

ivaneko = Human("Ivaneko")
person2 = Human("Ignatiev")
car1 = Auto("Porsche")
car2 = Auto("Reno Logan")

car1.print_passenger()
car2.print_passenger()

car1.add_passenger(ivaneko)
car2.add_passenger(person2)
print("А ну в багажник быстро")
car1.print_passenger()
car2.print_passenger()