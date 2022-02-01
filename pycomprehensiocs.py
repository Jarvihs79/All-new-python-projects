#comprehensions mean writing code in precise manner
l1=[]
for a in range(100):
    if a%5==0:
        l1.append(a)
print(l1)
l2=[a for a in range(100) if a%5==0]
print(l2)

normdict={0:'l0',1:'l1',2:'l3'}
print(normdict)
advdict={a:f"l{a}" for a in range(5)}
print(advdict)