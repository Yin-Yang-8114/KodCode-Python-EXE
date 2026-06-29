# part 1 section 1
try:
    age = input("Enter your age: ")
    next_year = int(age) + 1
    print("Next year you will be", next_year)
except ValueError:
    print("invalid literal for int() with base 10")


# part 1 section 2
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
except ZeroDivisionError:
    print("Cannot divide by zero")
print(a / b)

# part 1 section 3
numbers = [10, 20, 30]
index = int(input("Choose index: "))
try:
    print(numbers[index])
except IndexError:
    print("Index not found")

# part 1 section 4
prices = {"apple": 3,"banana": 5}
item = input("Enter item: ")
try:
    price = prices[item]
except KeyError:
    print("Item not found")

# part 1 section 5
numbers = [100, 200, 300]
try:
    index = int(input("Choose index: "))
except ValueError:
    print("Please enter a number")
    exit()
except IndexError:
    print("out of range")
    exit()
try:
    divider = int(input("Choose divider: "))
except ValueError:
    print("Please enter a number")
    exit()
try:
    result = numbers[index] / divider
except ZeroDivisionError:
    print("Divided by zero")
    exit()
print(result)

# part 1 section 6
try:
    score = int(input("Enter score: "))
    print("Your score is", score)
except ValueError:
    print("invalid score")
    exit()
finally:
    print("chack finished")

# part 1 section 7
name = input("Enter your name: ")
try:
    if name == "admin":
        print("Welcome admin")
    else:
        print("Welcome user")
except SyntaxError:
    print("syntax error")

# part 1 section 8
price = 100
discount = 20
final_price = price - discount / 100 #ogical error because that not the way you calculating %
print(final_price)
print(f'you should writhe that price - (price * (discount/100)): {price - (price * (discount/100))}')

# part 1 section 9
password = "abc123"
guess = input("Enter password: ")
if guess != password: # logic error I need to chack if the password corrct, not if it does not  correct
    print("Login successful")
else:
    print("Wrong password")
print(f'should be : if guess == password: ')

# part 1 section 10
try:
    num1 = int(input("Number 1: "))
    op = input("Operator: ")
    num2 = int(input("Number 2: "))
    print("Please enter a number")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("unknown operator")
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Division by zero")



# part 2 section 1
celsius = input("Celsius: ")
try:
    fahrenheit = int(celsius) * 9 / 5 + 32
except ValueError:
    print("Temperature must be a number.")
    exit(0)
print(fahrenheit)

# part 2 section 2
word = input("Enter word: ")
try:
    print(word[0])
except IndexError:
    print("Word is empty")

# part 2 section 3
scores = [90, 80, 100]
total = 0
for score in scores:
    total = score # should be += to calculate
average = total / len(scores)
print(average)

scores = [90, 80, 100]
total = 0
for score in scores:
    total += score # fixed
average = total / len(scores)
print(average)

# part 2 section 4

products = {"pen": 4,"notebook": 12}
product = input("Product: ")
try:
    amount = int(input("Amount: "))
except ValueError:
    print("Please enter a number")
    exit()
try:
    print(products[product] * amount)
except KeyError:
    print("Please enter a valid product")
    exit()

# part 2 section 5
files = ["data.txt", "users.csv", "notes.txt"]
try:
    choice = int(input("Choose file number: "))
except ValueError:
    print("Please enter a number")
    exit()
try:
    print(files[choice])
except IndexError:
    print("out of range")
    exit()

# part 2 section 6
numbers = [4, 10, 2, 8]
maximum = 0
for number in numbers:
    if number < maximum: # should be greater than
        maximum = number
print(maximum)


numbers = [4, 10, 2, 8]
maximum = 0

for number in numbers:
    if number > maximum:  # fixed
        maximum = number
print(maximum)

#  part 2 section 7

user = {"name": "Dana","age": 25}
field = input("Choose field: ")
try:
    print(user[field].upper())
except AttributeError:
    print("cant do int upper ")
    exit()
except KeyError:
    print("field not exist")
    exit()

# part 2 section 8

price = int(input("Price: "))
amount = int(input("Amount: "))
total = price * amount
if amount > 3:
    total = total - 10 # error not calculating %
print(total)

price = int(input("Price: "))
amount = int(input("Amount: "))
total = price * amount
if amount > 3:
    total = total - total * 10/100
print(total)

# part 2 section 9
grade = int(input("Grade: "))
if grade >= 90:
    print("Excellent")
if grade >= 70: # logic error should be a flow  condition: if not so not another con
    print("Good")
if grade >= 55: # same
    print("Pass")
else:
    print("Fail")

# fixes code
try:
    grade = int(input("Grade: "))
except ValueError:
    print("please enter a number")
if grade >= 90:
    print("Excellent")
elif grade >= 70:
    print("Good")
elif grade >= 55:
    print("Pass")
else:
    print("Fail")

# part 2 section 10

balance = 100
action = input("Action: ")
try:
    amount = int(input("Amount: "))
    if action == "deposit":
        balance = balance + amount
    elif action == "withdraw":
        if balance - amount > 0:
            balance = balance - amount
        else:
            print("Not enough money")
    print("Balance:", balance)
except ValueError:
    print("Please enter a number")
    exit()
finally:
    print("Bank action finished")
