def decToBinary(dec):
    orig = dec
    bin = ""

    if dec == 0:
        bin = '0'
    else:
        while dec > 0:
            r = dec % 2
            bin = str(r) + bin
            dec = dec // 2

    print("Binary representation of", orig, ": ", bin)

def binaryToN(bin, type):
    orig = bin
    dec = 0
    i = 0

    while (bin != 0):
        val = bin % 10
        dec = dec + val * pow(2, i)
        bin = bin // 10
        i += 1
    f_char = type[0]

    if(f_char == 'o') or (f_char == 'O'):
        decToOctal(dec)
    elif(f_char == 'h') or (f_char == 'H'):
        decToHex(dec)
    else:
        print("Binary representation of", orig, ": ", dec)

def decToOctal(dec):
    orig = dec
    oct = ""
    while dec > 0:
        r = dec % 8
        oct = str(r) + oct
        dec //= 8
    print("Octal representation of", orig, ": ", oct)

def decToHex(dec):
    orig = dec
    oct = ""
    while dec > 0:
        r = dec % 16
        oct = str(r) + oct
        dec //= 16
    print("Hexadecimal representation of", orig, ": ", bin)

def main():
    flag = True
    while flag==True:
        print("Available conversions"
                     "\n1. Decimal to Binary"
                     "\n2. Binary to N"
                     "\n3. Decimal to Octal"
                     "\n4. Decimal to Hexadecimal"
                     "\n5. Exit")
        scan = input("Select a conversion to perform: ")
        if(scan == 5):
            print("Thank you for using my conversion program!")
            return
        n = input("Please enter a value: ")
        if scan == '1':
            n = int (n)
            decToBinary(n)
        elif scan == '2':
            t = input("Please enter a type (Decimal, Octal, or Hexadecimal): ")
            binaryToN(n, t)
        elif scan == '3':
            n = int(n)
            decToOctal(n)
        elif scan == '4':
            n = int(n)
            decToHex(n)
        else:
            print("Invalid input. Please try again.")
        again = input("Perform another conversion? Y/N: ")
        if (again[0] != 'Y') or (again[0] != 'y'):
            flag = False

if __name__ == '__main__':
    main()