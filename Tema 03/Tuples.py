#  tuples
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
print(mi_tuple[0])
print(mi_tuple[-2])

mi_tuple2 = (1,2,(10,20),3,4)
print(type(mi_tuple))
print(mi_tuple2[2][0])

mi_tuple2 = list(mi_tuple2)
mi_tuple2 = tuple(mi_tuple2)

t = (1,2,3)
x,y,z = t
print(x,y,z)

t = (1,2,3,1)
print(t.count(1))
print(t.index(2))
