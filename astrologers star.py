n= int(input("plz tell a int num \n"))
a= (input("plz tell the boolean \n type t for true  \n type f for false\n"))
z=0
if a=="t":
    while z <= n:
        print("*" * z)
        z = z + 1
elif a=="f":
    while z <= n:
        print("*" * n)
        n = n - 1
else:
    print("put right values")
