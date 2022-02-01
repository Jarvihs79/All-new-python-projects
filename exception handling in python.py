def val (x):
    try:
        b= x/(x-1)
    except ZeroDivisionError :
        print("error")
    else:
        print(b)
    finally:
        print("after all this time always")

val(1)
val(2)
val(3)
