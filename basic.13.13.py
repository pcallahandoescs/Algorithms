#SHIFT ARRAY VALUES
#given an array, move all values forward by one index...
#dropping the first and leaving a '0' value at the end.

import array

shift = array.array('i', [1, 5, 6, 68, 90, 666])

for i in range(len(shift)-1):
    shift[i] = shift[i+1]

shift[-1] = 0

print(shift)

