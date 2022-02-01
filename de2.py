def main_func(func_1):
    def exe_1():
        print("execution point 1")
        func_1()
        print("execution point 2")
    return exe_1
@main_func
def my_name():
    print("my name is jarvihs")

#my_name = main_func(my_name)
my_name()