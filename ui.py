from tkinter import *
from quiz_brain import QuizBrain
from PIL.ImageTk import PhotoImage


THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')
false_image = 'images/false.png'
true_image = 'images/true.png'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_tracker = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_tracker.grid(row=0, column=1)
        self.true_button = Button(text='True', highlightthickness=0, activebackground=THEME_COLOR,
                                  bg=THEME_COLOR,
                                  borderwidth=0, command=self.check_true)
        # self.true_button = Button(image=PhotoImage(file=true_image), highlightthickness=0, activebackground=THEME_COLOR,
        #                           borderwidth=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)
        # self.false_button = Button(image=PhotoImage(file=false_image),
        #                            highlightthickness=0, borderwidth=0, command=self.check_false)
        self.false_button = Button(text='False',
                                   highlightcolor=THEME_COLOR, borderwidth=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def check_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_tracker.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.get_next_question)



