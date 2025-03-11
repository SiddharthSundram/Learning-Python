import random
import math

upper = int(input("Enter upper limit:"))
lower = int(input("Enter lower limit:"))
x = random.randint(lower,upper)

print(f"You've {round(math.log(upper-lower+1,2))}, chances to guess the integer.")
count = 0
while count < (math.log(upper-lower+1,2)):
    count+=1
    guess = int(input("Enter your guess: "))
    if x == guess:
        print(f"Congratulation You did it in {count} try.")
        break
    elif x > guess:
        print("You guess too small.")
    elif x < guess:
        print("You guess too high.")
        
    if count > (math.log(upper-lower+1,2)):
        print(f"The number is {x}")
        print("Better luck next time!!")