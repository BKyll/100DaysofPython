# TODO: Asking the questions
# TODO: Check if the answer is correct
# TODO: Check if we're at the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            self.score += 1
            print("Correct")
        else:
            print("Incorrect")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
