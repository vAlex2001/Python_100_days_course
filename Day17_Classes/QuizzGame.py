from Data import question_data
from QuizzBrain import QuizzBrain

class Question:
    
    # Constructor for initializaing the question with the question and the respective answer
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        

def ___main__():
    
    question_bank = []
    
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
        
    quiz = QuizzBrain(question_bank)
    
    while quiz.still_has_questions():
        quiz.next_question()
    
    print("You've completed the quiz!")
    print(F"Your final score was: {quiz.score}/{quiz.question_number}")
    
___main__()
    