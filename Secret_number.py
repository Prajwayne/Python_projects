import random 
def guess(x):
    rand_num = random.randint(1, x)
    guess = 0

    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}"))
        if guess < rand_num:
            print("Guess is to low")
        elif guess > rand_num:
            print('Guess is Too High')
        
    print(f"Awsome! thats right{rand_num}")


x = int(input("Whats the maximum of random numbers can you guess"))
guess(x)