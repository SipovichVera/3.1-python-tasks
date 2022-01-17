def summa_of_number(*args):
    summa = 0
    try:
        for item in args:
            if type(item) != int:
                raise TypeError
            summa += item
    finally:
        print("end")

print(summa_of_number(1,2,'vde',4))