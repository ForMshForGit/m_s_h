import random
Vasya = input('Введите число Васі: ')
Petya = input('Введите число Пети: ')
sum = float(Vasya) + float(Petya)
min = float(Vasya) - float(Petya)
mul = float(Vasya) * float(Petya)
div = float(Vasya) / float(Petya)
list = [sum, min, mul, div]
answer = input ("Зробити випадкову дію? Нажміть Ентер і введіть відповідь - Так/Ні")
k = 0
while(True):
    answer = input()
    if answer == "Так":
       print(" випадковий результат чисел Васі і Петра - ", random.choice(list))
       break
    else:
       k += 1
       if (k >= 5):
          break
       print(print("Ну і ладно"))
