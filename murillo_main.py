# Jayden Murillo
# 10/8/25

import os   # Importing Os lets us clear the terminal from previous python code executions
import random # Importing Random Lets us randomly get integers within a certain range
import time # Importing Time lets us to write code in order to find out the number of time it takes for a sorting method to sort a users list
from bubble_sort import bubble_sort # This lets us get our bubble sort function from another file, where our function is located
from insertion_sort import insertion_sort   # This lets us get our insertion sort function from another file, where our function is located
from selection_sort import selection_sort   # This lets us get our selection sort function from another file, where our function is located


def main(): # The function where our project is in
    user_min = 0    # User's minimum value for their list
    user_max = 0    # User's maximum value for their list     It's out of the while True loop so that these values for the user for their list does not reset when the while True loop loops
    user_range = 0  # User's range value for their list

    while True: # Makes sure that the function keeps the code running fro the project as long as the function is true/called


        print("[-] Main Menu: \n"
              "  [-] 0. Exit \n"                    # Prints out the main menu and the available options for the user to choose from
              "  [-] 1. Number Range Selection \n"
              "  [-] 2. Sorting Methods \n")

        # Allows the user to input the option they want by inputting the options number
        selection = int(input("What Would You Like To Do? Please Input The Number That Corresponds With Your Choice: ")) 

        os.system('cls' if os.name == 'nt' else 'clear')    # Clears the terminal from previously executed code

        def validate_input(): # Function for validating the users input in Number Range Selection
            while True: # Makes sure that the users input is checked as long as the function is called
                try: # Executes code that could cause a error 

                    minimum_value = int(input("[-] What Would You Like As Your Minimum Number/Value? "))
                    maximum_value = int(input("[-] What Would You Like As Your Maximum Number/Value? "))    # Allows the user to input their minimum, maximum, and range values for their list
                    list_range = int(input("[-] How Many Numbers Do You Want In Your List? "))

                    # Prints out a error and reason for the error to the user if the min they inputed is greater than the max they inputed.
                    # It lets them to retry inputting different values that satisfy the conditions for the inputs to work
                    if minimum_value >= maximum_value:
                        print("[!] MINIMUM & MAXIMUM VALUE ERROR! MINIMUM VALUE HAS TO BE LESS THAN THE MAXIMUM VALUE! PLEASE TRY AGAIN")

                    # Checks if the the users input for their max is greater than the value they inputted for their min and also checks if the range value they inputted
                    # is greater than 0. If these conditions are true, then it returns the values that the user inputed for the max, min, and range for their list.
                    if maximum_value > minimum_value and list_range > 0:
                        return minimum_value, maximum_value, list_range

                    # Prints out a error and reason for the error to the user if the range they inputted is not a positive number or greater than 0
                    # It allows the user to retry inputting different values that satisfy the conditions for the inputs to wwork
                    if list_range <= 0:
                        print("[!] RANGE ERROR! PLEASE INPUT A POSITIVE INTEGER MORE THAN 0! PLEASE TRY AGAIN")
                # Prints out a error if in any of the executed code, there is something other than a number inputted
                except:
                    print("[!] ERROR! PLEASE INPUT A INTEGER")

        if selection == 0:  # This is if the user chooses the exit the project
            exit()  # Closes the project

        if selection == 1:  # This is if the user selects the numbers range selection option from the main menu
            os.system('cls' if os.name == 'nt' else 'clear')    # Clears the terminal from previously executed code
            # Gives an explanation to the user of what they can do in the option they chose
            print("[-] In Here You Get To Customize Your Own List! You Get To Choose The Values Your List Ranges From And To And How Many Numbers You Want In That List!")
            # Calls the validation function and sets variables to equal whats returned from the function, the users input for min, max, and range, in chronological order
            # These varibales are so that we can use the users input for the entire project as long as the input fulfills certain conditions
            # user_min = minimum_value, user_max = maximum_value, user_range = list_range
            user_min, user_max, user_range = validate_input()
            # Tells the user from what numbers their list will be from and how many numbers their list will have depending on their inputs 
            print("[-] The Numbers In Your List Will Be From", str(user_min), "To", str(user_max), "And Your List Will Have", str(user_range), "Numbers! \n")
            # Notifys the user that they are going back to the main menu
            print("[!] Returning To The Main Menu... \n")


        if selection == 2: # This is if the user selects the sorting methods option from the main menu
            os.system('cls' if os.name == 'nt' else 'clear')    # Clears the terminal from previously executed code
            print("[-] 0. Exit \n"
                  "[-] 1. Bubble Sort Method \n"
                  "[-] 2. Insertion Sort Method \n"         # Prints out a menu of numbered sorting methods the user can choose from
                  "[-] 3. Selection Sort Method \n")
            # Allows the user to chose a sorting method by inputting the methods number
            sub_selection = int(input("[-] Please Input The Number That Corresponds With The Sorting Method You Would Like To Use For Your List: "))

            if sub_selection == 0: # This is if the user wants to exit the sorting methods menu
                os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal from previously executed code
                selection = 0 # Makes the user selection 0, so that it takes the user back to the main menu
            if sub_selection == 1: # This is if the user selects the bubble sort method from the menu
                os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal from previously executed code
                # Makes values equal to a randomly generated list based on the users inputs for the min, max, and range
                values = [random.randint(user_min, user_max) for i in range(user_range)] 
                # Prints out the users sorting method that they chose and the randomly generated list/values before the sorting method is used
                print("[-] Bubble Sort Method:  \n" 
                "  [-] List Before Sorting:", str(values))
                # Starts a timer before the sorting method's function is called, before the list is sorted.
                start_time = time.perf_counter()
                # Calls the bubble sort function and sets variables equal to whats returned from the function in chronological order.
                # sorted_values = values, loop_executions = outer_pass =0, sorting_actions = inner_pass=0.
                # We set these variables equal whats returned from the function so that we can use the values that were returned
                sorted_values, loop_executions, sorting_actions = bubble_sort(values, outer_pass = 0, inner_pass = 0)
                # Ends the timer after the sorting method's function is called, after the list got sorted.
                end_time = time.perf_counter()
                # Sets the total time that elapsed for the list to get sorted by the function equal to the final time minus to initial time
                total_time = end_time - start_time
                # Prints out the list after it was sorted by the sorting method the user chose
                print("  [-] List After Sorting:", str(sorted_values))
                # Gives the user the option to see the performance metrics of the sorting method based on their numbered input
                performance_selection = int(input("  [-] Would You Like To See The Sorts Performance Metrics? Please Input 0 For No And 1 For Yes: "))

                if performance_selection == 1: # This is if the user chooses to see the performance metrics of the sorting method
                    # Prints out the performance metrics of the sorting method: the number of executed loops, the number of sorting actions, and the total time the sorting method took to sort the users list.
                    print(" [-] Performance Metrics:")
                    print("  [-] Number Of Executed Loops:", str(loop_executions))
                    print("  [-] Number Of Sorting Actions:", str(sorting_actions))
                    print(f"  [-] Total Time To Sort: {total_time:.5f}s \n")
                    # Notifys the user that they are being taken back to the main menu
                    print("[!] Returning To The Main Menu... \n")

                if performance_selection == 0: # This is if the user chooses not to see the performance metrics of the sorting method
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal of previously executed code
                    print("[!] Returning To The Main Menu... \n") # Notifys the user that they are being taken back to the main menu
                    sub_selection = 0 # Makes the users sub selection in the sorting methods menu 0, so that it takes the user back to the main menu

                # Else statement was printing even when it shouldn't have so I used a elif statement so that if the user inputs anything other than 0 or 1 for the performance metrics option then it prints out a error for the user
                elif performance_selection < 0 or performance_selection > 1:
                    print("[!] ERROR. PLEASE INPUT 0 FOR NO OR 1 FOR YES")

            if sub_selection == 2:  # This is if the user selects the insertion sort method from the menu
                os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal from previously executed code
                # Makes values equal to a randomly generated list based on the users inputs for the min, max, and range
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                # Prints out the users sorting method that they chose and the randomly generated list/values before the sorting method is used
                print("[-] Insertion Sorting Method: \n"
                "  [-] List Before Sorting:", str(values))
                # Starts a timer before the sorting method's function is called, before the list is sorted.
                start_time = time.perf_counter()
                # Calls the insertion sort function and sets variables equal to whats returned from the function in chronological order.
                # sorted_values = values, loop_executions = outer_pass =0, sorting_actions = inner_pass=0.
                # We set these variables equal whats returned from the function so that we can use the values that were returned
                sorted_values, loop_executions, sorting_actions = insertion_sort(values, outer_pass = 0, inner_pass = 0)
                # Ends the timer after the sorting method's function is called, after the list got sorted.
                end_time = time.perf_counter()
                # Sets the total time that elapsed for the list to get sorted by the function equal to the final time minus to initial time
                total_time = end_time - start_time
                # Prints out the list after it was sorted by the sorting method the user chose
                print("  [-] List After Sorting:", str(sorted_values))
                # Gives the user the option to see the performance metrics of the sorting method based on their numbered input
                performance_selection = int(input("  [-] Would You Like To See The Sorts Performance Metrics? Please Input 0 For No And 1 For Yes : "))

                if performance_selection == 1: # This is if the user chooses to see the performance metrics of the sorting method
                    # Prints out the performance metrics of the sorting method: the number of executed loops, the number of sorting actions, and the total time the sorting method took to sort the users list.
                    print(" [-] Performance Metrics:")
                    print("  [-] Number Of Executed Loops:", loop_executions)
                    print("  [-] Number Of Sorting Actions:", sorting_actions)
                    print(f"  [-] Total Time To Sort: {total_time:.5f}s \n")
                    # Notifys the user that they are being taken back to the main menu
                    print("[!] Returning To The Main Menu... \n")

                if performance_selection == 0: # This is if the user chooses not to see the performance metrics of the sorting method
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal from previously executed code
                    print("[!] Returning To The Main Menu... \n") # Notifys the user that they are being taken back to the main menu
                    sub_selection = 0  # Makes the users sub selection in the sorting methods menu 0, so that it takes the user back to the main menu

                # Else statement was printing even when it shouldn't have so I used a elif statement so that if the user inputs anything other than 0 or 1 for the performance metrics option then it prints out a error for the user
                elif performance_selection < 0 or performance_selection > 1:
                    print("[!] ERROR. PLEASE INPUT 0 FOR NO OR 1 FOR YES")

            if sub_selection == 3:   # This is if the user selects the selection sort method from the menu
                os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal from previously executed code
                # Makes values equal to a randomly generated list based on the users inputs for the min, max, and range
                values = [random.randint(user_min, user_max) for i in range(user_range)]
                # Prints out the users sorting method that they chose and the randomly generated list/values before the sorting method is used
                print("[-] Selection Sorting Method: \n"
                "  [-] List Before Sorting:", str(values))
                # Starts a timer before the sorting method's function is called, before the list is sorted.
                start_time = time.perf_counter()
                # Calls the insertion sort function and sets variables equal to whats returned from the function in chronological order.
                # sorted_values = values, loop_executions = outer_pass =0, sorting_actions = inner_pass=0.
                # We set these variables equal whats returned from the function so that we can use the values that were returned
                sorted_values, loop_executions, sorting_actions = selection_sort(values, outer_pass = 0, inner_pass = 0)
                # Ends the timer after the sorting method's function is called, after the list got sorted.
                end_time = time.perf_counter()
                # Sets the total time that elapsed for the list to get sorted by the function equal to the final time minus to initial time
                total_time = end_time - start_time
                # Prints out the list after it was sorted by the sorting method the user chose
                print("  [-] List After Sorting:", str(sorted_values))
                # Gives the user the option to see the performance metrics of the sorting method based on their numbered input
                performance_selection = int(input("  [-] Would You Like To See The Sorts Performance Metrics? Please Input 0 For No And 1 For Yes: "))

                if performance_selection == 1: # This is if the user chooses to see the performance metrics of the sorting method
                    # Prints out the performance metrics of the sorting method: the number of executed loops, the number of sorting actions, and the total time the sorting method took to sort the users list.
                    print(" [-] Performance Metrics:")
                    print("  [-] Number Of Executed Loops:", loop_executions)
                    print("  [-] Number Of Sorting Actions:", sorting_actions)
                    print(f"  [-] Total Time To Sort: {total_time:.5f}s \n")
                    # Notifys the user that they are being taken back to the main menu
                    print("[!] Returning To The Main Menu... \n")

                if performance_selection == 0:
                    # This is if the user chooses not to see the performance metrics of the sorting method
                    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal from previously executed code
                    print("[!] Returning To The Main Menu... \n") # Notifys the user that they are being taken back to the main menu
                    sub_selection = 0 # Makes the users sub selection in the sorting methods menu 0, so that it takes the user back to the main menu

                # Else statement was printing even when it shouldn't have so I used a elif statement so that if the user inputs anything other than 0 or 1 for the performance metrics option then it prints out a error for the user
                elif performance_selection < 0 or performance_selection > 1:
                    print("[!] ERROR. PLEASE INPUT 0 FOR NO OR 1 FOR YES")

        # The else statement was printing when it shouldn't have been so instead I used a elif statement so that if the users input for their main menu selection if anything not between 0-2 or 0 and 2, then a error would be printed out for them
        elif selection < 0 or selection > 2:
            print("[!] ERROR. PLEASE SELECT AN ACTUAL OPTION")
        


if __name__ == "__main__":  # This checks to see if our file name has "main" in it and if it doe it calls the function for the project
    main()


