# Jayden Murillo
# 10/8/25

import random
from bubble_sort import bubble_sort


def main():
    while True:
        print("[-] 0. Exit \n"
              "[-] 1. Number Range Selection \n"
              "[-] 2. Sorting Methods \n")

        selection = int(input("What Do You Want To Do? Please Input A Number :) : "))

        if selection == 0:
            exit()

    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()

# # generate a list of 10 random numbers from -10 to 10
# values = [random.randint(-10, 10) for i in range(20)]
# print(f"Initial Values = {values}")
# bubble_sort(values)
#
# sorted_list = bubble_sort(values)
# print(f"Sorted Values = {sorted_list}")

