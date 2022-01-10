# https://www.101computing.net/random-password-generator/

import random
def shuffle (string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseLetter1 = chr(random.randint(65,90))
upperCaseLetter2 = chr(random.randint(65,90))
upperCaseLetter3 = chr(random.randint(65,90))
lowerCaseLetter1 = chr(random.randint(97,122))
lowerCaseLetter2 = chr(random.randint(97,122))
lowerCaseLetter3 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punctuation1 = chr(random.randint(33,47))
punctuation2 = chr(random.randint(33,47))
password = uppercaseLetter1 + upperCaseLetter2 + digit1 + digit2 + lowerCaseLetter1 + lowerCaseLetter2
password = shuffle(password)
print('Your random password is',password)
