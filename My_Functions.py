#Rock Paper Scissors=
def rock_paper_scissors(): #make the entire thing a function because I want only 2 lines when I collapse it
    # Function to get valid input
    def get_valid_input(player):
        attempts = 4
        while attempts > 0:  # while loop to determine when the player has gone over the attempts
            player_input = input(
                f"Enter 'rock', 'paper', 'scissors' for {player}: ").lower()  # tell the player to enter something and make sure everything is lowercase
            if player_input in ["rock", "paper", "scissors"]:  # make sure they put in the right thing
                print(f"{player} has a valid input")
                return player_input
            else:  # if they did not put in a valid input it says so, takes away 1 attempt, and goes back to the while loop start
                attempts -= 1
                print(f"{player} does not have a valid input. {attempts} attempts remaining.")
        print(f"{player} Is kinda dumb lol.")
        exit()

    # assigning players input to their name
    player1 = get_valid_input("Player 1")
    player2 = get_valid_input("Player 2")

    # create function to determine which player actually wins the game
    def game_winner(player1, player2):
        if player1 == player2:  # if they tie it exits the program
            print("Tie")
            exit()
        # the determinator for the winner. Pretty simple, we check if player 1 wins and if he didn't then player 2 wins
        elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (
                player1 == "scissors" and player2 == "paper"):
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")

        print("Thank You For Playing")

    game_winner(player1, player2)
#Binary translator
def binary_translator():
    user_input = int(input("Enter a number (0 to 255): "))
    x = user_input
    # test to see if our input is too large or negative
    if x >= 256:
        print("Input value is too large. Not allowed.")
        exit()
    if x < 0:
        print("Input value is negative. Not allowed")
        exit()
    b = [0] * 8  # Make our list be 8 numbers long
    # Start forming our list of 0s and 1s using b[]
    if x >= 128:
        b[0] = 1
        x -= 128
    if x >= 64:
        b[1] = 1
        x -= 64
    if x >= 32:
        b[2] = 1
        x -= 32
    if x >= 16:
        b[3] = 1
        x -= 16
    if x >= 8:
        b[4] = 1
        x -= 8
    if x >= 4:
        b[5] = 1
        x -= 4
    if x >= 2:
        b[6] = 1
        x -= 2
    if x >= 1:
        b[7] = 1
        x -= 1

    binary = "".join(map(str, b))  # Convert the list to a string
    print(f"Binary form of {user_input} is: {binary}")  # print out our binary number
    print("Thanks for using the Binary Robot!!")
#Rock paper scissors vs computer
def RPS_Computer():
    import random
    # Generate computer's choice
    random_choice = random.randint(1, 3)
    rock_dict = {1: "rock", 2: "scissors", 3: "paper"}
    computer = rock_dict[random_choice]
    # Player 1 attempts
    attempts1 = 4
    player_name = input("Welcome to Rock Paper Scissors! Please enter your name: ")
    while attempts1 > 0:
        player = input("Enter 'rock', 'paper', 'scissors' for " + player_name + ":").lower()
        if player in ["rock", "paper", "scissors"]:
            print(player_name + " has a valid input")
            break
        else:
            attempts1 -= 1
            print(player_name + f" does not have a valid input. {attempts1} attempts remaining.")
    if attempts1 == 0:
        print(player_name + "is kinda dumb... ending game.")
        exit()
    # Determine the winner
    if player == computer:
        print("It's a tie")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (
            player == "scissors" and computer == "paper"):
        print(player_name + f" wins with {player}")
        print(f"Computer loses with {computer}")
        human_wins_graphic()
    else:
        print(f"The computer wins with {computer}")
        print(player_name + f" loses with {player}")
        computer_winner_graphic()
    print("Thank You For Playing")
#Human wins graphic for PRS
def human_wins_graphic():
    import turtle
    window = turtle.Screen()
    human_wins_graphic = turtle.Turtle()
    human_wins_graphic.color("blue")
    human_wins_graphic.speed(999)
    human_wins_graphic.pensize(2)
    human_wins_graphic.shape('turtle')
    human_wins_graphic.penup()
    human_wins_graphic.goto(100, 50)
    human_wins_graphic.left(180)
    human_wins_graphic.forward(200)
    human_wins_graphic.right(90)
    human_wins_graphic.forward(100)
    human_wins_graphic.right(180)
    human_wins_graphic.pendown()
    human_wins_graphic.forward(200)
    human_wins_graphic.right(180)
    human_wins_graphic.forward(100)
    human_wins_graphic.right(90)
    human_wins_graphic.forward(150)
    human_wins_graphic.right(90)
    human_wins_graphic.forward(100)
    human_wins_graphic.right(180)
    human_wins_graphic.forward(200)
    human_wins_graphic.hideturtle()
    window.mainloop()
#Computer wins graphic for RPS
def computer_winner_graphic():
    import turtle
    window = turtle.Screen()
    compter_w = turtle.Turtle()
    compter_w.color('red')
    compter_w.speed(999)
    compter_w.pensize(2)
    compter_w.penup()
    compter_w.right(180)
    compter_w.goto(0, 120)
    compter_w.pendown()
    compter_w.circle(120, 185)
    compter_w.hideturtle()
    window.mainloop()
#RPS with inputs from a separate file, only works with names.txt but can be modified
def rps_name_file():
    import random
    # Function to determine the winner
    def determine_winner(name, player_choice, computer_choice):
        if player_choice == computer_choice:
            print("It's a tie\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or (
                player_choice == "paper" and computer_choice == "rock") or (
                player_choice == "scissors" and computer_choice == "paper"):
            print(name + f" wins with: {player_choice}")
            print(f"Computer loses with: {computer_choice}\n")
        else:
            print(f"The computer wins with: {computer_choice}\n")

    # Open the file and initialize variables
    with open("names.txt", "r") as names:
        for name_line in names:
            if not name_line.strip():
                continue  # Skip empty lines
            split_names = name_line.strip().split()
            if len(split_names) < 3:
                print(f"Invalid line: {name_line.strip()}")
                continue  # Skip lines with insufficient data
            if split_names[2] == "-":
                substring = split_names[3]  # Update substring to 3rd word if 2nd is "-"
            else:
                substring = split_names[2]  # Otherwise, use 2nd word
            name = split_names[0]  # Assign the name to the input
            if substring in ["rock", "scissors", "paper"]:
                print(name + " has a valid input: " + substring)
            else:
                print(name + " does not have a valid input.")
                continue
            # Generate computer's choice
            random_choice = random.randint(1, 3)
            rock_dict = {1: "rock", 2: "scissors", 3: "paper"}
            computer = rock_dict[random_choice]

            # Determine the winner
            determine_winner(name, substring, computer)

    print("Thank You For Playing")

    rps_name_file()