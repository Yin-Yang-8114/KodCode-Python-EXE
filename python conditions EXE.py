# part 1 section 1
age = int(input("Enter your age : "))
if age >= 18 :
    print('can enter')
elif age < 18 :
    print('canot enter')
# part 1 section 2
temperature = 38.2
if temperature >= 37.5 :
    print('High temperature')
else:
    print('Normal temperature')
# part 1 section 3
number = int(input("Enter a number : "))
if number % 2 == 0 :
    print('even number')
elif number % 2 != 0 :
    print('odd number')
# part 1 section 4
battery = 15
is_charging = True
if battery > 20 and is_charging :
    print('charging now')
elif battery < 20 and is_charging ==False:
    print('Low battery')
else :
    print('Battery OK')
# part 1 section 5
password = str(input("Enter your password : "))
if password == 'python123' :
    print('approved')
else :
    print('access denied')
# part 1 section 6
Define_score = 72
if Define_score > 90 :
    print('Excellent')
elif Define_score > 75 :
    print('Good')
else:
    print('fail')
# part 1 section 7
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
if first_number > second_number :
    print('First is bigger')
elif second_number == first_number :
    print(' the first number and the second number are equal')
else:
    print('second is bigger')
# part 1 section 8
fuel = 40
distance = 30
reserve = fuel - distance
if fuel - distance >= 10 :
    print('enough fuel with reserve')
elif fuel - distance >= 0 and reserve < 10 :
    print('enough fuel , low reserve')
else:
    print('not enough fuel')
# part 1 section 9
username = str(input("Enter your username : "))
if username == '' :
    print('guest user')
else :
    print('Hello', username)
# part 1 section 10
hour = 21
if hour < 0 or hour > 23 :
    print('invalid hour')
elif hour > 12:
    print('Good Morning')
elif hour == 18:
    print('Good Afternoon')
else :
    print('Good Evening')