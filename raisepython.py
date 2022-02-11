#Python raise Keyword is used to raise exceptions or errors
a= int(input("tell number"))
if a%2!=0:
    raise Exception("put even num only")
else:
    print("good")

#we can also raise the type of error
a='jarvihs'
try:
    b=int(a)
except ValueError:
    raise ValueError("str cannot be changed into int")

#we can just type raise also
a='jarvihs'
try:
    b=int(a)
except ValueError:
    raise 