#я сам робив цю програму тому що на уроці не міг скачати пайтон і в мене на 59 сроке ошибка, можете допомгти?
import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.happiness = 80
        self.hungry = 0
        self.Old_Age = 0
        self.alive = True

    def to_wolk(self):
        print("time to go for a walk")
        self.Old_Age += 0.1
        self.happiness -= 10
        self.hungry -= 20



    def eat(self):
        print("time to eat")
        self.happiness += 8
        self.hungry += 10

    def to_relax(self):
        print("time to sleep")
        self.happiness += 3

    def alive(self):
        if self.happiness < -0.1:
            print("My life very bored")
            self.alive = False
        elif self.hungry <= 0:
            print("Im very hungry")
            self.alive = False
        elif self.happiness >= 0:
            print("Im happy cat")
            self.alive = True

    def end_of_day(self):
        print(f"hapiness = {self.happiness}")
        print(f"old age = {round(self.Old_Age, 2)}")

    def life(self, day):
        day = "day" +str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_wolk()
        elif live_cube == 2:
            self.to_relax()
        elif live_cube == 3:
            self.eat()
        self.end_of_day()
        self.alive()


Barsik = Dog(name="Barsik")
for day in range(365):
    if Barsik.alive == False:
        break
    Barsik.life(day)

