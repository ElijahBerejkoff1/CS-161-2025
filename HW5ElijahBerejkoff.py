#Step 1, Write an if statement to determine if a number is divisible by 5.
def divisable_5(num1):
    """Checks to see if the number is divisable by 5"""
    return num1 % 5 == 0
num1 = float(input("Enter a number: "))
print(f"{num1} is divisable by 5?")
print(divisable_5(num1))
#Step 2.1, Use if and elifs to print the name of a state capital when given the name of the state (only need to do 5 or 6 states)
#Step 2.2, Create a dictionary of the states and capitals and use a get() to print the name of the capital from the dictionary
#And step 3 Ask the user to enter a State/Province name, and print out the capital of that state.  Your code should handle at least 6 different inputs.  Use an if/elif/else structure
state_capitals = {"Oregon":"Salem", "California": "Sacremento", "Florida": "Tallahassee"
    , "New York": "Albany", "Texas": "Austin", "Georgia": "Atlanta"}
state = input("Enter a state: ")
if (state == 'Oregon'):
    print("Salem")
elif (state == 'Florida'):
    print("Tallahassee")
elif (state == 'Georgia'):
    print("Atlanta")
elif (state == 'California'):
    print("Sacremento")
elif (state == 'New York'):
    print("Albany")
elif (state == 'Texas'):
    print("Austin")
else:
    print("Not sure please try again")
capital = state_capitals.get(state)
#Step 4,  Use elif in a function definition.  Use docstrings to document your function
def movie_tickets(age):
    """Takes the input of an age and return a dollar value based on that input"""
    if (age <= 3):
        return 0
    if (age <= 6):
        return 8
    if (age < 18):
        return 10
    if (age >= 18):
        return 12
age = int(input("Enter your age to buy a movie ticket: "))
print (f"To buy a movie ticket at {age} years old it will cost {movie_tickets(age)}")

#PART 2 in the assignment,  Determine how many times the string “160” appears in the HTML code for coccbobcat.com
import requests
url = "http://coccbobcat.com"
response = requests.get(url)
count = url.count("160")
print(f'The string "160" appears {count} times in the HTML code for {url}.')
#Step 2 in part 2, Write a Python program that will determine the number of processes running on your system
import psutil

def count_processes():
    processes = psutil.pids()
    number_of_processes = len(processes)
    return number_of_processes

if __name__ == "__main__":
    print("Number of processes running:", count_processes())
#Had to look up a youtube tutorial for this one but got it working