import random
import math

lower = int(input("Enter low end: "))
upper = int(input("Enter high end: "))

x = random.randint(lower, upper)
print("\nYou only have ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Great job! You guessed correctly in ", count, " tries")

        break
    elif x > guess:
        print("Higher")
    elif x < guess:
        print("Lower")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tSorry, you lost")
