from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz with a score of {quiz.score}/{quiz.question_number}!")
