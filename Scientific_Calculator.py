from tkinter import * #conda install -c anaconda tk
import math

#This programe is created by Sujit Mandal

class Scientific_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # create screen widget
        self.screen = Text(master, state='normal', width=30, height=3,background="white", foreground="black")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=5,padx=5,pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons using method createButton
        b1 =  self.createButton(1)
        b2 = self.createButton(2)
        b3 = self.createButton(3)
        b4 = self.createButton('+')
        b5 = self.createButton(u"\u232B",None,8)
        b6 = self.createButton(4)
        b7 = self.createButton(5)
        b8 = self.createButton(6)
        b9 = self.createButton('-')
        b10 = self.createButton("(",8)
        b11 = self.createButton(7)
        b12 = self.createButton(8)
        b13 = self.createButton(9)
        b14 = self.createButton('*')
        b15 = self.createButton(")",8)
        b16 = self.createButton('.')
        b17 = self.createButton(0)
        b18 = self.createButton('**')
        b19 = self.createButton(u"\u00F7")
        b20 = self.createButton('math.sqrt',8)
        b21 = self.createButton('math.sin',8)
        b22 = self.createButton('math.cos',10)
        b23 = self.createButton('math.tan',8)
        b24 = self.createButton('math.cot',8)
        b25 = self.createButton('math.sec',8)
        b26 = self.createButton('math.cosec',8)
        b27 = self.createButton('math.factorial',10)
        b28 = self.createButton('math.log2',8)
        b29 = self.createButton('math.log10',8)
        b30 = self.createButton('math.e',8)
        b31= self.createButton('=',None,48)

        # buttons stored in list
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31]

        count = 0
        # arrange buttons with grid manager
        for row in range(1,7):
            for column in range(5):
                buttons[count].grid(row=row,column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[30].grid(row=7,column=0,columnspan=5)

    def createButton(self,val,write=True,width=7):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button

        return Button(self.master, text=val,command = lambda: self.click(val,write), width=width)   

    def click(self,text,value):
       
        if value == None:
            if text == '=' and self.equation: 
                self.equation= re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == u"\u232B":
                self.clear_screen()
             
        else:
            # add text to screen
            self.insert_screen(text)
    
    def clear_screen(self):
        #to clear screen
        #set equation to empty before deleting screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        # record every value inserted in screen
        self.equation += str(value)
        self.screen.configure(state ='normal')

root = Tk()
my_gui = Scientific_Calculator(root)
root.mainloop()
