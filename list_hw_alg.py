# for check
my_list = [
    [1, None, 2, 3, 4 + 5j, 6],
    [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1],
    ['1', '2', '3.6', None, '4+5.7j', '6']
]


int_list = []   # обьявляем пустой список
float_list = []   # обьявляем пустой список
str_list = []   # обьявляем пустой список
for item in my_list:  # итерируемся по списку my_list чтобы разибить его на более мелкие части
    types = []  # обьявляем пустой список
    for elem in item: # итерируемся по списку elem чтобы работать с наименьшим элементом
        el_type = type(elem)    # Присваеваем переменной el_type тип elam
        types.append(el_type.__name__)  # Добавляем в список types имя типа ("int", "str"...)
    single_types = []   # обьявляем пустой список
    for i_type in types: # Итерируемся по спискау types
        if i_type not in single_types: # Проверяем есть ли такое знеачение в списе single_type
            single_types.append(i_type)     # Если значениея нет добавлеяем в список single_types так мы получим спискок типов данных без повторения
    types_count = []    # обьявляем пустой список
    for element_type in single_types:   # Итерируемся по списку singnle_types
        type_count = types.count(element_type)   # Переменной type_count присваиваем колличество типов данных в спике type
        types_count.append(type_count)  # Добавляем в список колличестов типов. Получится спсок в котором указанно число типов данных
    max_types_count = max(types_count)  # Переменной max_types_count писваиваем максимальное значение из списка types_count
    index_max = types_count.index(max(types_count))    # Переменной index_max присваиваем index максимального значения из списка type_count
    main_type = single_types[index_max]    # Переменной main_type присваиваем значение равное индексу index_max в спске single_types тем самым мы получили преобладющий тип
    separated_list = []     # обьявляем пустой список
    for element in item:    # Итерируемся по списку item
        if type(element).__name__ == main_type:   # Проверяем тип данные если он равер преобладющему добавляем в список
            separated_list.append(element)    # Добавляем в список данные с преобладающим типом

    int_list.extend(separated_list)    # Копируем лист
    float_list.extend(separated_list)    # Копируем лист
    str_list.extend(separated_list)    # Копируем лист

res_int_list = []   # обьявляем пустой список
for i in int_list:   # Итерируемся по листу int_list
    if type(i).__name__ == 'int':    # если имя типа переменной равно "int" добавляем в список
        res_int_list.append(i)    # Заполняем список
print('res_int_list: ', res_int_list)    # Выводим список

res_float_list = []     # обьявляем пустой список
for i in float_list:    # Итерируемся по листу float_list
    if type(i).__name__ == 'float':    # если имя типа переменной равно "int" добавляем в список
        res_float_list.append(i)    # Заполняем список
print('res_float_list: ', res_float_list)    # Вывод списка

res_str_list = [str(i) for i in str_list]    # Итерируемся по листу выбираем данные тип которых равен str и заносим в список res_str_list
print('res_str_list: ', res_str_list)    # Вывод списка
