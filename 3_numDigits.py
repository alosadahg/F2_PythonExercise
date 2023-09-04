scan = input("Please enter a number: ")
numDigits = 0;
maxN = 0
minN = 0
for c in scan:
    if c.isdigit():
        c = int(c)
        if(numDigits == 0):
            minN = c
        numDigits += 1
        if(c < minN):
            minN = c
        if(c > maxN):
            maxN = c
print("Number of digits in the given number is: ", numDigits)
print("Smallest number is: ", minN)
print("Highest number is: ", maxN)

