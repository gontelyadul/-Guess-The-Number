import random
n = random.randint(1, 100)
a= -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number Please")
    guesses += 1

print("You have guessed the number {n} correctly in {gusses} attempt")
