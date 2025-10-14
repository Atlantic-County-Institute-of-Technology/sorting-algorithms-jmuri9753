
import random

values = [random.randint(0,10) for i in range(10)]

print("Initial Values =", values)


def selection_sort():

    for i in range(len(values) - 1):
        # Outer loop
        for j in range(len(values) + i + 1):
            minimum = i
            if values[j] < values[minimum]:
                minimum = j
            values[i], values[minimum] = values[minimum], values[i]

    return values


print("Sorted Values =", values)


