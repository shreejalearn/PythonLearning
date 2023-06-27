#importing GUI module
from tkinter import *

# Frame is the superclass of Application
class Application(Frame):
    # Gui application that creates a story based on user input
    def __init__(self, master):
        # initialize Frame
        # Inheriting all of Frame's attributes
        # Super refers to the superclass(Frame)

        super(Application, self).__init__(master)
      
        # .grid() is a tkinter method -- it refers to the layout manager
        self.grid()
        self.create_widgets()

    #Creates new window for story and deletes old window
    def write(self):
        #Stores user selected tools
        tools= []
        #Checks value of checkbuttons (0 (false) or 1 (true))
        if self.c_status.get()==1:
            tools.append('screws')
        if self.c2_status.get()==1:
            tools.append('hammers')
        if self.c3_status.get()==1:
            tools.append('wrenches')
        else:
            tools.append('drills')
        
        tool1=tools[0]
        tool2=tools[1]
      
        #F string storing all entry values  
        story = f"I was going to be rich!\n I had just invented the first electric {self.noun_entry.get()}.\n Using a(n) {self.noun2_entry.get()} from {self.name_entry.get()}’s toolbox, I built it out of old {tool1} and metal {tool2}.\n The first time I turned it on, the machine worked {self.adj_var.get()}.\n I couldn’t believe it! “{self.expression_entry.get()}” I yelled, running up and down.\n I invited a billionaire to check out my invention. I couldn’t wait to sell it for {self.num_entry.get()} million dollars and live like {self.celeb_entry.get()}.\n But when I turned it on, something went terribly wrong. The machine started spewing random bits of {self.noun_var.get()} and exploded.\n The billionaire started screaming at the top of his lungs and ran out of my lab. Good thing I still get my weekly allowance."

        #Creates new window for story
        root2 = Tk()
        root2.title("MadLibs Result")
        # widthxlength
        root2.geometry("1200x300")
        # Creating an Application object
        app2 = Application(root2)

        story_lbl = Label(root2, text=story, font=("Courier", 11), fg="#005555").grid(sticky=W, padx=(10,10), pady=(7,7))
        #Closes old window before showing the new one
        root.destroy()
        root2.mainloop()

      
    def create_widgets(self):
          # Create widgets to get story information and to display story
      
         # create instruction label
        Label(self, text = "Time for a new story", fg="#2E5984", font=("Courier", 14, "bold", "underline")).grid(row=0, column=0, columnspan=5, sticky=W, pady =(15,25), padx=(20,0))

        # create noun input
        noun_label = Label(root, text="Enter a noun:", font=("Courier", 11), fg="#005555")
        noun_label.grid(row=1, column=0, padx=(10,0), pady=(7,7))
        self.noun_entry = Entry(root, bg='#59C1BD', fg="white")
        self.noun_entry.grid(row=1, column=1, columnspan=2, padx=(10,0), pady=(7,7))

        # create noun input
        noun2_label = Label(root, text="Enter another noun:", font=("Courier", 11), fg="#005555")
        noun2_label.grid(row=2, column=0, padx=(10,0), pady=(7,7))
        self.noun2_entry = Entry(root, fg="#59C1BD")
        self.noun2_entry.grid(row=2, column=1, columnspan=2, padx=(10,0), pady=(7,7))

        # create name input
        name_label = Label(root, text="Enter a name:", font=("Courier", 11), fg="#005555")
        name_label.grid(row=3, column=0, padx=(10,0), pady=(7,7))
        self.name_entry = Entry(root, bg='#59C1BD', fg="white")
        self.name_entry.grid(row=3, column=1, columnspan=2, padx=(10,0), pady=(7,7))

        #create checkbox for tools
        name_label = Label(root, text="Pick 2 tools:", font=("Courier", 11), fg="#005555")
        name_label.grid(row=4, column=0, columnspan=1, padx=(10,0), pady=(7,7))

        #Stores value in separate variable
        self.c_status = IntVar()
        self.c2_status = IntVar()
        self.c3_status = IntVar()
        self.c4_status = IntVar()

        c = Checkbutton(root, text = "Screws", variable=self.c_status, onvalue=1, offvalue=0, activebackground="#ADD8E6")
        c.grid(row=4, column=1, columnspan=1, padx=(10,0), pady=(7,7))

        
        c2 = Checkbutton(root, text = "Hammers", variable=self.c2_status, onvalue=1, offvalue=0, activebackground="#ADD8E6")
        c2.grid(row=4, column=2, columnspan=1, padx=(10,0), pady=(7,7))
        
        
        c3 = Checkbutton(root, text = "Wrenches", variable=self.c3_status, onvalue=1, offvalue=0, activebackground="#ADD8E6")
        c3.grid(row=4, column=3, columnspan=1, padx=(10,0), pady=(7,7))
        
        
        c4 = Checkbutton(root, text = "Drills", variable=self.c4_status, onvalue=1, offvalue=0, activebackground="#ADD8E6")
        c4.grid(row=4, column=4, columnspan=1, padx=(10,0), pady=(7,7))
        

        #create radiobuttons for adjectives

        adjective = Label(root, text="Choose an adjective:", font=("Courier", 11), fg="#005555")
        adjective.grid(row=5, column=0, padx=(10,0), pady=(7,7))

        #Stores value in separate variable
        self.adj_var = StringVar()
      
        adj_amazing = Radiobutton(root, text="Amazingly", variable=self.adj_var, value="amazingly", activebackground="#ADD8E6")
        adj_amazing.grid(row=5, column=1, padx=(10,0), pady=(7,7))
      
        adj_splendid = Radiobutton(root, text="Splendidly", variable=self.adj_var, value="splendidly", activebackground="#ADD8E6")
        adj_splendid.grid(row=5, column=2, padx=(10,0), pady=(7,7))
      
        adj_perfect = Radiobutton(root, text="Perfectly", variable=self.adj_var, value="perfectly", activebackground="#ADD8E6")
        adj_perfect.grid(row=5, column=3, padx=(10,0), pady=(7,7))

      
        #Create a number input
        num_label = Label(root, text="Enter a large number:", font=("Courier", 11), fg="#005555")
        num_label.grid(row=6, column=0, padx=(10,0), pady=(7,7))
        self.num_entry = Entry(root, bg='#59C1BD', fg="white")
        self.num_entry.grid(row=6, column=1, columnspan=2, padx=(10,0), pady=(7,7))

      
        #Create a celeb input
        celeb_label = Label(root, text="Enter a celebrity:", font=("Courier", 11), fg="#005555")
        celeb_label.grid(row=7, column=0, padx=(10,0), pady=(7,7))
        self.celeb_entry = Entry(root, fg="#59C1BD")
        self.celeb_entry.grid(row=7, column=1, columnspan=2, padx=(10,0), pady=(7,7))

      
        #create radiobuttons for nouns
        noun = Label(root, text="Choose an noun:", font=("Courier", 11), fg="#005555")
        noun.grid(row=8, column=0, padx=(10,0), pady=(7,7))

        #Stores value in separate variable
        self.noun_var = StringVar()
      
        noun_slime = Radiobutton(root, text="Slime", variable=self.noun_var, value="slime", activebackground="#ADD8E6")
        noun_slime.grid(row=8, column=1, padx=(10,0), pady=(7,7))
      
        noun_rainbow = Radiobutton(root, text="Rainbows", variable=self.noun_var, value="rainbows", activebackground="#ADD8E6")
        noun_rainbow.grid(row=8, column=2, padx=(10,0), pady=(7,7))
      
        noun_hats = Radiobutton(root, text="Hats", variable=self.noun_var, value="hats", activebackground="#ADD8E6")
        noun_hats.grid(row=8, column=3, padx=(10,0), pady=(7,7))

      
        #Create a expression input
        expression_label = Label(root, text="Enter an expression:", font=("Courier", 11), fg="#005555")
        expression_label.grid(row=9, column=0, padx=(10,0), pady=(7,7))
      
        self.expression_entry = Entry(root, bg='#59C1BD', fg="white")
      
        self.expression_entry.grid(row=9, column=1, columnspan=2, padx=(10,0), pady=(7,7))


      
        #Creating a button
        story = Button(root, text ="See Story", bg="#528AAE", fg="white")
        story.grid(padx=(10,0), pady=(25,0))
        story["command"] = self.write

  

#Main root creation
    
root = Tk()
root.title("MadLibs Game")
# widthxlength
root.geometry("680x600")
# Creating an Application object
app = Application(root)

root.mainloop()
