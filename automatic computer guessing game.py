import random
def computer_guessing_game(c,v):
    high=c
    low=1
    number=v
    x=0
    y=0
    while x!=3:
        guess=random.randint(low,high)
        if number>guess:
            low=guess+1
            y+=1
            print(f'computer guessed {guess} on its {y} try')
        elif number<guess:
            high=guess-1
            y += 1
            print(f'computer guessed {guess} on its {y} try')
        elif guess==number:
            y+=1
            print(f'compute guessed your number {guess} in {y} times')
            x=3
computer_guessing_game(1000,226)
