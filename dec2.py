def add_1(x):
    def addu(y):
        return x+y
    return addu
var1= add_1(15)
print(var1(10))