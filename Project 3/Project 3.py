# Although you are given this small example, your code should be able to input a size n matrix
# of weights and values and a knapsack size (read in a file). Here are the steps to complete
# the project:
#
# Step 1. Code an exhaustive search algorithm to find the optimal solution to the above
# problem.
from itertools import combinations
from tkinter import *
import ast

with open('input.txt', 'r') as f:
    # read = f.readlines(1)
    # capacity = read
    # weight = f.readlines(2)
    x = f.read().splitlines()
    capacity = ast.literal_eval(x[0])
    weight = ast.literal_eval(x[1])
    value = ast.literal_eval(x[2])
    ranges = [x for x in range(len(weight)+1)]

    inputSample = tuple(zip(ranges[1:], weight, value))
    print(inputSample)

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
          '\n  #'.join(sorted(str(Item) for Item, _, _ in result)))
    val, wt = totalvalue(result)
    print("for a maximum of %i and a total weight of %i" % (val, -wt))

exhaustive(inputSample, capacity)

# Step 2. Code a DP method to find the optimal solution to the problem.

# Step 3. Code your chosen method to find the optimal solution to the problem.

# Step 4. Be sure to create a user friendly menu (no crashing and easy exit, read knapsack
# data from a file).


class KnapsackUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="SkyBlue")
        self.DialogText = None
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
        t = Toplevel()
        t.title("Knapsack: Exhaustive Algorithm")
        t.resizable(0,0)
        t.config(bg="DarkSlateGrey")

        t.Image = Label(t, image=ex, bg="DarkSlateGrey")
        t.Image.pack(side="top")
        t.Title = Label(t, text="Exhaustive", fg="MediumSpringGreen", bg="DarkSlateGrey")
        self.Title(t.Title)

        t.exit = Button(t, text="CLOSE", fg="GhostWhite", bg="Crimson", activebackground="GhostWhite", activeforeground="Crimson", command=t.destroy)
        self.expandBottom(t.exit)
        t.enter = Button(t, text="START", fg="DarkSlateGrey", bg="Gold", activebackground="DarkSlateGrey", activeforeground="Gold")
        self.expandBottom(t.enter)
        t.load = Button(t, text="LOAD FILE", fg="DarkSlateGrey", bg="MediumSpringGreen", activebackground="DarkSlateGrey", activeforeground="MediumSpringGreen")
        self.expandBottom(t.load)

        self.OneAtATime(t)

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


root = Tk()
root.title("The Knapsack")
sackimage = PhotoImage(file="knapsack1.png")
ex = PhotoImage(file="fire.png")
root.resizable(0, 0)


app = KnapsackUI(master=root)
app.mainloop()
