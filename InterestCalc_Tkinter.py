#importing GUI module
from tkinter import *

# Frame is the superclass of Application
class Application(Frame):
  
  def __init__(self, master):
        # Inheriting all of Frame's attributes
        # Super refers to the superclass(Frame)

      super(Application, self).__init__(master)
      # .grid() is a tkinter method -- it refers to the layout manager
      self.grid()
      self.createWidgets()

  def compound(self):
    #clears Label to 'replace' value of compound and simple interest on the screen
    display = Label(root, text = "")
    display.grid(row = 7, column=0,sticky = N, pady=(30,0), padx=(40,0))   

    #Gets values from entry fields
    p = float(self.e1.get())
    i = float(self.e2.get())/100
    y = float(self.e3.get())
    n = float(self.e4.get())

    #Calculates compound interest
    c = p*(1+i/n)**(n*y)

    #Displays and formats on screen
    display = Label(root, text = f"Compounding: ${c:.2f}",font=("Courier", 10, "bold"), fg="#2E5984", width=30)
  
    display.grid(row = 7, column=0,sticky = N, pady=(30,0), padx=(40,0))   

    
  def simp_int(self):
    #clears Label to 'replace' value of compound and simple interest on the screen
    
    display = Label(root, text = "",  width=30)
  
    display.grid(row = 7, column=0,sticky = N, pady=(30,0), padx=(40,0))   

    #Gets values from entry fields
    p = float(self.e1.get())
    i = float(self.e2.get())/100
    y = float(self.e3.get())
    n = float(self.e4.get())

    #Calculates simple interest
    simple = p*(1+(i*y))

    #Displays and formats on screen
    display = Label(root, text = f"Simple: ${simple:.2f}",font=("Courier", 10, "bold"), fg="#2E5984")
    display.grid(row = 7, column=0,sticky = N, pady=(30,0), padx=(5,0))  


  def createWidgets(self):
    #Creating Title label
    self.header = Label(root, text = "Interest Calculator", fg="#2E5984", font=("Courier", 14, "bold"))
    self.header.grid(row=0, column=0, columnspan=5, sticky=N, pady =(15,25))

    #Creating label for principal, interest, years, and compounding per year
    principal = Label(root, text = "Principal:", font=("Times", 10))
    interest = Label(root, text = "Annual Interest:", font=("Times", 10))
    year = Label(root, text = "Years:", font=("Times", 10))
    compounding = Label(root, text = "# Compounding per Year:", font=("Times", 10))

    principal.grid(row = 1, column = 0, sticky = W, pady=(10, 0), padx = 10)
    interest.grid(row = 2, column = 0, sticky = W, pady=(10, 0), padx = 10)
    year.grid(row = 3, column = 0, sticky = W, pady=(10, 0), padx = 10)
    compounding.grid(row = 4, column = 0, sticky = W, pady=(10, 0), padx = 10)

    #Creating entry fields
    self.e1 = Entry(root, width=20)
    self.e2 = Entry(root, width=20)
    self.e3 = Entry(root, width=20)
    self.e4 = Entry(root, width=20)

     
    self.e1.grid(row = 1, column = 2)
    self.e2.grid(row = 2, column = 2)
    self.e3.grid(row = 3, column = 2)
    self.e4.grid(row = 4, column = 2)

    
    #Creating buttons
    comp_int = Button (root, text ="Compound Interest", bg="#528AAE", fg="white")
    comp_int.grid(row = 5, column = 0, pady=(30,0))
    comp_int["command"] = self.compound
    simp_int = Button (root, text ="Simple Interest", bg="#528AAE", fg="white")
    simp_int["command"] = self.simp_int
    simp_int.grid(row = 5, column = 1, pady=(30,0))


# Creating a Tkinter Object
root = Tk()
root.title("Interest Calculator")
# widthxlength
root.geometry("600x350")
# Creating an Application object
app = Application(root)

root.mainloop()
