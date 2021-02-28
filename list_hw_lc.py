my_list = [
    [1, None, 2, 3, 4 + 5j, 6],
    [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1],
    ['1', '2', '3.6', None, '4+5.7j', '6']
]

int_list = []
float_list = []
str_list = []
for item in my_list:
    types = [type(elem).__name__ for elem in item]
    single_types = []
    single_types = [i_type for i_type in types if i_type not in single_types]
    types_count = [types.count(element_type) for element_type in single_types]
    max_types_count = max(types_count)
    index_max = types_count.index(max(types_count))
    main_type = single_types[index_max]
    separated_list = [element for element in item if type(element).__name__ == main_type]

    int_list.extend(separated_list)
    float_list.extend(separated_list)
    str_list.extend(separated_list)

res_int_list = [i for i in int_list if type(i).__name__ == 'int']
print('res_int_list: ', res_int_list)

res_float_list = [i for i in float_list if type(i).__name__ == 'float']
print('res_float_list: ', res_float_list)

res_str_list = [str(i) for i in str_list]
print('res_str_list: ', res_str_list)
