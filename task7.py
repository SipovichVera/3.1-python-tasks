def func(*args, **kwarfs):
    for item in kwarfs.values():
        if callable(item):
            print(item(*args))

def summa(*args):
    return sum(args)

def multiple(*args):
    result = 1
    for item in args:
        result *= item
    return result

func(1,2,3,4, a=summa, b=multiple, c=3)