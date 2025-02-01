#Step 1
def average(num1, num2, num3):
    '''Def the average of num1 and num2 and num3'''
    return (num1 + num2 + num3)/3
print(average(197,35,100))
print (average(5, 10, 10))
#Step 2, Move the function definition after the print statements.
#I put the following into a docstring because i dont want my code to error each time i use it but i want to show my work.
"""
print (average1(1, 5, 12))
print (average1(26, 19, 25))
def average1(num1, num2, num3):
    #This was supposed to be in a docstring but i cant otherwise i will get errors: Same thing as above but def after
    return (num1 + num2 + num3)/3
#Returning the error name 'average1' is not defined for line 8. This is becuase the code works from top to bottom. So this code will not work
#Step 3 Print out the value of a parameter outside a function definition
def average1(num1, num2, num3):
    return (num1 + num2 + num3)/3
print (average(7, 5, 9))
print (average(6, 6, 7))
print (num1)
#I dont think this script will run becuase num1 hasnt been assigned a value AS a variable.
"""
#Step 4  Define a function that converts a dog's age into human years
def human_years(num4):
    '''Calculation for human to dog years'''
    return (24 + (num4 - 2) * 4)
dog_years = (human_years(4))
print (f"If a dog is 4 years old they are {dog_years} years old as a human.")
#Step 5, Define a function that will calculate the value of a car. Input to the function is the purchase price of the car, the number of years, and type of car.
psw = input ("Key word:")
if psw == "Admin": #Ender Admin if you dont want to re-do the whole thing
    pass
else:
    def calculate_car_value(car_purchase_price, car_years, car_type):
        """Calculate all of our diffrent variables in lines 45-47"""
        if car_type.lower() == "german": #if statements to determain wich contry the car is from
            return car_purchase_price * (0.95 ** car_years) #Calculate the value
        elif car_type.lower() == "japanese":
            return car_purchase_price * (0.93 ** car_years)
        elif car_type.lower() == "italian":
            return car_purchase_price * (1.05 ** car_years)
        else:
            return "Not sure what type of car you are looking for" #If user enters the wrong contry this is a failsafe


    car_purchase_price = float(input("Enter how much your car cost: ")) #define our variables using floats and integers when necessary
    car_years = int(input("Enter the amount of years its been since you bought the car: "))
    car_type = input("Enter the type of car (German, Japanese, Italian): ")

    car_value = calculate_car_value(car_purchase_price, car_years, car_type) #send our inputs to line 31 for calculation
    print(f"The value of the car after {car_years} years is: ${car_value}") #and finally print the result

#Step 6,  Define a function that converts a dog’s age into human years and RETURNs the result. Outside of the function, allow a user to input their dog’s age and name.  Print out “Your Spot is 22.3 human years old”
psw1 = input("Word:")
if psw1 == "Admin": #Again as above so you dont have to keep doing through the whole process
    pass
else:
    # Function to convert dog's age into human years
    def dog_to_human_years(dog_age1):
        """The calculation for dog years to human years from variable lines 66 and 67"""
        human_years1 = 24 + (dog_age1 - 2) * 4
        return human_years1


    # User input
    print("Dog’s Age Calculator:")
    dog_name = input("What is your dog’s name? ")
    dog_age1 = float(input(f"How old is {dog_name}? "))

    # Calculate human years and print result
    human_years1 = dog_to_human_years(dog_age1)
    print(f"{dog_name} is {human_years1} human years old.")
#Step 7, Calculate the price of an ice cream cone
# Function to calculate the price of an ice cream cone
def calculate_cone_price(scoops):
    """I scream for ice cream!! takes variable from line 81 and does the calcuation for ice cream price"""
    price = scoops * 1.15 + 2.25
    return price

# User input
print("Ice cream cone price calculator:")
scoops = int(input("How many scoops would you like? "))

# Calculate the price and print result
price = calculate_cone_price(scoops)
print(f"A {scoops}-scoop cone will cost ${price:.2f}")
print("End of process, thank you")
