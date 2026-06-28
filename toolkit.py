# section 1 part 1
def greet(name):
    print("Hello",name)
greet(name="agentX")
# section 1 part 2
def add(num1,num2):
    print(num1+num2)
add(3,4)
# section 1 part 3
def square(num1):
    print(num1**2)
square(5)
# section 1 part 4
def greet_with_title(name,title="Agent"):
    print(f'Hello {title} {name}')
greet_with_title("Y")
greet_with_title(name="Y",title = "sir")
# section 1 part 5
def describe(name, level, active):
    print(f"name: {name} level: {level} active : {active}")
describe(name="michael", active=True, level=1)
# section 1 part 6
def multiply(num1,num2=2):
    print(num1*num2)
multiply(3)
multiply(2 ,10)
# section 1 part 7
def print_largest(a, b, c):
    if a <= b >= c:
        largest = b
    elif b <= a >= c:
        largest = a
    else:
        largest = c
    print(largest)
print_largest(5,3,8)
print_largest(10,2,7)
print_largest(4,4,1)
# section 1 part 8
def show_fahrenheit(c):
    fahrenheit = (c*9/5)+32
    print(fahrenheit)
show_fahrenheit(0)
show_fahrenheit(100)
show_fahrenheit(37.5)
# section 1 part 9
def check_even(n):
    if n % 2 == 0:
        print("the number is even")
    elif n % 2 == 1:
        print("the number is odd")
check_even(4)
check_even(7)
# section 1 part 10
def summarize(items):
    print(sum(items)) # I did another option at the end of file !
    print(min(items))
    print(max(items))
summarize(items=[4,9,2,10,3])
# section 2 part 1
def show_all(*args):
    for arg in range(len(args)):
        print(args[arg])
show_all("radio", "map", "flashlight")
# section 2 part 2
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_profile(name="Agent X", level=7, active=True)
# section 2 part 3
def power(base, exponent=2):
    print(base**exponent)
power(3)
power(3,3)
power(exponent=4, base=2)
# section 2 part 4
def repeat(text, times):
    print(text*times)
repeat("ha",3)
# section 2 part 5
def flatten_and_print(nested):
    for row in nested:
        for col in row:
            print(col)
flatten_and_print([[1, 2], [3, 4], [5]])


list1=[10,2,3,4,5,6,7,1,2,8,9,11,12,14,5,]
maxnum=list1[0]
for i in range(len(list1)):
    if maxnum<list1[i]:
        maxnum=list1[i]
    else:
        continue
print(maxnum)

minnum=list1[0]
for i in range(len(list1)):
    if minnum>list1[i]:
        minnum=list1[i]
    else:
        continue
print(minnum)

sumnum=0
for i in range(len(list1)):
    sumnum+=list1[i]
print(sumnum)

