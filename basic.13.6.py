#MAX, MIN, AVERAGE
#given an array, print the max, min and average values for that array

import array
the_array = array.array('i', [45, 6, 17, 3888, 52, 3])

print(max(the_array))
print(min(the_array))

average = sum(the_array) / len(the_array)
print(average)
