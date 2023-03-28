#Array with odds
#Create an array with all the odd integers between 1 and 255 (inclusive)

import array
odds_array = array.array('i', [i for i in range(1, 256) if i % 2 == 1])
print(odds_array)