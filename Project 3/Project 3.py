# Although you are given this small example, your code should be able to input a size n matrix
# of weights and values and a knapsack size (read in a file). Here are the steps to complete
# the project:
#
# Step 1. Code an exhaustive search algorithm to find the optimal solution to the above
# problem.
from itertools import combinations
from tkinter import *
import subprocess as sub

sample1 = ((1, 3, 25), (2, 2, 20), (3, 1, 15), (4, 4, 40), (5, 5, 50))


def exhaustive(item, capacity):
    def anycombination(Item):
        """ return combinations of any length from the items """
        return (comb
                for r in range(1, len(Item) + 1)
                for comb in combinations(Item, r)
                )

    def totalvalue(x):
        """ Sums up a combination of items """
        total_weight = total_value = 0
        for Item, Weight, Value in x:
            total_weight += Weight
            total_value += Value
        return (total_value, -total_weight) if total_weight <= capacity else (0, 0)

    result = max(anycombination(item), key=totalvalue)  # max val or min wt if values are equal to each other
    print("Found items:\n  #" +
          '\n  #'.join(sorted(str(x) for x, _, _ in result)))
    val, wt = totalvalue(result)
    print("for a maximum of %i and a total weight of %i" % (val, -wt))

# Step 2. Code a DP method to find the optimal solution to the problem.

# Step 3. Code your chosen method to find the optimal solution to the problem.

# Step 4. Be sure to create a user friendly menu (no crashing and easy exit, read knapsack
# data from a file).


class KnapsackUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="SkyBlue")
        self.child_window = None
        self.MainMenu()

    def MainMenu(self):

        self.knapimg = Label(self, image=sackimage, bg="SkyBlue")
        self.knapimg.pack(side="top")

        self.q = Button(self, text="EXIT", fg="GhostWhite", bg="Crimson", activebackground="GhostWhite", activeforeground="Crimson", command=root.destroy)
        self.h = Button(self, text="HELP", fg="DarkRed", bg="LightCoral", activebackground="DarkRed", activeforeground="LightCoral", command=self.tutorial)
        self.c = Button(self, text="RECURSION", fg="Sienna", bg="Wheat", activebackground="Sienna", activeforeground="Wheat")
        self.DP = Button(self, text="DYNAMIC PROGRAMMING", fg="DarkSlateGray", bg="LightGreen", activebackground="DarkSlateGray", activeforeground="LightGreen")
        self.ex = Button(self, text="EXHAUSTIVE", fg="DarkSlateGray", bg="MediumSpringGreen", activebackground="DarkSlateGray", activeforeground="MediumSpringGreen", command=self.Exhaustive)
        MainMenuButtons = [self.q, self.h, self.c, self.DP, self.ex]

        self.introTitle = Label(self, text="The Knapsack", fg="White", bg="SkyBlue")
        self.Title(self.introTitle)

        self.introText = Label(self, text="Which algorithm method would you like to try for this Knapsack problem?", fg="DarkSlateGrey", bg="SkyBlue")
        self.introText.config(font=("Georgia", 12))
        self.introText.pack(side="top", fill='y', expand=0)
        self.pack()
        for x in MainMenuButtons:
            self.expandBottom(x)

    def tutorial(self):
        # display text
        t = Toplevel(self)
        t.title("Knapsack: Tutorial")
        t.resizable(0, 0)

        t.Title = Label(t, text="Sorry!", fg="Maroon", bg="HoneyDew")
        self.Title(t.Title)

        t.Body1 = Label(t, text="Exhaustive Algorithm", fg="Brown", bg="PapayaWhip")
        self.Body(t.Body1)

        t.Body2 = Label(t, text="Dynamic Programming Algorithm", fg="Maroon", bg="Wheat")
        self.Body(t.Body2)

        t.Body3 = Label(t, text="Recursion Algorithm", fg="MistyRose", bg="LightSalmon")
        self.Body(t.Body3)

        t.Body4 = Label(t, text="Navigation", fg="MistyRose", bg="LightCoral")
        self.Body(t.Body4)

        t.exit = Button(t, text="THANKS", fg="GhostWhite", bg="Crimson", activebackground="GhostWhite", activeforeground="Crimson", command=t.destroy)
        self.expandBottom(t.exit)

        self.OneAtATime(t)


    def Exhaustive(self):
        self.t = Toplevel()
        sys.stdout = self.t
        self.t.title("Knapsack: Exhaustive Algorithm")
        self.t.resizable(0,0)
        self.t.config(bg="DarkSlateGrey")

        def Enter():
            print(eval(self.t.entry.get()))
            self.t.entry.delete(0, END)

        def write(txt):
            self.t.text.insert(END,str(txt))

        self.t.Image = Label(self.t, image=ex, bg="DarkSlateGrey")
        self.t.Image.pack(side="top")
        self.t.Title = Label(self.t, text="Exhaustive", fg="MediumSpringGreen", bg="DarkSlateGrey")
        self.Title(self.t.Title)

        self.t.exit = Button(self.t, text="CLOSE", fg="GhostWhite", bg="Crimson", activebackground="GhostWhite", activeforeground="Crimson", command=self.t.destroy)
        self.expandBottom(self.t.exit)
        self.t.enter = Button(self.t, text="START", fg="DarkSlateGrey", bg="Gold", activebackground="DarkSlateGrey", activeforeground="Gold", command=Enter)
        self.expandBottom(self.t.enter)
        self.t.load = Button(self.t, text="LOAD FILE", fg="DarkSlateGrey", bg="MediumSpringGreen", activebackground="DarkSlateGrey", activeforeground="MediumSpringGreen")
        self.expandBottom(self.t.load)

        self.t.entry = Entry(self.t, fg="DarkSlateGrey", bg="HoneyDew")
        self.t.entry.config(font=("Consolas", 10), bd=0, width=47)
        self.t.entry.pack(side="bottom", padx=0, pady=15)

        self.t.text = Text(self.t, fg="DarkSlateGrey", bg="HoneyDew")
        self.t.text.config(font=("Consolas", 10), bd=0, width=47, height=10)
        self.t.text.pack(side="bottom", padx=0, pady=0)

        self.OneAtATime(self.t)



    def normalButton(self, Button):
        self.x = Button
        self.x.config(font=("Helvetica", 16, "bold"), bd=0, width=16)
        self.x.pack(side="bottom", padx=0, pady=0)

    def expandBottom(self, Button):
        self.x = Button
        self.x.config(font=("Helvetica", 16, "bold"), bd=0)
        self.x.pack(side="bottom", fill='both', expand=1, padx=0, pady=0)

    def Title(self, Label):
        self.x = Label
        self.x.config(font=("Helvetica", 50, "bold"))
        self.x.pack(side="top", fill='both', padx=5)

    def Body(self, Label):
        self.x = Label
        self.x.config(font=("Georgia", 11))
        self.x.pack(side="top", fill='both', expand=0, anchor=W)

    def OneAtATime(self, t):
        t.transient(root)
        t.grab_set()
        root.wait_window(t)

    # def displayList(self, Item):
class Display(Frame):
    """"" Demonstrate python interpreter output in Tkinter Text widget
type python expression in the entry, hit DoIt and see the results
in the text pane."""

    def __init__(self,parent=0):
       Frame.__init__(self,parent)
       self.entry = Entry(self)
       self.entry.pack()
       self.doIt = Button(self,text="DoIt", command=self.onEnter)
       self.doIt.pack()
       self.output = Text(self)
       self.output.pack()
       sys.stdout = self
       self.pack()

    def onEnter(self, Entry):
        print(eval(Entry.get()))




root = Tk()
root.title("The Knapsack")
sackimage = PhotoImage(file="knapsack1.png")
ex = PhotoImage(file="fire.png")
root.resizable(0, 0)


app = KnapsackUI(master=root)
app.mainloop()
