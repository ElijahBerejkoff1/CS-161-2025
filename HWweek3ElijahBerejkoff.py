#Step 1 ask the user thier name
u_name = input("Hello! What is your name?")
if u_name == "Admin": #Put here so I dont have to do the entire name/age process. AKA a backdoor.
    pass
else:
    print (f"Hello {u_name} nice to meet you")
    #Step 2 ask their age and add 5
    # #u_age = input(f"{u_name},Eli how old are you?") #We get an error here, this is becuase we cannot add (or concatenate) a string and a integer together
    u_age = int(input(f"{u_name}, how old are you?")) #To fix the problem we must use the int() command
    print (f"In 5 years you will be {u_age + 5}") #however this does create more problems, if the user inputs something other than a number we are hit with a error
    # #Step 3, make a simple calculator for current age + x and print result
    x = int(input(f"If you are {u_age} now how many years would you like to add? +"))
    print (f"Ok! In {x} years you will be {u_age + x}")

#Step 4, Ask the user to enter values that might be floating point.
u_hours = float(input("How many hours did you work this week?"))
u_wage = float(input("What is your wage?"))
#Step 5, income
u_paycheck = print (f"This week you will make {u_wage * u_hours}$!")
u_paycheck = int(float(f"{u_wage * u_hours}"))
u_salary = float(u_paycheck * 48)
print (f"Your estimated salary before tax is ${u_salary}!")
if u_salary <= 11600.0:
    u_net = u_salary * .1
    print (f"After tax you will have ${u_salary - u_net}!")
if  11600.0 < u_salary <= 47150.0:
    u_net = u_salary * .12
    print (f"After tax you will have ${u_salary - u_net}")
if 47150.0 < u_salary <= 100525.0:
    u_net = u_salary * .22
    print(f"After tax you will have ${u_salary - u_net}")
if 100525.0 < u_salary <= 191950:
    u_net = u_salary * .24
    print(f"After tax you will have ${u_salary - u_net}")
if 191950.0 < u_salary <= 243725:
    u_net = u_salary * .32
    print(f"After tax you will have ${u_salary - u_net}")
if 243725 < u_salary <= 609350:
    u_net = u_salary * .35
    print(f"After tax you will have ${u_salary - u_net}")
if 609350.0 < u_salary:
    u_net = u_salary * .37
    print(f"After tax you will have ${u_salary - u_net}")
