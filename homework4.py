try:
    dividend = int(input('Введите делимое '))
except ValueError:
    print('Ошибка введено не число')
    dividend = 0
try:
    divider = int(input('Введите делитель '))
except ValueError:
    print('Ошибка введено не число')
    divider = 1
try:
    noun = dividend / divider
except ZeroDivisionError:
    print('Ошибка на 0 делить нельзя')
    noun = 0
print('частное ', noun)


cars = [{"brand": "ford", "model": "MusTAng Gt500", "year": 2018},
        {"brand": "ZAZ", "model": "Fortza", "year": 2001},
        {"brand": "VW", "model": "Golf GTI", "year": 1999}]
import operator
cars.sort(key=operator.itemgetter('year'))
for car in cars:
    car['brand'] = car['brand'].upper()
    car['model'] = car['model'].title()
    if ' ' in car['model']:
        temp_model = car['model'].split(' ')
        temp_model[-1] = temp_model[-1].upper()
        car['model'] = ' '.join(temp_model)
print('cars', cars)