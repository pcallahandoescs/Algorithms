#Print Sum 0-255
#Print integers from 0 to 255, and with each integer print the sum so far

sum = 0
for i in range(1, 256):
    sum += i
    print(i, sum)