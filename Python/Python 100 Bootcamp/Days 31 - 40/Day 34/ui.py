import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = tk.Label(text=f"Score: {self.quiz.score}")
        self.score_text.grid(row=0,column=1)        

        self.question_text = 'Placeholder Text'
        self.canvas = tk.Canvas(bg="white",width=300,height=250,highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, text=self.question_text,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.check_image = tk.PhotoImage(file="images/true.png")
        self.cross_image = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(image=self.check_image, command=self.select_true,highlightthickness=0)
        self.false_button = tk.Button(image=self.cross_image, command=self.select_false,highlightthickness=0)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    
    def select_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def select_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000,self.get_next_question)