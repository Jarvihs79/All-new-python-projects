
def name_func(x):
    try:
        y= x/(x-1)

    except ZeroDivisionError:
        print('error')
    else:
        print(y)
    finally:
        print("always there")

name_func(1)
name_func(2)