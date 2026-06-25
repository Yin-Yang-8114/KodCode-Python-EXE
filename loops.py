# part 1 section 1
i = 0
while i <=5 :
    print(i)
    i=i+1
# part 1 section 2
i = 10
while i >=0  :
    print(i)
    i-=1
# part 1 section 3
total = 0
num =0
while num <= 10 :
    total += num
    num+=1
print(total)
# part 1 section 4
items = [2, 4, 6, 8]
i =0
while True:
    if items[i] > 5:
        print(items[i])
        break
    i+=1
# part 1 section 5
i =0
while i <= 10:
    if i %2 ==0:
        print(i)
    i+=1
# part 1 section 6
agents = ['Alpha', 'Bravo', 'Charlie']
i = 0
while i < len(agents):
    print(agents[i])
    i+=1
# part 1 section 7
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
i = 0
list_scores = list(scores.items())
while i < len(scores):
    print(list_scores[i])
    i+=1
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
i = 0
list_scores = list(scores.items())
while i < len(scores):
    name , score = list_scores[i]
    print(name, score)
    i += 1
# part 1 section 8
start = 1
while start <=100:
    start *= 2
print(start)
# part 1 section 9
data = [3, 7, 2, -1, 5]
i = 0
sum1 = 0
while i < len(data):
    if data[i] == -1:
        break
    sum1 += data[i]
    i += 1
print(sum1)
# part 1 section 10
n =10
i = 1
while i <= n:
    print(n * i)
    i += 1
# part 2 section  1
items = ['a', 'x', 'b', 'x', 'x']
i =0
while i < len(items):
    if items[i] == 'x':
        items.remove('x')
        print(items)
    else:
        i = i + 1
items = ['a', 'x', 'b', 'x', 'x']
i =0
while "x" in items:
    items.remove("x")
    print(items)
# part 2 section  2
matrix = [[1, 2], [3, 4], [5, 6]]
row = 0
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        print(matrix[row][col])
        col += 1
    row += 1
# part 2 section  3
list101 = [1, 2, 3, 4 ,5 ]
list102 =[]
i = len(list101)-1
while i >=0 :
    list102.append(list101[i])
    i -= 1
print(list102)
# part 2 section  4
data = [10, 30, 55, 20, 80]
i = 0
while i < len(data):
    if data[i] > 50:
        print(data.index(data[i]))
        break
    i += 1
# part 2 section  5
secret = 42
list_of_guesses = [10,30,42]
attempt =0
i =0
while i < len(list_of_guesses):
    attempt +=1
    if list_of_guesses[i] == secret:
        break
    i+=1
print(f'the number of attempts is {attempt}')
