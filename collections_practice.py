# part 1 section 1
tags = {'python', 'bash', 'git', 'python'}
print(tags)
# part 1 section 2
tags.add('linux')
print(tags)
# part 1 section 3
tags.discard('bash')
print(tags)
tags.discard('ziv')
print(tags)
# part 1 section 4
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
# part 1 section 5
print("git" in tags )
# part 1 section 6
point = (10, 20)
print(point)
print(point[0], point[1])
# part 1 section 7
# point[0]=90
# ERROR TypeError: 'tuple' object does not support item assignment
# part 1 section 8
rgb = (255, 128, 0)
r, g, b = rgb
print("r =", r)
print("g =", g)
print("b =", b)
# part 1 section 9
coords = (1, 2, 3, 2, 1)
print(coords.count(2))
print(coords.index(3))
# part 1 section 10
set1 = {1, 2, 3}
tuple1 = (1, 2, 3)
list1 = [1, 2, 3]
print(set1)
print(tuple1)
print(list1)
# part 2 section 1
a = {1, 2, 3}
b = {3, 4, 5}
print(a.issubset(b))
print(a.issuperset(b))
# part 2 section 2
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(pairs[1][1])
# part 2 section 3
list200=[1,2,3,3,3,3,2,1,4,7,5,2,1,2,3,4,5,6,1,1,1]
set200=set(list200)
print(set200)
list201=list(set200)
print(list201)
# part 2 section 4
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))
# part 2 section 5
# Tuples are immutable (hashable)so they are allowed in sets.
# Lists can change (unhashable) so python blocks them to prevent breaking the set
