import random
i=1
user_points=0
comp_points=0
round_s=0
l1= ['snake','water','gun']
a= random.choice(l1)
while i in range (11):
    round_s= round_s + 1
    print("round",round_s)


    b= input("plz type \n s for snake \n w for water \n g for gun \n")


    i= i+1
    if (b=='s' and a=='snake'):
        print("i selected", a)
        print("its a draw, no one gets the points")
    elif(b=='s' and a=='water'):
        print("i selected", a)
        user_points = user_points + 1
        print("you win" )
    elif(b=='s' and a=='gun'):
        print("i selected", a)
        comp_points = comp_points + 1
        print("i win")
    elif (b == 'w' and a == 'snake'):
        print("i selected", a)
        comp_points = comp_points + 1
        print("i win")
    elif (b == 'w' and a == 'water'):
        print("i selected", a)
        print("its a draw, no one gets the points ")
    elif (b == 'w' and a == 'gun'):
        print("i selected", a)
        user_points = user_points + 1
        print("you win")
    elif (b == 'g' and a == 'snake'):
        print("i selected", a)
        user_points = user_points + 1
        print("you win")
    elif (b == 'g' and a == 'water'):
        print("i selected", a)
        comp_points = comp_points + 1
        print("i win")
    elif (b == 'g' and a == 'gun'):
        print("i selected", a)
        print("its a draw, no one gets the points ")
    else:
        print("enter proper value")
print("points you got ",user_points)
print("points i got", comp_points)
if user_points > comp_points:
    print("you win")
elif user_points < comp_points:
    print("i win")
else:
    print("its a draw")



