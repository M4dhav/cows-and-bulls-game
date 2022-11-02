import random
num = random.randint(1000, 9999+1)
num = str(num)
print(num)
def play(acnum):
        guesses = 0
        l1 = []
        l2 = []
        l4 = []
        while True:
            l4 = []
            pnum =(input("Enter your guess: "))
            if pnum == acnum:
                print("Congratulations! You Win.")
                print("You took {} guesses".format(guesses))
                l3 = ["yes", "ye", "sure", "ok"]
                pagain =(input().lower())
                if pagain in l3:
                    continue
                else:
                    break
            for i in pnum:
                l1.append(int(i))
            for j in acnum:
                l2.append(int(j))
            if(pnum[0] == acnum[0]) and(pnum[1] == acnum[1]) and(pnum[2] == acnum[2]):
                print("3 Cows, 0 Bulls")
            elif ((pnum[0] == acnum[0]) and(pnum[1] == acnum[1])) or ((pnum[1] == acnum[1]) and(pnum[3] == acnum[3])) or ((pnum[0] == acnum[0]) and(pnum[2] == acnum[2])) or ((pnum[2] == acnum[2]) and(pnum[3] == acnum[3])):
                for a in l1:
                    if a in l2:
                        l4.append(a)
                if len(l4) == 3:
                    print("2 Cows, 1 Bulls")
                elif len(l4) == 4:
                    print("2 Cows, 2 Bulls")
                elif len(l4) == 2:
                    print("2 Cows, 0 Bulls")
            elif (pnum[0] == acnum[0]) or(pnum[1] == acnum[1]) or(pnum[2] == acnum[2]) or(pnum[3] == acnum[3]):
                for a in l1:
                    if a in l2:
                        l4.append(a)
                if len(l4) == 2:
                    print("1 Cows, 1 Bulls")
                elif len(l4) == 3:
                    print("1 Cows, 2 Bulls")
                elif len(l4) == 4:
                    print("1 Cows, 3 Bulls")
                elif len(l4) == 1:
                    print("1 Cows, 0 Bulls")
            else:
                print("0 Cows, 0 Bulls")
            guesses += 1
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
    pass
elif i == 2:
    play(num)
elif i == 3:
    print("Thanks for looking it over")
    exit()