from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, window):
        # always call parent instructor
        super().__init__(window)
        # we need to call grid on the frame
        self.grid()

        # BUTTON class: execute a specified function when pressed
        # self.btnOk = Button(self, text="Show Menu", fg="#990000", bg="#ffc72c", font="Arial 20 bold",
        #                activeforeground="#ffc72c", activebackground="#990000", command=self.showMenu())
        # self.btnOk.grid(row=1, column=1, rowspan =1, columnspan =1, sticky ="")
        #
        # self.btnShow = Button(self, text="Show", command=self.show)
        # self.btnShow.grid(row=1, column=0)

        # LABEL class: non-interactive piece of text Label(rootWindow, text="your text here")
        # self.lblName = Label(self, text="Info Window", fg="#0051BA", bg="#F9D616", font="Arial 20 bold")
        # self.lblName.grid()

        # ENTRY class: enter text
        # self.entName = Entry(self, font="Arial 20 bold", fg="blue")
        # self.entName.grid(row=2, column=1)

        # RADIOBUTTON
        # self.svYesNo = StringVar()
        # self.svYesNo.set("y")
        # self.radioYes = Radiobutton(self, text="Yes", value="y", variable=self.svYesNo)
        # self.radioNo = Radiobutton(self, text="No", value="n", variable=self.svYesNo)
        # self.radioYes.grid()
        # self.radioNo.grid()

        # CHECKBUTTON
        # self.bvCheck = BooleanVar()
        # self.checkTerms = Checkbutton(self, text="Accept?", variable=self.bvCheck)
        # self.checkTerms.grid()
        #
        # self.btnTest = Button(self, text="Test", command=self.test)
        # self.btnTest.grid(row=2, column=0)


        # SHOW MENU
        # Drink label
        dd = Label(self, text="Drink", fg="green").grid(row=1, column=11, sticky=W)

        # Drink item, each is a radio button to ensure one item per type
        self.d = StringVar()
        self.d.set("None")
        self.radioD1 = Radiobutton(self, text="Soda -- $1.5 -- Choose from sprite coke or pepsi", variable=self.d,
                    value="Soda", fg="black")
        self.radioD1.grid(row=2, column=11, sticky=W)

        self.radioD2 = Radiobutton(self, text="Thai Iced Tea -- $3 -- Glass of thai iced tea", variable=self.d,
                    value="Thai Iced Tea", fg="black")
        self.radioD2.grid(row=3, column=11, sticky=W)

        self.radioD3 = Radiobutton(self, text="Coffee -- $1.5 -- Black coffee either hot or cold", variable=self.d,
                    value="Coffee", fg="black")
        self.radioD3.grid(row=4, column=11, sticky=W)

        # Appetizer label
        aa = Label(self, text="Appetizer", fg="green").grid(row=5, column=11, sticky=W)

        # Appetizer item, each is a radio button to ensure one item per type
        self.a = StringVar()
        self.a.set("None")
        self.radioA1 = Radiobutton(self, text="Fresh Spring Rolls -- $3.99 -- 4 vegetarian rolls wrapped in rice paper either fresh or fried", variable=self.a,
                                   value="Soda", fg="black")
        self.radioA1.grid(row=6, column=11, sticky=W)

        self.radioA2 = Radiobutton(self, text="Cream Cheese Wantons -- $5.99 -- Vegetarian friendly fried wantons stuffed with creamcheese", variable=self.a,
                                   value="Thai Iced Tea", fg="black")
        self.radioA2.grid(row=7, column=11, sticky=W)

        self.radioA3 = Radiobutton(self, text="Dumplings -- $5.99 -- 8 pieces of meat dumplings either fried or steamed", variable=self.a,
                                   value="Coffee", fg="black")
        self.radioA3.grid(row=8, column=11, sticky=W)

        # Entree label
        ee = Label(self, text="Entree", fg="green").grid(row=9, column=11, sticky=W)

        # Drink item, each is a radio button to ensure one item per type
        self.e = StringVar()
        self.e.set("None")
        self.radioE1 = Radiobutton(self, text="Shrimp Lo Mein -- $8.5 -- Noodles with shrimp and veggies", variable=self.e,
                                   value="Soda", fg="black")
        self.radioE1.grid(row=10, column=11, sticky=W)

        self.radioE2 = Radiobutton(self, text="Tofu Vegetable Soup -- $5.99 -- Bowl of vegetarian soup with tofu in chicken broth", variable=self.e,
                                   value="Thai Iced Tea", fg="black")
        self.radioE2.grid(row=11, column=11, sticky=W)

        self.radioE3 = Radiobutton(self, text="Beef Fried Rice -- $7.5 -- Rice fried with egg vegetables and beef", variable=self.e,
                                   value="Coffee", fg="black")
        self.radioE3.grid(row=12, column=11, sticky=W)
        self.radioE4 = Radiobutton(self, text="Vegetable Lo Mein -- $8.5 -- Vegetarian friendly noodles", variable=self.e,
                                   value="Coffee", fg="black")
        self.radioE4.grid(row=13, column=11, sticky=W)
        self.radioE5 = Radiobutton(self, text="Chicken Mushroom Soup -- $5.99 -- Bowl of soup with chicken and mushrooms in chicken broth", variable=self.e,
                                   value="Coffee", fg="black")
        self.radioE5.grid(row=14, column=11, sticky=W)

        # Dessert label
        dede = Label(self, text="Dessert", fg="green").grid(row=15, column=11, sticky=W)

        # Dessert item, each is a radio button to ensure one item per type
        self.de = StringVar()
        self.de.set("None")
        self.radioDe1 = Radiobutton(self, text="Ice Cream -- $3.5 -- 3 scoops of chocolate or vanilla or strawberry", variable=self.de,
                                   value="Soda", fg="black")
        self.radioDe1.grid(row=16, column=11, sticky=W)

        self.radioDe2 = Radiobutton(self, text="Chocolate Cake -- $4.5 -- Slice of dark chocolate cake", variable=self.de,
                                   value="Thai Iced Tea", fg="black")
        self.radioDe2.grid(row=17, column=11, sticky=W)

        self.radioDe3 = Radiobutton(self, text="Apple Pie -- $4.5 -- American classic served with vanilla ice cream", variable=self.de,
                                   value="Coffee", fg="black")
        self.radioDe3.grid(row=18, column=11, sticky=W)

    # This function shows the status of yes/no in the radiobutton
    def show(self):
        messagebox.showinfo("Show", self.svYesNo.get())

    # This function shows the status of check/uncheck in the checkbutton
    def test(self):
        if self.bvCheck.get() == True:
            messagebox.showinfo("Test", "You checked!")
        else:
            messagebox.showinfo("Test", "You have not checked!")

    # This function display menu in the Entry box
    def showMenu(self):
        # messagebox.showinfo("Message", "Today is Thursday")
        pass