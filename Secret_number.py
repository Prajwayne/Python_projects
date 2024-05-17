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
#This function enables computer to guess the secret number 

def computer_guess(x):
    #set low and high.(Basically computer has to guess a number in the range provided)
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
        #Anything below low: stop considering || anything above high stop considering
         guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too hight (H), too low (L), or correct (C)??').lower()
        #if the guess is too high: adjust the upper bound
        if feedback =='h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1
    print(f"Absolute Genius! Thats is right,{guess}")

computer_guess(10)


