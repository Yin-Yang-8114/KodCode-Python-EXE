# part 1 section 1
agents = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
print(agents)
# part 1 section 2
print(agents[0],agents[-1])
# part 1 section 3
print(agents[2])
# part 1 section 4
print(agents[1:4])
# part 1 section 5
agents.append('Foxtrot')
print(agents)
# part 1 section 6
agents.insert(2,'Zulu')
print(agents)
# part 1 section 7
agents.remove('Bravo')
print(agents)
# part 1 section 8
print(len(agents))
# part 1 section 9
scores = [42, 17, 95, 8, 61]
print(max(scores))
print(min(scores))
# part 1 section 10
agents2 = agents.copy()
agents2[0]="ZuZU"
print(f'agents : {agents}\nagents 2 : {agents2}')
# part 2 section 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers, numbers)
# part 2 section 2
a = [1, 2, 3]
b = [4, 5, 6]
c= a + b
print(c)
a.extend(b)
print(a)
# part 2 section 3
items = ['x', 'y', 'z', 'x', 'y', 'x']
print(items.count('x'))
items.remove('x')
print(items)
items.pop()
print(items)
del items[2]
print(items)
# part 2 section 4
data = [1, 2, 3, 4, 5]
print(data[0::2])
# part 2 section 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])