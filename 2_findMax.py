x, y, z = map(int, input("Please enter three values: ").split())
maxVal = 0
if (x>y) and (x>z):
        maxVal = x
elif (y>z):
    maxVal = y
else:
    maxVal = z
print("The maximum value is ", maxVal)