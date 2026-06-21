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
    print('equal')
else:
    print('second is bigger')
# part 1 section 8