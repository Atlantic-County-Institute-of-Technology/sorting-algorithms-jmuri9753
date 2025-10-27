# Jayden Murillo
# 10/8/25

def insertion_sort(values, outer_pass = 0, inner_pass = 0): # Adds values, outer_pass, and inner_pass as parameters
    # Values in this function serves as a placeholder for the users list
    for i in range(1, len(values)):  # This starts i from 1, so that sorting can happen, the first values all the way till the last value
        outer_pass += 1 # Adds one to outer pass which is equal to the number of times a loop is executed
        # Outer Loop
        temp = values[i]  # This makes a temporary variable equal to whatever i is/what value i is inside the list
        j = i - 1      # This makes J equal the value behind i, for example if i = 2, then j = 1
        while j >= 0 and temp < values[j]:
            # Inner Loop
            inner_pass += 1 # Adds one to the inner pass which is equal to the number of sorting actions taken to sort the list
            # This is the condition for sorting. If j is 0 or greater than 0 and if the temporary variable(whatever i is
            # -equal to in the list) is less than whatever j is in the list (Which is the previous number behind i) then
            # -the code will execute. The loop keeps going until the first value is sorted correctly.
            values[j + 1] = values[j]  # This is saying that if the condition is true then i (j+1) = j, this swaps the-
            # -values
            j -= 1  # Then this sets j back to j-1 because above, it make it equal to j+1 which is i
            values[j + 1] = temp  # This sets back the temporary variable to i (j+1)

    return values, outer_pass, inner_pass # This returns the sorted list, the number of times a loop is executed, and the number of sorting 
    # actions taken to sort the list


