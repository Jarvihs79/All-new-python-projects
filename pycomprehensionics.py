#comprehensions mean writing code in precise manner
l1=[] #normal method
for i in range(101):
    if i%5==0:
        l1.append(i)
print(l1)
l2=[i for i in range(101) if i%5==0] #comprehension method
print(l2)

normdict={0:'l0',1:'l1',2:'l2'}
print(normdict)
advdict={i:f"l{i}" for i in range(5)}
print(advdict)