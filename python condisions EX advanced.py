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
calculator_action = str(input(f'choose your calculator action : \n 1) add\n 2) subtract\n 3) multiply\n'))
if calculator_action == "add" or "1" :
    print('the add of the tow numbers is : ',num1 + num2)
elif calculator_action == "subtract" or "2" :
    print('the subtract of the tow numbers is : ',num1 - num2)
elif calculator_action == "multiply" or "3" :
    print('the multiply of the tow numbers is : ',num1 * num2)
else:
    print('Invalid calculator action')
# section 3
