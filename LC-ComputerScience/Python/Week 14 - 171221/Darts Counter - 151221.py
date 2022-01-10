# Making a darts score counter where it asks for your score as long as it is greater than 0
print('Darts score counter ''\nEnter in your scores and the computer will tell you your remaining score.')
starting_score = int(input('What is the starting score >> '))
points_scored = 0
score = starting_score - points_scored

while score > 0:
    points_scored = int(input('What did you score >> '))
    if points_scored > 180:
        points_scored = int(input('What did you score (Must be =< 180) >> '))
        score = starting_score - points_scored
        starting_score = score
        print('score remaining : ', score)       
        continue
    
    score = starting_score - points_scored
    starting_score = score
    print('score remaining : ', score)        
    
    if score == 0:
        print('The game is over!')
        