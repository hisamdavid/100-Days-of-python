class QuizBrain:

  def __init__(self,question_list):
    self.question_number=0
    self.question_list=question_list
    self.score=0

  def still_has_question(self):
    return self.question_number < len(self.question_list)

  def check_asnwer(self, user_asnwer, correct_answer):
    if user_asnwer.lower() == correct_answer.lower() :
      print("you got it right")
      self.score += 1
    else:
      print("you got it wrong")
    print(f"the correct answer was: {correct_answer}")
    print(f"your current score is: {self.score}/{self.question_number}")
    print("\n")

  def next_question(self):
    current_question=self.question_list[self.question_number]
    self.question_number += 1
    user_asnwer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_asnwer(user_asnwer,current_question.answer)
