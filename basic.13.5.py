#GREATER THAN Y
#given an array and a value Y, count and print the number ...
#of array values greater than Y

import array
array_Y = array.array('i', [1,4,67,7,45,666,9])

Y = 30
for i in array_Y:
    if i > Y:
        print(i)


        #