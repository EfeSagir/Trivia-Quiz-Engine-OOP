import html
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    for question in data["results"]:
        question_text = html.unescape(question["question"]) 
        question_answer = question["correct_answer"]
        
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

quiz = QuizBrain(question_bank)
score = 0

while quiz.still_has_questions():
    user_answer, correct_answer = quiz.next_question()
    
    if user_answer.lower() == correct_answer.lower():
        score += 1
        print(f"Correct! Your current score is: {score}/{quiz.QuestionNumber}")
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")
    print("\n")

print(f"Quiz completed! Your final score is: {score}/{len(question_bank)}")