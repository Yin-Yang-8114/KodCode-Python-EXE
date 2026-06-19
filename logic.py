# part 1 section 1
is_online = True
has_access = False
print (f'is online and has access : {is_online and has_access}' )
# part 1 section 2
print (f'is online or has access : {is_online or has_access}' )
# part 1 section 3
status = False
print(f' status is not  : {not status}')
# part 1 section 4
age = 20
has_id = True
print(f' the person can enter {age > 18 and has_id == True}')
# part 1 section 5
level = 3
print (f' level is {1 <= level <= 5}')
# part 1 section 6
a = 0
b = "hello"
c = ""
print (f'the truthiness pf a is : {(bool(a))}\nthe truthiness pf b is : {(bool(b))}\nthe truthiness pf c is : {(bool(c))}')
# part 1 section 7
x = None
y = 42
print (f' the result of X or Y is : {x or y}') # בגלל שבפייתון OR בודק ומחזיר את הערך האמת שהראשון שהוא מוצא ובמקרה שלנו זה המספר42 תודה רבה ושבת שלום ומבורך לכל עם ישראל אשר בגלות ואשר בין בים ובין ביבשה
# part 1 section 8
username = ""
default = "guest"
print (f'the final username is {username or default}')
# part 1 section 9
print (True and False or True)
print((True and False) or True)
# part 1 section 10
score = 75
print (f'the score is between 60 to 100 :{60 < score < 100} ')