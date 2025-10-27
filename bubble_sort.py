# Jayden Murillo
# 10/8/25

def bubble_sort(values, outer_pass = 0, inner_pass = 0): # Adds values, outer_pass, and inner_pass as parameters
    # perform the bubblesort
    for i in range(len(values) - 1): # Performs selection sort and subtracts 1 from the total range of values, which is a placeholder for the users list, so i does not loop through more than the range is.
        outer_pass += 1 # Adds one to outer pass which is equal to the number of times a loop is executed
        # assume the final value in each pass is sorted
        for j in range(len(values) - i - 1): # Makes sure that j is less than i, so j is one number behind i
            # perform the swap using a temp variable
            if values[j] > values[j+1]: # This is basically saying that if the number behind i is greater, then the code under the if statement will execute
                inner_pass += 1 # Adds one to the inner pass which is equal to the number of sorting actions taken to sort the list
                values[j], values[j+1] = values[j+1], values[j]
                # Swaps j and i
                # temp = values[j]
                # values[j] = values[j+1]
                # values[j+1] = temp

    return values, outer_pass, inner_pass # This returns the sorted list, the number of times a loop is executed, and the number of sorting actions taken to sort the list
