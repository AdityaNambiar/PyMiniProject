from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

calculator = Tk()
calculator.title("CALCULATOR")

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    def calculateExpression(self): #python's calculate function 
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/ 100")

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)

    def clearText(self): #clears imput on pressing C on Calculator
        self.replaceText("0")

    def fileOps(self): #Will handle the file import feature and directly make a call to calculate function passing on the expression from the text file to eval() function.
        self.filedir = filedialog.askopenfilename(initialdir = "C:\\Program Files (x86)\\Python36-32\\Aditya_SEITA65\\PythonMiniproject - ScientificCalc\\",title = "Select a file\
                            with arithmetic operations")
        # Fetches Arithmetic strings from a text file in the location. Displays answer in a new window.  
        mul_calc = Toplevel(calculator)
        mul_calc.title("Multiple calculations result")
        mul_calc.resizable(1,1)
        with open(self.filedir,'r') as f:
            listbx = Listbox(mul_calc)
            listbx2 = Listbox(mul_calc)
            for ind, line in enumerate(f):
                listbx.insert(ind,line)
                listbx.grid(row=0,column=0)
                listbx2.insert(ind,eval(line))
                listbx2.grid(row=0,column=1)

    def mul_table(self): #Displays multiplication table of a number
        self.no = int(self.display.get())
        mul_t_gui = Toplevel(calculator)
        mul_t_gui.title("Multiplication table of {}".format(self.no))
        mul_t_gui.resizable(1,1)

        ans = 1
        multip_table = Listbox(mul_t_gui)
        for i in range(1,11):
            ans = self.no * i 
            multip_table.insert(i,"{} * {} = {}".format(self.no,i,ans))
            multip_table.grid(row=0,column=0) 
    
    def delText(self):
        length = len(self.display.get())
        return self.display.delete(length-1)

    def M_Conv(self):
        mconv = Toplevel(calculator)
        mconv.title("Metric Conversions")
        mconv.resizable(1,1)
        
        var1 = StringVar()
        mLabel = Label(mconv, textvariable = var1, relief = RAISED)
        var1.set("Number [Default: in  Meters]")
        mLabel.grid(row=0,column=0)

        var2 = StringVar()
        mLabel = Label(mconv, textvariable = var2, relief = RAISED)
        var2.set("Conversions")
        mLabel.grid(row=0,column=1)

        m0_lsbx = Listbox(mconv)
        self.no = int(self.display.get())
        m0_lsbx.insert(0,"{} meters".format(self.no))
        m0_lsbx.grid(row=1,column=0)

        m_lsbx = Listbox(mconv)
        m_lsbx.insert(0,"{0:.4f} foot".format(eval("self.no*3.28084")))
        m_lsbx.insert(1,"{0:.4f} inches".format(eval("self.no*39.37")))
        m_lsbx.insert(2,"{0:.4f} yard".format(eval("self.no*1.093")))
        m_lsbx.insert(3,"{0:.4f} mile".format(eval("self.no*0.000621371")))
        m_lsbx.insert(4,"{0:.4f} centimeters".format(eval("self.no*100")))

        m_lsbx.grid(row=1,column=1)

    def C_Conv(self):
        cconv = Toplevel(calculator)
        cconv.title("Currency Conversions")
        cconv.resizable(1,1)

        var1 = StringVar()
        mLabel = Label(cconv, textvariable = var1, relief = RAISED)
        var1.set("Number [Default: in INR]")
        mLabel.grid(row=0,column=0)

        var2 = StringVar()
        mLabel = Label(cconv, textvariable = var2, relief = RAISED)
        var2.set("Conversions")
        mLabel.grid(row=0,column=1)
        
        c0_lsbx = Listbox(cconv)
        self.no = int(self.display.get())
        c0_lsbx.insert(0,"{} INR".format(self.no))
        c0_lsbx.grid(row=1,column=0)

        c_lsbx = Listbox(cconv)
        c_lsbx.insert(0,"{0:.4f} USD".format(eval("self.no/65")))
        c_lsbx.insert(1,"{0:.4f} AUD".format(eval("self.no/50")))
        c_lsbx.insert(2,"{0:.4f} GBP".format(eval("self.no/92")))
        c_lsbx.insert(3,"{0:.4f} CAD".format(eval("self.no/51")))
        c_lsbx.insert(4,"{0:.4f} EUR".format(eval("self.no/80")))
        c_lsbx.insert(5,"{0:.4f} JPY".format(eval("self.no/0.61")))
        c_lsbx.insert(6,"{0:.4f} BHD".format(eval("self.no/173")))
        c_lsbx.insert(7,"{0:.4f} BDT".format(eval("self.no/0.79")))
        c_lsbx.insert(8,"{0:.4f} HKD".format(eval("self.no/8")))
        c_lsbx.insert(9,"{0:.4f} NZD".format(eval("self.no/48")))
        c_lsbx.grid(row=1,column=1)
                
    def createWidgets(self):

#Implementing a file menu for importing files:

        menubar = Menu(calculator)
        self.filemenu = Menu(menubar,tearoff=0)
        self.filemenu.add_command(label="Open File",command=lambda: self.fileOps())
        menubar.add_cascade(label="File",menu = self.filemenu)
        calculator.config(menu=menubar)
#Main Frame:
        self.display = Entry(self, font=("Helvetica", 16), borderwidth=0, relief=RAISED, justify=RIGHT)
        self.display.insert(0,"0")
        self.display.grid(row=2, column=0, columnspan=5)

#Importing images:
        self.cbrt = PhotoImage(file="PythonMiniproject - ScientificCalc\cbrt.png")
        self.multiples = PhotoImage(file="PythonMiniproject - ScientificCalc\multiple.png")
        self.bckarr = PhotoImage(file="PythonMiniproject - ScientificCalc\\bckarr.png") 
#This is Third row
        self.cbrtButton = Button(self,command=lambda: self.replaceText(eval("int(self.display.get()) ** (1/3)")))
        self.cbrtButton.config(image=self.cbrt, width='32',height='32',bd=1)
        self.cbrtButton.grid(row=3, column=0)
        
        self.multiplesButton = Button(self, command = lambda: self.mul_table())
        self.multiplesButton.config(image=self.multiples, width='32', height='32', bd=1)
        self.multiplesButton.grid(row=3, column=1)

        self.metricButton = Button(self, font=("Helvetica", 11), text="Met", borderwidth=0, command=lambda: self.M_Conv())
        self.metricButton.grid(row=3, column=2, sticky="NWNESWSE")

        self.currButton = Button(self, font=("Helvetica", 11), text="$", borderwidth=0, command=lambda: self.C_Conv())
        self.currButton.grid(row=3, column=3, sticky="NWNESWSE")

        self.bckarrButton = Button(self, command=lambda: self.delText())
        self.bckarrButton.config(image=self.bckarr, width='32', height='32', bd=1)
        self.bckarrButton.grid(row=3, column=4)
#This is the Fourth Row
        self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=0, command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=4, column=0, sticky="NWNESWSE")

        self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=0, command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=4, column=1, sticky="NWNESWSE")

        self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=0, command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=4, column=2, sticky="NWNESWSE")

        self.timesButton = Button(self, font=("Helvetica", 11), text="*", borderwidth=0, command=lambda: self.appendToDisplay("*"))
        self.timesButton.grid(row=4, column=3, sticky="NWNESWSE")

        self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=0, command=lambda: self.clearText())
        self.clearButton.grid(row=4, column=4, sticky="NWNESWSE")

#This is the Fifth Row
        self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=0, command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=5, column=0, sticky="NWNESWSE")

        self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=0, command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=5, column=1, sticky="NWNESWSE")

        self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=0, command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=5, column=2, sticky="NWNESWSE")

        self.divideButton = Button(self, font=("Helvetica", 11), text="/", borderwidth=0, command=lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=5, column=3, sticky="NWNESWSE")

        self.percentageButton = Button(self, font=("Helvetica", 11), text="%", borderwidth=0, command=lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=5, column=4, sticky="NWNESWSE")

#This is the Sixth Row
        self.oneButton = Button(self, font=("Helvetica", 11), text="1", borderwidth=0, command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=6, column=0, sticky="NWNESWSE")

        self.twoButton = Button(self, font=("Helvetica", 11), text="2", borderwidth=0, command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=6, column=1, sticky="NWNESWSE")

        self.threeButton = Button(self, font=("Helvetica", 11), text="3", borderwidth=0, command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=6, column=2, sticky="NWNESWSE")

        self.minusButton = Button(self, font=("Helvetica", 11), text="-", borderwidth=0, command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=6, column=3, sticky="NWNESWSE")

        self.equalsButton = Button(self, font=("Helvetica", 11), text="=", borderwidth=0, command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=6, column=4, sticky="NWNESWSE", rowspan=2)

#This is the Seventh Row
        self.zeroButton = Button(self, font=("Helvetica", 11), text="0", borderwidth=0, command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=7, column=0, columnspan=2, sticky="NWNESWSE")

        self.dotButton = Button(self, font=("Helvetica", 11), text=".", borderwidth=0, command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=7, column=2, sticky="NWNESWSE")

        self.plusButton = Button(self, font=("Helvetica", 11), text="+", borderwidth=0, command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=7, column=3, sticky="NWNESWSE")


app = Application(calculator).grid()        
calculator.mainloop()




