import tkinter as tk
import random

FUNNY_COLOR_MAIN = '#df00ff' #pinkish
FUNNY_COLOR_SECONDARY="#ffdf00" #gay yellow
FUNNY_COLOR_THIRD="#00ffdf" #takova
FUNNY_COLOR_FOUR="#00ff5f"
FUNNY_COLOR_FIVE="#5f00ff"

WORST_POSSIBLE_FONT =("Kalinga",16)
BIGGER_FONT=("Franklin Gothic Medium",40,"bold")
DIGIT_FONT=("Adobe Hebrew",24,"bold")
OPERATORS_FONT=("Adobe Hebrew",20,"bold")


class Calculator:
    #ebasi konstruktora 
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("GUI Calculator")

        self.fullExpression=""
        self.currentExpression=""
        self.mainFrame= self.CreateMainFrame()

        self.fLabel,self.label=self.CreateDisplayLabels()





        self.buttonFrame=self.CreateButtonFrame()
        

        self.buttonFrame.rowconfigure(0,weight=1)

        for x in range(1,5):
            self.buttonFrame.rowconfigure(x,weight=1)
            self.buttonFrame.columnconfigure(x,weight=1)

        self.digits={
            1: (1,1),4: (1,2),9: (1,3), #dictionary with coordinates
            8: (2,1),2: (2,2),5: (2,3),
            7: (3,1),6: (3,2),3: (3,3),
            0: (4,2), '.':(4,1)
        }

        self.createDigitButtons()


        self.operations={"/": "\u00F7", '*':"\u00D7", '-':'-', "+": "+"} #the unique values that represent the x for multipl and strange symb for division
        self.CreateOperatorButtons()

        self.CreateSpecialButtons()






############################################33
         
    def CreateDisplayLabels(self):
        flabel=tk.Label(self.mainFrame, text=self.fullExpression, anchor=tk.E,bg=FUNNY_COLOR_MAIN,
                       fg=FUNNY_COLOR_THIRD,padx=24,font=WORST_POSSIBLE_FONT) #east basically
        flabel.pack(expand=True,fill="both")

        label=tk.Label(self.mainFrame, text=self.currentExpression, anchor=tk.E,bg=FUNNY_COLOR_MAIN,
                       fg=FUNNY_COLOR_SECONDARY,padx=24,font=BIGGER_FONT) #east basically
        label.pack(expand=True,fill="both")
        return flabel,label


       
    def CreateMainFrame(self):
        frame = tk.Frame(self.window,height=221,bg=FUNNY_COLOR_MAIN)
        frame.pack(expand=True,fill="both")
        return frame
    


    #buttons
    def createDigitButtons(self):
        for digit,grid_value in self.digits.items():
            i=random.randint(1,2)
            if i % 2 == 0 :
                button = tk.Button(self.buttonFrame, text=str(digit),bg=FUNNY_COLOR_FOUR,
                               fg=FUNNY_COLOR_FIVE,font=DIGIT_FONT,borderwidth=0, command=lambda x=digit : self.UpdateCurrentExpression(x))#mn qko
                button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
            else:
                button = tk.Button(self.buttonFrame, text=str(digit),bg=FUNNY_COLOR_FIVE,
                               fg=FUNNY_COLOR_FOUR,font=DIGIT_FONT,borderwidth=0,command=lambda x=digit: self.UpdateCurrentExpression(x))
                button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)           
             #mn qko reshenie za podrejdane north south east west
            #pochti pochva da mi se nravi python

    def CreateOperatorButtons(self):
        i=0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttonFrame, text=symbol,bg=FUNNY_COLOR_THIRD,fg=FUNNY_COLOR_SECONDARY,
                               font=OPERATORS_FONT,borderwidth=0,command=lambda x=operator:self.AppendOperator(x))#x e za da ne prenapisva stoinostta postoqnno
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1


    def Clear(self):
        self.currentExpression=""
        self.fullExpression=""

        self.UpdateCurrentLabel()
        self.UpdateFullLabel()

    def Evaluate(self):
        self.fullExpression += self.currentExpression
        self.UpdateFullLabel()
        try:
            self.currentExpression=str(eval(str(self.fullExpression)))
            self.fullExpression=""
        except Exception as e:
            self.currentExpression = "Error"
        finally:        
            self.UpdateCurrentLabel()

        

    def CreateEqualsButton(self):
        button = tk.Button(self.buttonFrame, text="=",bg=FUNNY_COLOR_MAIN,
                               fg=FUNNY_COLOR_SECONDARY,font=DIGIT_FONT,borderwidth=0, command=self.Evaluate)
        button.grid(row=4,column=3, columnspan=2, sticky=tk.NSEW)

    def CreateClearButton(self):
        button = tk.Button(self.buttonFrame, text="C",bg=FUNNY_COLOR_SECONDARY,
                               fg=FUNNY_COLOR_THIRD,font=DIGIT_FONT,borderwidth=0,command=self.Clear)
        button.grid(row=0,column=1, sticky=tk.NSEW)



    def Square(self):
        self.currentExpression= str(eval(f"{self.currentExpression}**2"))
        self.UpdateCurrentLabel()

    def CreateSquareButton(self):
        #unicode value of second power symbol
        button = tk.Button(self.buttonFrame, text="x\u00b2",bg=FUNNY_COLOR_SECONDARY,
                               fg=FUNNY_COLOR_THIRD,font=DIGIT_FONT,borderwidth=0,command=self.Square)
        button.grid(row=0,column=2, sticky=tk.NSEW)


    def Sqrt(self):
        self.currentExpression= str(eval(f"{self.currentExpression}**0.5"))
        self.UpdateCurrentLabel()
        
    def CreateSqrtButton(self):
        #unicode value of sqrt symbol
        button = tk.Button(self.buttonFrame, text="\u221ax",bg=FUNNY_COLOR_SECONDARY,
                               fg=FUNNY_COLOR_THIRD,font=DIGIT_FONT,borderwidth=0,command=self.Sqrt)
        button.grid(row=0,column=3, sticky=tk.NSEW)


    def CreateSpecialButtons(self):
        self.CreateEqualsButton()
        self.CreateClearButton()
        self.CreateSquareButton()
        self.CreateSqrtButton()


    def CreateButtonFrame(self):
        frame = tk.Frame(self.window,bg=FUNNY_COLOR_SECONDARY)
        frame.pack(expand=True,fill="both")
        return frame
    





    def UpdateFullLabel(self):
        expression = self.fullExpression
        #making sure the correct operattors are displayed in the top label
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator,f' {symbol} ')
        self.fLabel.config(text=self.fullExpression)

    def UpdateCurrentLabel(self):
        self.label.config(text=self.currentExpression[:10])#limiting lenght



    #in digit buttons
    def UpdateCurrentExpression(self,value):
        self.currentExpression+=str(value)
        self.UpdateCurrentLabel()


    ####in  operator buttons
    def AppendOperator(self,operator):
        self.currentExpression+=operator
        self.fullExpression+=self.currentExpression
        self.currentExpression=""

        self.UpdateFullLabel()
        self.UpdateCurrentLabel()
    
    def run(self):
        self.window.mainloop()

calc = Calculator()
calc.run()
        