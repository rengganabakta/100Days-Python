class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.question_list = q_list
        self.point = 0
        
    def still_has_question(self):
        return self.number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.number]
        self.number += 1
        user_input = input(f"Q{self.number}. {current_question.text} (True or False) : ")
        
        if current_question.ans == user_input:
            self.point += 1