# section 1
menu_choice = input(f'Please enter your choice: \n 1) forest \n 2) cave \n 3) river\n')
if menu_choice == "forest":
    forest_choice = str(input('choose tp hide or walk : '))
    if forest_choice == "hide":
       print('You hide behind a tree ')
    elif forest_choice == "walk":
        print('You find a sleeping wolf')
    else:
       print('Invalid forest action')
elif menu_choice == "cave":
    cave_choice = str(input('do you have a torch : '))
    if cave_choice == "yes":
        cave_dircetions = str(input('you want to go left or to the right  : '))
        if cave_dircetions == "left":
            print('You find gold  ')
        elif cave_dircetions == "right":
            print('You find bats')
        else:
            print('Invalid path')
    else :
        print('Its too dark to enter')
elif menu_choice == "river":
    print('You find a boat')
else:
    print('unknown place')
# section 2
num1 = float(input('enter your first number: : '))
num2 = float(input('enter your second number: : '))
calculator_action = input(f'choose your calculator action : \n 1) add\n 2) subtract\n 3) multiply\n')
if calculator_action == "add" or calculator_action == "1" :
    print('the add of the tow numbers is : ',num1 + num2)
elif calculator_action == "subtract" or calculator_action == "2" :
    print('the subtract of the tow numbers is : ',num1 - num2)
elif calculator_action == "multiply" or calculator_action == "3"  :
    print('the multiply of the tow numbers is : ',num1 * num2)
else:
    print('Invalid calculator action')
# section 3
computer_choice = "rock"
user_chose_for_rock_etc = input(f'choose \n 1) rock \n 2) paper \n 3) scissors\n')
if user_chose_for_rock_etc == computer_choice:
    print('drow')
elif user_chose_for_rock_etc == "paper":
    print('you win')
elif user_chose_for_rock_etc == "scissors":
    print('you lose')
else :
    print('INVALID CHOICE')
# section 4
correct_pin = 4321
balance = 500
user_PIN_input = int(input('Enter your PIN: '))
if user_PIN_input == correct_pin:
    Withdrawal=int(input('how much you want to withdraw?: '))
    if Withdrawal>balance:
        print('not enough money')
    else:
        want_receipt = input('do yo want to receipt?: yes/no ')
        if want_receipt=='yes':
            print('Withdrawal approved with receipt')
        elif want_receipt=='no':
            print('Withdrawal approved without receipt')
        else:
            print('Withdrawal approved')
else:
    print('wrong password')
# section 5
order_price = float(input('enter your order price: '))
if order_price <= 50:
    print('order to small for delivery')
else:
    club_number = input('enter your if you have club number yes/no : ')
    if club_number == 'yes':
        coupon = input('do you have a coupon ?  yes / no : ')
        if coupon == 'yes':
            print('you got free delivery and 10% discount')
        else:
            print('you got only free delivery')
    else:
        print('delivery cost is 15$')