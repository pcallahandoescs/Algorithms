#ZERO OUT NEGATIVE NUMBERS
#return the given array, after setting any negative values to zero

import array
zero_a = array.array('i', [1, -4, 6, -8, 81, 69, -9000])

zero = 0
for i in range(0, len(zero_a)):
    if zero_a[i] < zero:
        zero_a[i] = zero

print(zero_a)