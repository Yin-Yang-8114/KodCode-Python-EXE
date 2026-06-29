# # part 1 section 1
# try:
#     age = input("Enter your age: ")
#     next_year = int(age) + 1
#     print("Next year you will be", next_year)
# except ValueError:
#     print("invalid literal for int() with base 10")

# # part 1 section 2
# try:
#     a = int(input("First number: "))
#     b = int(input("Second number: "))
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# print(a / b)

# # part 1 section 3
# numbers = [10, 20, 30]
# index = int(input("Choose index: "))
# try:
#     print(numbers[index])
# except IndexError:
#     print("Index not found")

# # part 1 section 4
# prices = {"apple": 3,"banana": 5}
# item = input("Enter item: ")
# try:
#     price = prices[item]
# except KeyError:
#     print("Item not found")

# # part 1 section 5
# numbers = [100, 200, 300]
# try:
#     index = int(input("Choose index: "))
# except ValueError:
#     print("Please enter a number")
#     exit()
# except IndexError:
#     print("out of range")
#     exit()
# try:
#     divider = int(input("Choose divider: "))
# except ValueError:
#     print("Please enter a number")
#     exit()
# try:
#     result = numbers[index] / divider
# except ZeroDivisionError:
#     print("Divided by zero")
#     exit()
# print(result)

# # part 1 section 6
# try:
#     score = int(input("Enter score: "))
#     print("Your score is", score)
# except ValueError:
#     print("invalid score")
#     exit()
# finally:
#     print("chack finished")

# # part 1 section 7
# name = input("Enter your name: ")
# try:
#     if name == "admin":
#         print("Welcome admin")
#     else:
#         print("Welcome user")
# except SyntaxError:
#     print("syntax error")

# # part 1 section 8
# price = 100
# discount = 20
# final_price = price - discount / 100 #ogical error becouse that not the way you calculting %
# print(final_price)
# print(f'you should writhe that price - (price * (discount/100)): {price - (price * (discount/100))}')

# # part 1 section 9
# password = "abc123"
# guess = input("Enter password: ")
# if guess != password: # logic error i need to chack if the password corrct, not if dose not  correct
#     print("Login successful")
# else:
#     print("Wrong password")
# print(f'should be : if guess == password: ')

# # part 1 section 10
# try:
#     num1 = int(input("Number 1: "))
#     op = input("Operator: ")
#     num2 = int(input("Number 2: "))
#     print("Please enter a number")
#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#         print(num1 / num2)
#     else:
#         print("unknown operator")
# except ValueError:
#     print("Please enter a number")
# except ZeroDivisionError:
#     print("Division by zero")



# part 2 section 1
celsius = input("Celsius: ")
fahrenheit = int(celsius) * 9 / 5 + 32
print(fahrenheit)
