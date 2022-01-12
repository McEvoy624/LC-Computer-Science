start_score = int(input('Starting Score (301/501) : '))
entry = 0  
score = start_score - entry

while score > 1 :
    entry = int(input('Scored : '))
    if entry > 180 :
        print('Invalid score')
        entry = int(input('Scored : '))
    
    score = score - entry
    if score < 1 :
        print('Game over')
        break
    else:
        print('Score remaining :',score)
