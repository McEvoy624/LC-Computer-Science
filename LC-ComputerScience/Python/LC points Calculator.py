print('Leaving Certificate Points Calculator \nEnter in your percentage result from each exam and you will recieve your total points \nEnter in all 7 subjects results')
result7 = int(input('What result did you recieve in Maths ?: '))
if result7 > 100:
    print('Invalid entry')
elif result7 >= 90:
    points7 = 125
    score7 = 'H1'
elif result7 >= 80:
    points7 = 113
    score7 = 'H2'
elif result7 >= 70:
    points7 = 102
    score7 = 'H3'
elif result7 >= 60:
    points7 = 91
    score7 = 'H4'
elif result7 >= 50:
    points7 = 81
    score7 = 'H5'
elif result7 >= 40:
    points7 = 71
    score7 = 'H6'
elif result7 >= 30:
    points7 = 37
    score7 = 'H7'
else:
    points7 = 0
    score7 = 'H8'
print('You recieved a',score7,'in maths')

subject1 = 'Irish'
result = int(input('What result did you recieve in Irish?: '))
if result > 100:
    print('Invalid entry')
elif result >= 90:
    points = 100
    score = 'H1'
elif result >= 80:
    points = 88
    score = 'H2'
elif result >= 70:
    points = 77
    score = 'H3'
elif result >= 60:
    points = 66
    score = 'H4'
elif result >= 50:
    points = 56
    score = 'H5'
elif result >= 40:
    points = 45
    score = 'H6'
elif result >= 30:
    points = 37
    score = 'H7'
else:
    points = 0
    score = 'H8'
print('You recieved a',score,'in',subject1)

subject2 = 'English'
result2 = int(input('What result did you recieve in English ?: '))
if result2 > 100:
    print('Invalid entry')
elif result2 >= 90:
    points2 = 100
    score2 = 'H1'
elif result2 >= 80:
    points2 = 88
    score2 = 'H2'
elif result2 >= 70:
    points2 = 77
    score2 = 'H3'
elif result2 >= 60:
    points2 = 66
    score2 = 'H4'
elif result2 >= 50:
    points2 = 56
    score2 = 'H5'
elif result2 >= 40:
    points2 = 45
    score2 = 'H6'
elif result2 >= 30:
    points2 = 37
    score2 = 'H7'
else:
    points2 = 0
    score2 = 'H8'
print('You recieved a',score2,'in',subject2)

subject3 = input('Enter your 4th subject: ')
result3 = int(input('What result did you recieve ?: '))
if result3 > 100:
    print('Invalid entry')
elif result3 >= 90:
    points3 = 100
    score3 = 'H1'
elif result3 >= 80:
    points3 = 88
    score3 = 'H2'
elif result3 >= 70:
    points3 = 77
    score3 = 'H3'
elif result3 >= 60:
    points3 = 66
    score3 = 'H4'
elif result3 >= 50:
    points3 = 56
    score3 = 'H5'
elif result3 >= 40:
    points3 = 45
    score3 = 'H6'
elif result3 >= 30:
    points3 = 37
    score3 = 'H7'
else:
    points3 = 0
    score3 = 'H8'
print('You recieved a',score3,'in',subject3)

subject4 = input('Enter your 5th subject: ')
result4 = int(input('What result did you recieve ?: '))
if result4 > 100:
    print('Invalid entry')
elif result4 >= 90:
    points4 = 100
    score4 = 'H1'
elif result4 >= 80:
    points4 = 88
    score4 = 'H2'
elif result4 >= 70:
    points4 = 77
    score4 = 'H3'
elif result4 >= 60:
    points4 = 66
    score4 = 'H4'
elif result4 >= 50:
    points4 = 56
    score4 = 'H5'
elif result4 >= 40:
    points4 = 45
    score4 = 'H6'
elif result4 >= 30:
    points4 = 37
    score4 = 'H7'
else:
    points4 = 0
    score4 = 'H8'
print('You recieved a',score,'in',subject1)

subject5 = input('Enter your 6th subject: ')
result5 = int(input('What result did you recieve ?: '))
if result5 > 100:
    print('Invalid entry')
elif result5 >= 90:
    points5 = 100
    score5 = 'H1'
elif result5 >= 80:
    points5 = 88
    score5 = 'H2'
elif result5 >= 70:
    points5 = 77
    score5 = 'H3'
elif result5 >= 60:
    points5 = 66
    score5 = 'H4'
elif result5 >= 50:
    points5 = 56
    score5 = 'H5'
elif result5 >= 40:
    points5 = 45
    score5 = 'H6'
elif result5 >= 30:
    points5 = 37
    score5 = 'H7'
else:
    points5 = 0
    score5 = 'H8'
print('You recieved a',score5,'in',subject5)

subject6 = input('Enter your 7th subject: ')
result6 = int(input('What result did you recieve ?: '))
if result6 > 100:
    print('Invalid entry')
elif result6 >= 90:
    points6 = 100
    score6 = 'H1'
elif result6 >= 80:
    points6 = 88
    score6 = 'H2'
elif result6 >= 70:
    points6 = 77
    score6 = 'H3'
elif result6 >= 60:
    points6 = 66
    score6 = 'H4'
elif result6 >= 50:
    points6 = 56
    score6 = 'H5'
elif result6 >= 40:
    points6 = 45
    score6 = 'H6'
elif result6 >= 30:
    points6 = 37
    score6 = 'H7'
else:
    points6 = 0
    score6 = 'H8'
print('You recieved a',score6,'in',subject6)
totalresults = [points,points2,points3,points4,points5,points6,points7]
totalresults.sort(reverse=True)
totalpoints = totalresults[0] + totalresults[1] + totalresults[2] + totalresults[3] + totalresults[4] + totalresults[5]
print('\nYour total points for the Leaving certificate are',totalpoints)