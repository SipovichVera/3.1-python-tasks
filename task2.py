my_dict = {'a':1, 'b':2, 'c':3}

def create_list_from_dict_keys_way1(my_dict):
    return list(my_dict.keys())

def create_list_from_dict_keys_way2(my_dict):
    list_of_keys = []
    for key in my_dict.keys():
        list_of_keys.append(key)
    return list_of_keys

__main__ = print(create_list_from_dict_keys_way1(my_dict), create_list_from_dict_keys_way2(my_dict))