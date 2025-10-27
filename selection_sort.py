# Jayden Murillo
# 10/8/25

def selection_sort(values, outer_pass = 0, inner_pass = 0): # Adds values, outer_pass, and inner_pass as parameters
    for i in range(len(values) - 1):  # Performs selection sort and subtracts 1 from the total range of values, 
        # which is a placeholder for the users list, so i does not loop through more than the range is.
        outer_pass += 1 # Adds one to outer pass which is equal to the number of times a loop is executed
        min_val = i # Makes the minimum value of the function i
        for j in range(i + 1, len(values)): # This makes j greater than i by 1, j is the number in front of i.
            if values[j] < values[min_val]: # This is saying that if j, the number in front of i, is less than i, the number behind j, 
                # then the code for the if statement will execute.
                inner_pass += 1 # Adds one to the inner pass which is equal to the number of sorting actions taken to sort the list
                min_val = j # This switches the minimum value of the list, so that the new minimum value of the list is j, since its 
                # less than the number behind it, i.
        values[i], values[min_val] = values[min_val], values[i] # This swaps the j and i, so that since j is less than i, j should 
        # naturally be behind i since were sorting the list.

    return values, outer_pass, inner_pass # This returns the sorted list, the number of times a loop is executed, and the number of 
    # sorting actions taken to sort the list
