# CTI-110

# P4HW1 - Score List

# Tory Horton

# 4-26-23



# makes a list based on users scores
total_scores = int(input("How many scores do you want to enter? ")) # asks user to input the amount of scores they want

print()

score_input_listed = [] # makes a list based on users scores

score_input = 0

while(True):

    while score_input < total_scores:
        
        score = float(input('Enter score #: '))

        while(True):
            
            if score < 0 or score > 100: # score has to be between 0 and 100
                print()
                print('INVALID Score entered!!!!')
                print('Score should be between 0 and 100')
                score = float(input('Enter score # again: ')) # asks user to input valid score

            else:
                score_input_listed.append(score)
                break

        score_input += 1
        
    if(score_input == total_scores):
        break
print()

print()

print('--------------Results-----------')

print(f'Lowest Score  : {min(score_input_listed)}') # finds the min

score_input_listed.remove(min(score_input_listed)) # drops users lowest score

print('Modified List :', score_input_listed) # shows list without lowest score

scores_average = sum(score_input_listed)

total_average = scores_average / (total_scores - 1) # finds the average

print(f'{"Scores Average: "}{total_average:.2f}')

# determines letter grade

if total_average >= 90:
    grade = 'A'
elif total_average >= 80:
    grade = 'B'
elif total_average >= 70:
    grade = 'C'
elif total_average >= 60:
    grade = 'D'
else:
    grade = 'F'

print('Grade         :', grade) # shows the letter grade

print('----------------------------------')
