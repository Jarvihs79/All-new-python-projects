def largs (*arsp,**qwerty):
    for i in arsp:
        print(i)
    for key,value in qwerty.items():
        print(key,value)


d1=['me','you','else','no one','none']

largs(*d1)

q1={'me':'p','you':'go','else':'hi','no one':'fu','none':'but','gud':'grace'}
largs(**q1)