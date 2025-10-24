# Jayden Murillo
# 10/8/25

import os
import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def main():
    user_min = 0
    user_max = 0
    user_range = 0

    while True:
        print("[-] 0. Exit \n"
              "[-] 1. Number Range Selection \n"
              "[-] 2. Sorting Methods \n")

        selection = int(input("What Do You Want To Do? Please Input The Number For Your Choice :) : "))

        os.system('cls' if os.name == 'nt' else 'clear')

        def validate_input():
            while True:
                try:

                    minimum_value = int(input("[-] What would you like as your minimum number/value? "))
                    maximum_value = int(input("[-] What would you like as your maximum number/value? "))
                    list_range = int(input("[-] How many numbers do you want in your list? "))

                    if minimum_value >= maximum_value:
                        print("[!] MIN & MAX ERROR! MIN VALUE HAS TO BE LESS THAN MAX VALUE! PLEASE TRY AGAIN")

                    if maximum_value > minimum_value and list_range > 0:
                        return minimum_value, maximum_value, list_range

                    if list_range < 0:
                        print("[!] RANGE ERROR! PLEASE INPUT A POSITIVE INTEGER MORE THAN 0! PLEASE TRY AGAIN")

                except:
                    print("[!] ERROR! PLEASE INPUT A INTEGER")

        if selection == 0:
            exit()

        if selection == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[-] In here, you choose the range of your numbers and how many numbers you want in that range for "
                  "your list!")

            user_min, user_max, user_range = validate_input()
            print("[-] Your numbers in your list will be from ", str(user_min), "-", str(user_max), "and it will have",
                  str(user_range), "numbers!")

        if selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[-] 0. Exit \n"
                  "[-] 1. Bubble Sort Method \n"
                  "[-] 2. Insertion Sort Method \n"
                  "[-] 3. Selection Sort Method \n")
            sub_selection = int(input("Please input the number for the sorting you would like to use for your list : "))

            if sub_selection == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                selection = 0
            if sub_selection == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                print("List before Sorting : ", str(values))
                bubble_sort(values)
                print("List after Sorting : ", str(values))

            if sub_selection == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                print("List before Sorting : ", str(values))
                insertion_sort(values)
                print("List after Sorting : ", str(values))
            if sub_selection == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                print("List before Sorting : ", str(values))
                selection_sort(values)
                print("List after Sorting : ", str(values))


if __name__ == "__main__":
    main()

# # generate a list of 10 random numbers from -10 to 10
# print(f"Initial Values = {values}")
# bubble_sort(values)
#
# sorted_list = bubble_sort(values)
# print(f"Sorted Values = {sorted_list}")

