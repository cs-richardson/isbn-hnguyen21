'''
This code takes any 10 digit number and sees if its a valid ISBN number.
The code will reprompt the user if the input is not a number or not 10 digits.
By Ben
'''

isbn = input("IBSN: ")

#Reprompt
while isbn.isdigit() == False or len(isbn) != 10:
    isbn = input("Retry: ")


checkDigit = int(isbn) % 10
checkSum = 0

#Calculation
for digit in range(9,0,-1):
    isbnDigit = ((int(isbn) // (10 ** (10 - digit))) % 10) * digit
    checkSum = checkSum + isbnDigit

#Output
if checkSum % 11 == checkDigit:
    print("YES")

else:
    print("NO")
