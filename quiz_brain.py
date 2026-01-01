from question_model import Question

class QuizBrain:
    def __init__(self, QuestionsList):
        self.QuestionNumber = 0
        self.QuestionsList = QuestionsList
    
    def next_question(self):
        current_question = self.QuestionsList[self.QuestionNumber]
        self.QuestionNumber += 1
        user_answer  = input(f"Q.{self.QuestionNumber}: {current_question.Text} (True/False):\n")
        return user_answer, current_question.Answer

    
    def still_has_questions(self):
        return self.QuestionNumber < len(self.QuestionsList)