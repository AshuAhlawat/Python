from tkinter import *
from tkinter import messagebox as mb

class Quiz:
    def __init__(self):
        self.q_no=0
         
        # assigns ques to the display_question
        self.display_title()
        self.display_question()
         
        # opt_selected holds an integer
        self.opt_selected=IntVar()
         
        # displaying radio button 
        self.opts=self.radio_buttons()
         
        # display options 
        self.display_options()
         
        # displays the button 
        self.buttons()
         
        # no of questions
        self.data_size=len(question)
         
        # keep a counter
        self.correct=0
 
#--------------------------------------------------------------#
    # display the result
    def display_result(self):
         
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        # calcultaes the percentage 
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
        # display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
#--------------------------------------------------------------#
    def check_ans(self, q_no):
         
        # if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            return True
 
#------------------------------------------------------------#
    def next_btn(self):
         
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
         
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
 
 
    # This method shows the two buttons on the screen.
#------------------------------------------------------------#
    def buttons(self):
         
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
         
        # palcing the button  on the screen
        next_button.place(x=350,y=380)
         
        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
         
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)
 

#-----------------------------------------------------------#
    # This method deselect buttons
    def display_options(self):
        val=0
         
        # deselecting the options
        self.opt_selected.set(0)
         
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
#---------------------------------------------------------#
    # This method shows the current Question on the screen
    def display_question(self):
         
        # setting the Question properties
        q_no = Label(gui, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
         
        #placing the option on the screen
        q_no.place(x=70, y=100)
 
#------------------------------------------------------#
    # This method is used to Display Title
    def display_title(self):
         
        # The title to be shown
        title = Label(gui, text="QUIZ",
        width=50, bg="grey",fg="white", font=("ariel", 20, "bold"))
         
        # place of the title
        title.place(x=0, y=2)
 
#-------------------------------------------------------#
    # This method shows the radio buttons
    def radio_buttons(self):
         
        # initialize the list with an empty list of options
        q_list = []
         
        # position of the first option
        y_pos = 150
         
        # adding the options to the list
        while len(q_list) < 4:
             
            # setting the radio button properties
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
             
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
             
            # incrementing the y-axis position by 40
            y_pos += 40
         
        # return the radio buttons
        return q_list
 
#=====================================================#
if __name__=="__main__":
    gui = Tk()
 

    gui.geometry("800x450")
    

    gui.title("QUIZ")
    

    data = {
        "question": [
            "Q1. What Indian city is the capital of two states?",
            "Q2. Which city is the capital of India?",
            "Q3. Smallest State of India?",
            "Q4. Where is Taj Mahal Located?"
        ],
        "answer": [
            1,
            2,
            3,
            2
        ],
        "options": [

            ["Chandigarh",
            "Kolkata",
            "Delhi",
            "Banglore"
            ],
            ["Jaipur",
            "Delhi",
            "Chennai",
            "Mumbai"
            ],
            ["Rajasthan",
            "Punjab",
            "Goa",
            "Bihar"
            ],
            ["Lucknow",
            "Agra",
            "Bhopal",
            "Delhi"
            ]
        ]
    }
        

    question = (data['question'])
    options = (data['options'])
    answer = (data[ 'answer'])
    

    quiz = Quiz()
    

    gui.mainloop()