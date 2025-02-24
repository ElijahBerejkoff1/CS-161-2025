#Step 1, Print Even Numbers Between Two User-Input Numbers
# Get user input for the lower and higher numbers
lower = int(input("Enter the lower number: "))
higher = int(input("Enter the higher number: "))
# Initialize an empty list to store even numbers
even_numbers = []
# Loop through the range from lower to higher (inclusive)
for num in range(lower, higher + 1):
    # Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num)
# Print the even numbers
print("The even numbers between", lower, "and", higher, "are:", ' '.join(map(str, even_numbers)))
#Step 2: Print All Factors of a Given Positive Integer
# Get user input for a positive integer
number = int(input("Enter a positive integer: "))
# Initialize an empty list to store factors
factors = []
# Initialize a counter variable
i = 1
# Loop to find all factors of the number
while i <= number:
    # Check if i is a factor of the number
    if number % i == 0:
        factors.append(i)
    i += 1
# Print the factors
print("The integers that are factors of", number, "are:", ' '.join(map(str, factors)))
#Step 3: Sum of Numeric Positions of Letters in a Name
# Define the alphabet list
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

# user input for a name
name = input("Enter your name: ").lower()
# Initialize a variable to store the sum
sum_positions = 0
# Loop through each letter in the name
for letter in name:
    # Add the position of the letter to the sum
    sum_positions += alphabet.index(letter)
# Print the sum of the positions
print("The sum of the numeric positions of the letters in your name is:", sum_positions)
#Step 4: Recursive Function to Print Squares of Integers
# Define the recursive function
def print_squares(n, current=1):
    # Base case: if current exceeds n, stop the recursion
    if current > n:
        return
    # Print the square of the current number
    print(current ** 2)
    # Recursive call with the next number
    print_squares(n, current + 1)
# Get user input for a positive integer
number = int(input("Enter a positive integer: "))
# Call the recursive function
print_squares(number)
#Step 4: TeePee Sort
# Define the unsorted list
unsorted_list = [12, 43, 22, 34, 2, 21, 3, 33, 81]
# Separate the list into odd and even numbers
odds = [num for num in unsorted_list if num % 2 != 0]
evens = [num for num in unsorted_list if num % 2 == 0]
# Sort odd numbers in ascending order
odds.sort()
# Sort even numbers in descending order
evens.sort(reverse=True)
# Find the largest number
largest = max(unsorted_list)
# Combine the sorted lists with the largest number in the center
sorted_list = odds + [largest] + evens
# Print the sorted list
print("Sorted list:", sorted_list)

#Step 6: Next Highest Number Algorithm (This was really hard lol)
# Function to find the next highest number
def next_highest_number(digits):
    # Convert the number to a list of digits
    digits = list(map(int, str(digits)))

    # Find the first digit that is smaller than the digit next to it
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        # If no such digit is found, return that no higher number is possible
        return "No higher number possible"

    # Find the smallest digit on the right side of the found digit that is larger than the found digit
    for j in range(len(digits) - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Swap the found digits
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits after the found digit
    digits = digits[:i + 1] + digits[i + 1:][::-1]

    # Convert the list of digits back to a number
    return int(''.join(map(str, digits)))

# Get user input for a number
number = int(input("Enter a number: "))

# Find and print the next highest number
print("The next highest number is:", next_highest_number(number))