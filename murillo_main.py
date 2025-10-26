# Jayden Murillo
# 10/8/25

import os
import random
import time
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

        selection = int(input("What Would You Like To Do? Please Input The Number That Corresponds With Your Choice :) : "))

        os.system('cls' if os.name == 'nt' else 'clear')

        def validate_input():
            while True:
                try:

                    minimum_value = int(input("[-] What Would You Like As Your Minimum Number/Value? "))
                    maximum_value = int(input("[-] What Would You Like As Your Maximum Number/Value? "))
                    list_range = int(input("[-] How Many Numbers Do You Want In Your List? "))

                    if minimum_value >= maximum_value:
                        print("[!] MINIMUM & MAXIMUM VALUE ERROR! MINIMUM VALUE HAS TO BE LESS THAN THE MAXIMUM VALUE! PLEASE TRY AGAIN")

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
            print("[-] In Here You Get To Customize Your Own List! You Get To Choose The Values Your List Ranges From And How Many Number You Want In That List!")

            user_min, user_max, user_range = validate_input()
            print("[-] Your Numbers In Your List Will Be From", str(user_min), "To", str(user_max), "And It Will Have",
                  str(user_range), "Numbers!")

        if selection == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[-] 0. Exit \n"
                  "[-] 1. Bubble Sort Method \n"
                  "[-] 2. Insertion Sort Method \n"
                  "[-] 3. Selection Sort Method \n")
            sub_selection = int(input("Please Input The Number That Corresponds With The Sorting Method You Would Like To Use For Your List : "))

            if sub_selection == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                selection = 0
            if sub_selection == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                print("[-] List Before Sorting : ", str(values))
                start_time = time.perf_counter()
                sorted_values, loop_executions, sorting_actions = bubble_sort(values, outer_pass = 0, inner_pass = 0)
                end_time = time.perf_counter()
                total_time = end_time - start_time

                print("[-] List After Sorting : ", str(sorted_values))
                print("[-] Number Of Loops Execution: ", loop_executions)
                print("[-] Number Of Sorting Actions: ", sorting_actions)
                print(f"[-] Total Time To Sort: : {total_time:.5f}s \n") 



            if sub_selection == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                print("[-] List Before Sorting : ", str(values))
                start_time = time.perf_counter()
                sorted_values, loop_executions, sorting_actions = insertion_sort(values, outer_pass = 0, inner_pass = 0)
                end_time = time.perf_counter()
                total_time = end_time - start_time

                print("[-] List After Sorting : ", str(sorted_values))
                print("[-] Number Of Loops Execution: ", loop_executions)
                print("[-] Number Of Sorting Actions: ", sorting_actions)
                print(f"[-] Total Time To Sort: : {total_time:.5f}s \n") 

            if sub_selection == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                print("[-] List Before Sorting : ", str(values))
                start_time = time.perf_counter()
                sorted_values, loop_executions, sorting_actions = selection_sort(values, outer_pass = 0, inner_pass = 0)
                end_time = time.perf_counter()
                total_time = end_time - start_time

                print("[-] List After Sorting : ", str(sorted_values))
                print("[-] Number Of Loops Execution: ", loop_executions)
                print("[-] Number Of Sorting Actions: ", sorting_actions)
                print(f"[-] Total Time To Sort: : {total_time:.5f}s \n")

            else: 
                print("[!] ERROR. PLEASE SELECT AN ACTUAL OPTION")
        


if __name__ == "__main__":
    main()


