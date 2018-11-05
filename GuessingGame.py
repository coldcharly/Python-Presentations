import random
def guessNumbers():
    num = random.randint(1,100)
    tries = 0
    while True:
        print("Guess a number between 1-100...")
        your_num = int(input())
        if your_num > num:
            print("Your number is too big!")
            tries = tries + 1
        elif your_num < num:
            print("your number is too small!")
            tries = tries + 1
        else:
            print("Hooray, you got it in {} tries!".format(tries))
            break
guessNumbers()
    
    
