my_dict = {'a':1, 'b':2, 'c':3}
new_dict = my_dict.copy()
for key, value in new_dict.items():
    new_dict[key] = key
    new_dict[value] = new_dict.pop(key)
print(new_dict)
