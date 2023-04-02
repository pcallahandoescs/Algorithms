#MAX, MIN, AVERAGE
#given an array, print the max, min and average values for that array

import array
the_array = array.array('i', [45, 6, 17, 3888, 52, 3])

min = the_array[0]
for i in range(1, len(the_array)):
    if the_array[i] < min:
        min = the_array[i]

max = the_array[0]
for i in range(1, len(the_array)):
    if the_array[i] > max:
        max = the_array[i]

avg = the_array[0]
for i in range(1, len(the_array)):
    if the_array[i]:
        avg += the_array[i]
avg /= len(the_array)

print(min)
print(max)
print(avg)
