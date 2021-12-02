def display_gamelist(game_list):
    print(f"Here's the current list: \n{game_list}")

def position_choice():
    choice = "False"
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2):\n")
        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice!\n")
    return int(choice)

def replacement_choice(game_list,position):
    user_placement = input("Type a string to replace at selected pos:\n")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = "False"
    while choice not in ['y','n']:
        choice = input("Keep playing?(y/n):\n")
        if choice not in ['y', 'n']:
            print("Sorry, invalid choice!(y/n)\n")
        
    if choice == 'y':
        return True
    else:
        return False
   
game_on = True
game_list = [0, 1, 2]

while game_on:
    display_gamelist(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_gamelist(game_list)
    game_on = gameon_choice()


