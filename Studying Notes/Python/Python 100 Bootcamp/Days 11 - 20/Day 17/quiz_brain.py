class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0 # because all games start with the question number of zero
        self.question_list = question_list
        self.score = 0
    
    def has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_valid(self,answer,question):
        if answer.lower() in ['y','yes','true','t']:
            answer = 'True'
        elif answer.lower() in ['n','no','f','false']:
            answer = 'False'
        else:
            print("Not a valid response")
            answer = self.check_valid(input("Q.{}: {}".format(self.question_number,question)),question)
        return answer
    
    def check_answer(self,question,answer,q_question):
        if self.check_valid(answer,q_question) == question:
            self.score += 1
            print("Corrent!")
            
        else:
            print("Incorrect!")
        print("The answer was {}".format(question))
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # This increments the question number while also printing the correct number in the next statement
        answer = input("Q.{}: {}\n".format(self.question_number,current_question.text))
        self.check_answer(current_question.answer,answer,current_question.text)
        print("Your current score is: {} / {}\n".format(self.score,self.question_number))
        