# Function to convert decimal to binary number

def binaryconversion(n):
    print(n % 2, end='')
    if n > 1:
        binaryconversion(n // 2)  # Use integer division here

number = int(input("Enter Number: "))
binaryconversion(number)
print()
