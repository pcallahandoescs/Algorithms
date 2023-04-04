#SQUARE THE VALUES
#square each value in a given array, returning that same array with changed values

import array
square = array.array('i', [1, 4, 6, 8, 9])

for i in range(0, len(square)):
    square[i] *= square[i]
    
print(square)
