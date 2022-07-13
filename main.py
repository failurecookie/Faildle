import random as random

def setup():
    # Open Valid Word List
    global wordlist
    words = open("words.txt")
    wordpassing = words.read()
    wordlist = wordpassing.split("\n")
    words.close()

    # Sets up a Random Word to Start
    global answer
    answer = wordlist[random.randint(0,2315)]
    print(f"The answer was: {answer}.")

def gameloop():
    run = True
    while run:
        print("Impossidle (0.0.1)\n[][][][][]\n[][][][][]\n[][][][][]\n[][][][][]\n[][][][][]\n[][][][][]\n")
        choice = input("Please type your word guess: ")
        # if (choice in wordlist):
        #    print(answer)


if __name__ == "__main__":
    setup()
    gameloop()