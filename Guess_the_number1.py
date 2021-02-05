import random
number=random.randint(1,30)
guess_taken=0
print('You Have to Guess a number within 6 attempts.')
print('Enter your name:')
name=input()
print('Welcome '+ name)

print('Guess a number between 1 to 30')
for guess_taken in range(6):
    print('Take a guess')
    guess=input()
    guess=int(guess)
    if guess<number:
        print('Guess is too low')
    elif guess>number:
        print('Guess is too high')
    else:
        break

if guess==number:
    print("You've guessed in "+ str(guess_taken+1) +"th attempts")
    print('Congratulation   '+ name)

else:
    print('Sorry , Try again')
