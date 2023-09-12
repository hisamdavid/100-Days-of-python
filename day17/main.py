from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for q_data in question_data:
  question_bank.append(Question(q_data["question"],q_data["correct_answer"]))

quiz= QuizBrain(question_bank)
while quiz.still_has_question():
  quiz.next_question()

print(f"you've complited the quiz\nyour final score was: {quiz.score}/{quiz.question_number}")