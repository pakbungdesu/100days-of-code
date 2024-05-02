

class Quiz:
  def __init__(self, dictionary):
    self.text = dictionary["text"]
    self.answer = dictionary["answer"]

class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 1
    self.score = 0
    self.question_list = q_list

  def current_question(self):
    # question
    current_q = self.question_list[self.question_number]
    print(f"Q.{self.question_number} : {current_q.text} (True/False)")
    user_input = str(input("Your answer: ")).lower()
    self.check_ans(user_input, current_q.answer.lower()) # here is important

    # update number
    self.question_number += 1

  def check_ans(self, user_ans, correct_ans):
    if user_ans == correct_ans:
      self.score += 1
      print("Correct answer. Great job 🥊")
      if self.question_number == 11:
        print(f"Your final score {self.score}/{self.question_number}\nCongratulation ✨")
      else:
        print(f"Your current score {self.score}/{self.question_number}")
    else:
      print(f"Wrong! The correct answer is {correct_ans} 🔥")
      if self.question_number == 11:
        print(f"Your final score {self.score}/{self.question_number}\nCongratulation ✨")
      else:
        print(f"Your current score {self.score}/{self.question_number}")


  def question_left(self):
    return self.question_number < len(self.question_list)

