
import random

values = [random.randint(0,10) for i in range(10)]

print("Initial Values =", values)


def insertion_sort():
    for i in range(1, len(values)):
        # Outer Loop
        # if i < range(len(values)):
        #     j = i - 1
        #     index = values[i]
        #     for j in range(len(values)):
        #         while j >= 0 and i < j:
        #             values[j], index = index, values[j]
        temp = values[i]
        j = i - 1
        while j >= 0 and temp < values[j]:
            values[j + 1] = values[j]
            j -= 1
            values[j + 1] = temp

    return values


print("Changed Values =", values)

