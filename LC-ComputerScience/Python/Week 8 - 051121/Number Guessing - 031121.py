import random
number = random.randint(1,10)
print('The computer says',number,)
name = input('What is your name ?')
guess = int(input('Enter a number between 1 and 10: '))
close = int(number + 2)
close1 = int(number - 2)
#print('The computer says',number,)

if guess == number:
    print('Your guess was correct !')
    print('Well done',name,'!')
    
elif guess >= close1 and guess <= close:
    print('You were close!')
    
elif guess > number:
    print('Too high!')
    
elif guess < number:
    print('Too low!')
    
else:
    print('Your guess was wrong')
    print('Hard luck! ')
    
print('Goodbye')