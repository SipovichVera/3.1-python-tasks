def summa_of_number(*args):
    summa = 0
    for item in args:
        try:
            if type(item) != int:
                raise TypeError
            summa += item
        finally:
            continue
    return summa

print(summa_of_number(1,2,'vde',4, 10, 2.2, 'a'))