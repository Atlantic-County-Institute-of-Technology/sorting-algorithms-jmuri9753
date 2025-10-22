
# import random
#
# numbers = [random.randint(-10, 10) for i in range(10)]  # Gets 10 random numbers from 0-19
#
# print("Initial Values =", numbers)  # Prints the unchanged values in numbers first
#

def insertion_sort(values):
    # Values in this function is what's inside numbers, is serves as a placeholder for the values in numbers
    for i in range(1, len(values)):  # This starts i from 1, so that sorting can happen, the first values all the way-
        # -till the last value
        # Outer Loop
        temp = values[i]  # This makes a temporary variable equal to whatever i is/what value i is inside the list
        j = i - 1      # This makes J equal the value behind i, for example if i = 2, then j = 1
        while j >= 0 and temp < values[j]:
            # This is the condition for sorting. If j is 0 or greater than 0 and if the temporary variable(whatever i is
            # -equal to in the list) is less than whatever j is in the list (Which is the previous number behind i) then
            # -the code will execute. The loop keeps going until the first value is sorted correctly.
            values[j + 1] = values[j]  # This is saying that if the condition is true then i (j+1) = j, this swaps the-
            # -values
            j -= 1  # Then this sets j back to j-1 because above, it make it equal to j+1 which is i
            values[j + 1] = temp  # This sets back the temporary variable to i (j+1)

    return values # This returns the sorted values inside numbers
#
#
# numbers = insertion_sort(numbers)  # This makes number equal to the sorted numbers
#
# print("Changed Values =", numbers)  # This prints out the sorted numbers since numbers now equals it.

