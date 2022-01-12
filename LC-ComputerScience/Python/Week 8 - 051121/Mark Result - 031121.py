mark1 = int(input('What mark did you recieve in the exam ? '))
if mark1 > 100:
    print('Value must be between 0 and 100')
subject = input('Subject: ')
if mark1 >= 90:
    print('You recieved a H1 in',subject)
elif mark1 >= 80:
    print('You recieved a H2 in',subject)
elif mark1 >= 70:
    print('You recieved a H3 in',subject)
elif mark1 >= 60:
    print('You recieved a H4 in',subject)
elif mark1 >= 50:
    print('You recieved a H5 in',subject)
elif mark1 >= 40:
    print('You recieved a H6 in',subject)
elif mark1 >= 30:
    print('You recieved a H7 in',subject)
elif mark1 < 20:
    print('You recieved a H8 in',subject)
    print('You have failed')