u = input("Enter word:")
if u == "skip":
    pass
else:
    # Step 1
    word1 = input("Enter a sentence in lowercase:")
    word2 = input("Enter the same sentence in uppercase:")
    print(word1 == word2.lower())  # Checking to see if the inputs are the same
    print("Stop shouting please!")
    # Step 2
    word3 = input("Enter a string in lowercase:")
    count = 0
    for char in word3:
        if char == 'a':
            count += 1
        elif char == 'e':
            count += 1
        elif char == 'i':
            count += 1
        elif char == 'o':
            count += 1
        elif char == 'u':
            count += 1

    print("The total number of vowels is:", count)
    # Step 3
    # Ask the user to enter two strings
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")

    # Compare the two strings and print the one that comes first alphabetically
    if string1 < string2:
        print(f"{string1} comes before {string2}")
    else:
        print(f"{string2} comes before {string1}")
#Step 4
while True:
    email1 = input("Enter your email: ")
    email2 = input("Enter your email again: ")
    if email1 == email2:
        print(f"{email1} and {email2} are the same email")
        break
    else:
        print("Emails don't match, please try again")
#Step 5
import time

# Iterative factorial function
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive factorial function using recur_vvv as variable
def recursive_factorial(recur_vvv):
    if recur_vvv == 1:
        return 1
    else:
        return recur_vvv * recursive_factorial(recur_vvv - 1)

# Function to measure and print the time taken by both methods
def measure_time(n):
    # Measure time for iterative factorial
    start = time.perf_counter_ns()
    iterative_result = iterative_factorial(n)
    stop = time.perf_counter_ns()
    iterative_time = stop - start

    # Measure time for recursive factorial
    start = time.perf_counter_ns()
    recursive_result = recursive_factorial(n)
    stop = time.perf_counter_ns()
    recursive_time = stop - start

    # Print results
    print(f"For input {n}:")
    print(f"Iterative factorial: {iterative_result}, Time taken: {iterative_time} ns")
    print(f"Recursive factorial: {recursive_result}, Time taken: {recursive_time} ns")
    print()

    return iterative_time, recursive_time
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
user_input = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial of user input
result = factorial(user_input)
start = time.perf_counter_ns()
stop = time.perf_counter_ns()
print(stop - start)
print(f"The factorial of {user_input} is {result} and it took {stop - start} ns")
#I cant figure out how to make it in table form as in the instruction example.