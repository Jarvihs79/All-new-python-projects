l1=[1,2,3,4,5,6]
#squert= list(map(lambda x:x*x,l1))
def funct_1(num):
    return num>3
filtr_1=list(filter(funct_1,l1))
print(filtr_1)
#print(squert)
