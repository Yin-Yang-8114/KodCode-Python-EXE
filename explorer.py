# # part 1 section 1
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
# # part 1 section 2
# for i in range(1,6):
#     print(i)
# # part 1 section 3
# for i in range(0,10,2):
#     print(i)
# # part 1 section 4
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
# # part 1 section 5
# scores = {'Alpha': 80, 'Bravo': 95}
# list_score =list(scores.items())
# print(list_score)
# for item in list_score:
#     print(item[0],item[1])
# # part 1 section 6
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)
# # part 1 section 7
# i = 1
# list1=[]
# while 0<  i <=5:
#     list1.append(i)
#     i += 1
# for i in list1:
#     print(i)
# # part 1 section 8
# matrix = [[1, 2, 3], [4, 5, 6]]
# for row in matrix:
#     for col in row:
#         print(col)
# # part 1 section 9
# squares_numbers = [num ** 2 for num in range(1,11)]
# print(squares_numbers)
# # part 1 section 10
# even_num=[num for num in range(1,21) if num % 2 == 0]
# print(even_num)
# # part 2 section 1
# names = ['Alpha', 'Bravo']
# scores = [80, 95]
# zipped = zip(names, scores)
# for i in zipped:
#     print(i[0], i[1])
# # part 2 section 2
# list1933=[(n, n**2) for n in range(1,6)]
# print(list1933)
# part 2 section 3
list1 = [1, 2, 3, 4, 5]
for index,num in enumerate(list1, start=1):
    print(index, num)
# # part 2 section 4
# matrix = [[1, 2], [3, 4], [5, 6]]
# flatten_matrix=[col for row in matrix for col in row]
# print(flatten_matrix)
# # part 2 section 5
# words = ['hello', 'world', 'python']
# uppercase=[word.upper() for word in words ]
# print(uppercase)