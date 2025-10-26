# Jayden Murillo
# 10/8/25

# import random library for list generation
# import random

# # generate a list of 10 random numbers from -10 to 10
# values = [random.randint(-10, 10) for i in range(20)]
# print(f"Initial Values = {values}")
#



def bubble_sort(values, outer_pass = 0, inner_pass = 0):
    # perform the bubblesort
    for i in range(len(values) - 1):
        outer_pass += 1
        # assume the final value in each pass is sorted
        for j in range(len(values) - i - 1):
            inner_pass += 1
            # perform the swap using a temp variable
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                # temp = values[j]
                # values[j] = values[j+1]
                # values[j+1] = temp

    return values, outer_pass, inner_pass


# print(f"Sorted Values = {values}")
# print(f"Outer passes: {outer_pass} | Inner passes: {inner_pass}")
