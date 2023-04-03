#SWAP STRING FOR ARRAY NEGATIVE VALUES
#replace any negative array values with 'Patrick!'

import array
rep_array = array.array('i', [13, -6, 17, -888, -99, 10])

rep_list = list(rep_array)
for i in range(len(rep_list)):
    if rep_list[i] < 0:
        rep_list[i] = 'Patrick!'

print(rep_list)