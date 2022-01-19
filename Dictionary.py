#d1={ "uzumaki": "naruto", "uchiha":"sasuke", "huga": "neji"}
#print(d1)
#print(d1["uchiha"])
d1={ "uzumaki": "naruto", "uchiha":"sasuke", "huga":{'main branch': 'hinata', 'side branch': 'neji'}}
#print(d1)
#print(d1['huga'])
#print(d1['huga']['main branch'])
d1.update({'nara': 'shikmaru'})
#del d1 ['uchiha']
d2= d1.copy()
del d2 ['uchiha']
print(d2.keys())
print(d2.values())
print(len(d1))
print(str(d2))








