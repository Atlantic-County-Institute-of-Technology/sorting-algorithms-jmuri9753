
import random

numbers = [random.randint(-10,10) for i in range(10)]

print("Initial Values =", numbers)


def selection_sort(values):

    for i in range(len(values) - 1):
        # Outer loop
        min_val = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_val]:
                min_val = j
        values[i], values[min_val] = values[min_val], values[i]

    return values


numbers = selection_sort(numbers)

print("Sorted Values =", numbers)


