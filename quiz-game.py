question = {'question': 'This is the question',
            'answers': {'A': 'this is an answer',
                        'B': 'this is another answer',
                        'C': 'yes, this is another answer',
                        'D': 'You will not believe it, this also is an answer'},
            'correct_answer': 'A'
            }
question2 = {'question': 'This is the question',
             'answers': {'A': 'this is an answer',
                         'B': 'this is another answer',
                         'C': 'yes, this is another answer',
                         'D': 'You will not believe it, this also is an answer'},
             'correct_answer': 'A'
             }
Questions = [question, question2]
score = 1


# def doing_question(question):


def answer_checking(right_answer, user_answer):
    global score
    if user_answer == right_answer:
        score += 1


print('Hello, welcome to this quiz game, you will pass through several questions and your score will be saved (soon)')
user = input('introduce your name \n')
print(question['question'])
# I will make a function that put the answers in a beautiful display
print([(k, question['answers'][k] + '\n') for k in question['answers']])
your_answer = input('which one is correct?')
answer_checking(question['correct_answer'], your_answer)
print(score)
print(user)
print(Questions)
