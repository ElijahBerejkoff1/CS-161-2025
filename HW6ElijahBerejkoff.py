#Step 1, 2, and 3
x1 = int(input("Enter a positive number:"))
dec = int(input("Enter a number to decrease by:"))
while (x1 > 0): #While statement to count down by one, with the users input. And determain which numbers are odd/even
    print (f"T-{x1}")

    if x1 % 2 == 0: #To test if the number is positive or negative.
        print (f"{x1} is even")
    else:
        print (f"{x1} is odd")
    if dec <= 1: #This statement is to show the use of x = x-1 as that is the instructions in step 1
        x1 = x1-1
    else:
        x1 = x1 - dec
print("Liftoff!") #When while statement is done print liftoff!
#Step 4.1 and 4.2
word = input("Enter a word:")
e = 1 #I will use this string to track how many times the while loop has executed
while len(word) > 5:
    #word = word[:-1]
    print(f"{word} is {len(word)} letters long")
    word = input("Enter a word:")
    e = e +1
    if e >= 5: #If statement to break if user inputs a word more than 5 letters, 5 times
        print("Loser")
print ("Goodbye")
#Step 5
number = 10
# While loop to count from 10 to 100
while number <= 100:
    # Print the number in decimal, binary, and hexadecimal formats
    print(f"Decimal: {number} | Binary: {bin(number)} | Hexadecimal: {hex(number)}")

    # Increment the counter
    number += 1
print("Done")
#Step 6
#Iterative approach
def print_stars_iterative(x):
    """while loop that continues to execute as long as x is greater than zero"""
    while x > 0:
        print('*' * x)
        x -= 1
#Example
print_stars_iterative(5)

#Recursive approach
def print_stars_recursive(x):
    """recursive function that calls itself with x - 1 until x is zero"""
    if x > 0:
        print('*' * x)
        print_stars_recursive(x - 1)
#Example
print_stars_recursive(5)
#Extra Credit:
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# Examples
print(sum_of_digits(1234))  # Output: 10
print(sum_of_digits(99991))  # Output: 37
print(sum_of_digits(51))  # Output: 6
