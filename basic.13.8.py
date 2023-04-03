#PRINT ODDS 1-255
#print all odd integers from 1 to 255

for i in range(1, 256, 2):
    print(i)

#OR

for i in range(1, 256):
    if i % 2 != 0:
        print(i)

