
#  Sets
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(8)
s1.remove(3)
s1.discard(2)
s2.pop()
s2.clear()


