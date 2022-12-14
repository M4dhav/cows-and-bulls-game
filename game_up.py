import random
import time
l3 = ["yes", "ye", "sure", "ok", "2", "y"]
rules = '''1. A random 4 digit number will be picked by the computer, and you will have to guess it.
2.For every digit that you have guessed correctly in the correct place, you have a cow. 
  For every digit that you have guessed correctly in the wrong place, you have a bull.
3.Try to replay the game until you have the best score you can. Your number of guesses indicate the score. Lower the Guesses, Higher the score.'''
def play():
        acnum = random.randint(1000, 9999+1)
        acnum = str(acnum)
        guesses = 0
        l1 = []
        l2 = []
        l4 = []
        while True:
            
            cows = 0
            bulls = 0
            guesses += 1
            l4 = []
            pnum =(input("Enter your guess: "))
            try:
                int(pnum)
            except:
                print("*----------------------------------------------------------*")
                print("ERROR!\n".center(35))
                print("Please enter NUMBERS only!!")
                print("Try Again:".center(33))
                print("*----------------------------------------------------------*")
                guesses -= 1
                continue
            if len(pnum) != 4:
                print("*----------------------------------------------------------*")
                print("ERROR!\n".center(35))
                print("Please enter a 4 DIGIT NUMBER only!!")
                print("Try Again:".center(33))
                print("*----------------------------------------------------------*")
                guesses -= 1
                continue
            if pnum == acnum:
                print("Congratulations! You Win.")
                print("You took {} guesses".format(guesses))
                pagain =(input("Would you like to play again?\n").lower())
                if pagain in l3:
                    play()
                else:
                    time.sleep(0.5)
                    print("Thanks for playing. I hope you play again later!")
                    time.sleep(3)
                    break
            l1=list(pnum)
            l2=list(acnum)
            for i in range(len(pnum)):
                if pnum[i] == acnum[i]:
                    cows += 1
                    l1.remove(pnum[i])
                    l2.remove(acnum[i])
            for a in l1:
                if a in l2:
                    l4.append(a)
            bulls += len(l4)
            print("{} Cows, {} Bulls".format(cows, bulls))
            print("*----------------------------------------------------------*")
print("Cows and Bulls Game\n")
print("*----------------------------------------------------------*")
print("Menu:")
print("*----------------------------------------------------------*")
print("1. Rules")
print("2. Play")
print("3. Exit")
print("*----------------------------------------------------------*")
i = int(input("Choose an option(1/2/3):\n"))
print("*----------------------------------------------------------*")
if i == 1:
    print('Rules:')
    print(rules)
    print("*----------------------------------------------------------*")
    pl = input("Would you like to play now?:\n").lower()
    if pl in l3:
        play()
    else:
        print("Alright, have a nice day. Hope to see you here again.")
elif i == 2:
    play()
elif i == 3:
    print("Thanks for looking it over")
    time.sleep(3)
    exit()