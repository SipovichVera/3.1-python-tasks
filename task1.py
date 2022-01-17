def copy_dict():
    my_dict = {'a':1, 'b':2, 'c':3}
    return my_dict.copy()

def swap_keys_values(new_dict):
    for key, value in new_dict.items():
        new_dict[key] = key
        new_dict[value] = new_dict.pop(key)
    return new_dict

__main__ = print(swap_keys_values(copy_dict()))