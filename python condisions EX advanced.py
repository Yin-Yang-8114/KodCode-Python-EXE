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
