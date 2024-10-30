from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)
    
Quiz = QuizBrain(question_bank)

    
while Quiz.still_has_question() == True:
    Quiz.next_question()
    
print(f"finish... you won {Quiz.point} point")