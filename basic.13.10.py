#GET AND PRINT AVERAGE
#analyze an array's values and print the average

import array
gap = array.array('i', [1, 3, 6, 78, 95, 45, 999])

average = 0
average = sum(gap) / len(gap)
print(average)
print(sum(gap))
print(len(gap))
