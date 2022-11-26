
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A or B): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses))
    print("Your score is: "+str(score))

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
    "Computeer works on binary language.":"A",
    "Python is a high level language.":"B",
    "Assembly language is combination of Machine language and High level language.":"B",
    "IP in IP adress stands for Internet prototype.":"A",
    "HTTP is more secure protocol than HTTPS.":"B",
    "Ram is also known as volatile memory.":"A",
    "Processors are made up of capacitors.":"B",
    "Python was developed in the year 1992.":"A",
    "Fiber optic router is used for better internet speed.":"B",
    "HDD(hard disk drive) are faster than SDD(Solid state drive).":"A",
}

options = [
          ["A.True", "B. False"],
          ["A. True","B. False"],
          ["A. True","B. False"],
          ["A. True","B. False"],
          ["A. True","B. False"],
          ["A.True", "B. False"],
          ["A. True","B. False"],
          ["A. True","B. False"],
          ["A. True","B. False"],
          ["A. True","B. False"] 
          ]

new_game()

while play_again():
    new_game()


print("You got" + str(score) + "/" + str(len(questions)) +"correct" )