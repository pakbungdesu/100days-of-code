
from quiz import *
from question import *
from pic import *


print(logo)

quiz_bank = []
for question in question_data:
  quiz_bank.append(Quiz(question))

user = QuizBrain(quiz_bank)
while user.question_left():
  user.current_question()

