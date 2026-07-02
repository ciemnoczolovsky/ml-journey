#Excercise 7.6 - fototball quiz
wrong_answers = 0
player_score = 0
loop_iterations=1
allowed_answers = ['a','b','c','d']
questions = {
    1:{
        'question': (
            'Who is 2026 Champions League winner?'
            '\n\ta) Barcelona'
            '\n\tb) PSG'
            '\n\tc) Manchester City'
            '\n\td) Real Madrid'
            '\nYour answer: '
        ),
        'answer': 'b'
    },
    2:{
        'question': (
            'What is Leo Messi goals record in one calendar year?'
            '\n\ta) 13'
            '\n\tb) 47'
            '\n\tc) 92'
            '\n\td) 88'
            '\nYour answer: '
        ),
        'answer': 'c'
    },
    3:{
        'question':(
            'Who has the most trophies in polish Ekstraklasa?'
            '\n\ta) Legia Warsaw'
            '\n\tb) Lech Poznan'
            '\n\tc) Gornik Zabrze'
            '\n\td) Widzew Lodz'
            '\nYour answer: '
        ),
        'answer': 'a'
    },
    4:{
        'question':(
            'How much Tottenham paid for Sandro Tonali?'
            '\n\ta) 95M pounds'
            '\n\tb) 78M pounds'
            '\n\tc) He was free agent'
            '\n\td) 37M pounds'
            '\nYour answer: '
        ),
        'answer': 'a'
    },
    5:{
        'question':(
            'How many Balon d\'ors has Lionel Messi?'
            '\n\ta) 7'
            '\n\tb) 2'
            '\n\tc) 9'
            '\n\td) 8'
            '\nYour answer: '
        ),
        'answer': 'a'
    }
}

print('Welcome to the football quiz! To answer questions choose a,b,c or d!')
while True:
    if wrong_answers > 2:
        print(f"You have reached wrong answer limit!"
              f"Your final score is {player_score} points.")
        break
    elif loop_iterations > 5:
        print(f"No more questions for you. You have got {player_score} points"
              f" and {wrong_answers} wrong answers!")
        break

    answer = input(questions[loop_iterations]['question'])
    if answer.lower() not in allowed_answers:
        print("You have to write a, b, c or d!")
        continue
    elif answer.lower() == questions[loop_iterations]['answer']:
        player_score += 1
        print(f"Good job! You have {player_score} points and {wrong_answers}"
              " wrong answers!")
        loop_iterations += 1
    else:
        wrong_answers += 1
        print(f"Ooops! That's not correct. You have {player_score}"
              f" points and {wrong_answers} wrong answers!")
        loop_iterations += 1