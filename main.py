import os
import random
import time
import utils.game_msg as msg

# global consts
grid_col_count = 4
ship_count = 2
trail_no = 5
target_hitted = False

# game data
computer_ship_position = []
computer_ship_targeted = []

# function to genrate random pair
def generate_pair():
    num1 =  random.randint(0, grid_col_count-1)
    num2 = num = random.randint(0, grid_col_count-1)
    return [num1, num2]


# clear screen function
def clear_screen() :
     os.system('cls')


# function to place randomly computer ships
def place_computer_ship() :
    while(len(computer_ship_position) <= ship_count) :
        ship_pos = generate_pair()
        # print(ship_pos)
        if ship_pos not in computer_ship_position :
            computer_ship_position.append(ship_pos)
    with open("./utils/location.txt", "w") as out_file:
         out_file.write(str(computer_ship_position))


# function to display grid with targeted ships
def display_grid(ship_pos) :
     print("\t\t\t\t-------------------------------")
     for i in range(grid_col_count) :            
            print("\t\t\t\t", end="")
            for j in range(grid_col_count) :
                if [i, j] in ship_pos :
                    print("|  X  |", end=" ")
                    continue
                print(f"| {i},{j} |", end=" ")
            print()
     print("\t\t\t\t-------------------------------")

#check win
def win() :
    if(len(computer_ship_position) == 0) :
          print("Player wins")
          return True
    return False






if __name__ == "__main__" :
     clear_screen()
     print(msg.story_msg)
     place_computer_ship()     
    #  print(computer_ship_position)
     time.sleep(2)     
     clear_screen()
     for i in range(trail_no):
            if(len(computer_ship_position) == 0):
                 break
            print(msg.info_msg)
            if target_hitted :
                 print("\t\t\t\tCongrates You Hitted the Target\n\n")
            else :
                 print()
            print(f"\t\t\t\t\t\t\t\t\tOnly {trail_no-i} missiles remained")
            display_grid(computer_ship_targeted)
            target_hitted = False
            row, col = input("\t\t\t\t\t\t\t\t\tTarget enemy ship : ").split(',')
            target = [int(row), int(col)]
            if target in computer_ship_position :
                computer_ship_position.remove(target)
                computer_ship_targeted.append(target)
                target_hitted = True
            clear_screen()
     
     if(len(computer_ship_position) == 0):
          print(msg.win_msg)
     else :
          print(msg.lost_msg)

     display_grid(computer_ship_targeted)
     print("\n\n\n\n\n")



    