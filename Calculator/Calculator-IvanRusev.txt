class Calculator:
    ###method needs 'self' as a parameter, since it is a class method and not a function.
    
    @staticmethod
    def Init():
           print("Welcome to Calculator!")  
           Calculator.SelectOperation()        
                    
    @staticmethod
    def SelectOperation():
        c=Calculator()
        while True:
          m = input("\nSelect operation : ( + , - , * , / , % , pow , root ) ['exit' to stop]:\n")
          if m=="exit":
            break
          elif m =='+':
            print(c.Add())
          elif m=="-":
            print(c.Sub())
          elif m=="*":
            print(c.Mul())
          elif m=="/":
            print(c.Div())
          elif m=="%":
            print(c.Mod())
          elif m=="pow":
            print(c.Pow())
          elif m=="root":
            print(c.Root())
          else :
            print("\nBad entry. Try again!")
        print("\nOperations finished. Calculator closed.")
        

    @staticmethod
    def CheckValues(x, y):
        if x.lstrip("+-.,").replace('.','').isdecimal() and y.lstrip("+-.,").replace('.','').isdecimal() : 
            #striping the input string from all operands to ensure that it can correctly check if a number 
            return True
        print("Incorrect values! Try again")
        return False
    
    @staticmethod
    def EnterValues(name1,name2):
         
         while(True):
           a=input(f"Enter {name1} value: ")
           b=input(f"Enter {name2} value: ")
           if Calculator.CheckValues(a,b) :
               if '.' in a or '.' in b:
                a=float(a)
                b=float(b)
                break
               else:
                  a=int(a)
                  b=int(b)
                  break
         return a,b
    @staticmethod
    def CheckFloat(a,b):
       if '.' in str(a) or '.' in str(b):
           return True
       else:
          return False
      
       
    def Add(self):
        print("Add function selected.\n")
        
        a,b=Calculator.EnterValues("first add","second add")
        print("Result: ")
        if Calculator.CheckFloat(a,b):
           return str(round(a+b,3))
        else:
           return a+b


    def Sub(self):
        print("Subtract function selected.\n")
        
        a,b=Calculator.EnterValues("first subtract","second subtract")
        
        print("Result: ")
        if Calculator.CheckFloat(a,b):
           return str(round(a-b,3))
        else:
           return a-b

    def Mul(self):
        print("Multiply function selected.\n")

        a,b=Calculator.EnterValues("first multiply","second multiply")

        print("Result: ")
        if Calculator.CheckFloat(a,b):
           return str(round(a*b,3))
        else:
           return a*b


    def Div(self):
        print("Divide function selected.\n")

        a,b=Calculator.EnterValues("first division","second division")
        if b==0:
           return "Cannot divide by zero!"
        print("Result: ")
        if Calculator.CheckFloat(a,b):
           return str(round(a/b,3))
        else:
           return a/b



    def Mod(self):
        print("Modulo function selected.\n")

        a,b=Calculator.EnterValues("first modulo","second modulo")

        print("Result: ")
        if Calculator.CheckFloat(a,b):
           print("Values must be whole numbers!")
           return 0
        else:
           return a%b

    def Pow(self):
        print("Power function selected.\n")
        a,b=Calculator.EnterValues("number","power")

        print("Result: ")
        if Calculator.CheckFloat(a,b):
           return str(round(pow(a,b),3))
        else:
           return pow(a,b)

    def Root(self):
        print("Root function selected.\n")
        a,b=Calculator.EnterValues("number","root type(quadratic,cube...)")

        print("Result: ")
        if Calculator.CheckFloat(a,b):
           return "Second value must be a whole number!"
        else:
           return round(pow(a,1/b),3)


Calculator.Init()