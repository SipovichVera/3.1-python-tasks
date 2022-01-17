def foo_1(foo_2):
    return foo_2()

def foo_2():
    return print(12*13)

foo_1(foo_2)