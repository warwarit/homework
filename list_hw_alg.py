my_list = [
    [1, None, 2, 3, 4 + 5j, 6],
    [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1],
    ['1','2','3.6',None,'4+5.7j','6']
]


int_list = []
float_list = []
str_list = []
for item in my_list:
    types = []
    for elem in item:
        el_type = type(elem)
        types.append(el_type.__name__)
    single_types = []
    for i_type in types:
        if i_type not in single_types:
            single_types.append(i_type)
    types_count = []
    for element_type in single_types:
        type_count = types.count(element_type)
        types_count.append(type_count)
    max_types_count = max(types_count)
    index_max = types_count.index(max(types_count))
    main_type = single_types[index_max]
    separated_list = []
    for element in item:
        if type(element).__name__ == main_type:
            separated_list.append(element)

    int_list.extend(separated_list)
    float_list.extend(separated_list)
    str_list.extend(separated_list)

res_int_list = []
for i in int_list:
    if type(i).__name__ == 'int':
        res_int_list.append(i)
print('res_int_list: ', res_int_list)

res_float_list = []
for i in float_list:
    if type(i).__name__ == 'float':
        res_float_list.append(i)
print('res_float_list: ', res_float_list)

res_str_list = [str(i) for i in str_list]
print('res_str_list: ', res_str_list)
