from tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("VietFamily Restaurant")


def main():

    def callBack(number):
        count = number + 1
        item(count)
    def item(number):
        menu = ['nft', 'nckt', 'cat', 'nck outer reef burrito',]
        m = Label(root, text=menu[number], fg="orange").grid(row=7, column=0)
    root = Tk()
    app = Example(root)
    #root.geometry("750x750+400+50")
    for r in range(20):
        for c in range(14):
            Label(root, text='',
                borderwidth=0).grid(row=r,column=c)
    count = -1
    B = Button(root, text ="Submit and Continue", relief=RIDGE, fg="black", command= lambda:callBack(count)).grid(row=19, column=7)
    L = Label(root, text="What comes in the following", fg="blue").grid(row=6, column=0)
    #I = Label(root, text="***Loop Items Here***", fg="blue").grid(row=7, column=0)
    V = Label(root, text="Veggies", fg="green").grid(row=1, column=11, sticky=W)
    v1 = IntVar()
    Checkbutton(root, text="Lettuce", variable=v1, fg="black").grid(row=2, column=11, sticky=W)
    v2 = IntVar()
    Checkbutton(root, text="Cabbage", variable=v2).grid(row=3, column=11, sticky=W)
    v3 = IntVar()
    Checkbutton(root, text="Cheese", variable=v3).grid(row=4, column=11, sticky=W)
    v4 = IntVar()
    Checkbutton(root, text="Ahee Rice", variable=v4).grid(row=5, column=11, sticky=W)
    v5 = IntVar()
    Checkbutton(root, text="Brown Rice", variable=v5).grid(row=6, column=11, sticky=W)
    v6 = IntVar()
    Checkbutton(root, text="Banzai Veg", variable=v6).grid(row=7, column=11, sticky=W)
    v7 = IntVar()
    Checkbutton(root, text="Red Cabbage", variable=v7).grid(row=8, column=11, sticky=W)
    v8 = IntVar()
    Checkbutton(root, text="Black Beans", variable=v8).grid(row=9, column=11, sticky=W)
    v9 = IntVar()
    Checkbutton(root, text="Cajun White Beans", variable=v9).grid(row=10, column=11, sticky=W)
    T = Label(root, text="Tortillas     ", fg="green").grid(row=1, column=12, sticky=W)
    t1 = IntVar()
    Checkbutton(root, text="Corn          ", variable=t1).grid(row=2, column=12, sticky=W)
    t2 = IntVar()
    Checkbutton(root, text="Flour", variable=t2).grid(row=3, column=12, sticky=W)
    P = Label(root, text="Proteins", fg="green").grid(row=1, column=13, sticky=W)
    p1 = IntVar()
    Checkbutton(root, text="Carne Asada", variable=p1).grid(row=2, column=13, sticky=W)
    p2 = IntVar()
    Checkbutton(root, text="Flamebroiled Chicken", variable=p2).grid(row=3, column=13, sticky=W)
    p3 = IntVar()
    Checkbutton(root, text="Blackened Chicken", variable=p3).grid(row=4, column=13, sticky=W)
    p4 = IntVar()
    Checkbutton(root, text="Flamebroiled Fish", variable=p4).grid(row=5, column=13, sticky=W)
    p5 = IntVar()
    Checkbutton(root, text="Pork", variable=p5).grid(row=6, column=13, sticky=W)
    p6 = IntVar()
    Checkbutton(root, text="Shrimp", variable=p6).grid(row=7, column=13, sticky=W)
    p7 = IntVar()
    Checkbutton(root, text="Tofu", variable=p7).grid(row=8, column=13, sticky=W)
    p8 = IntVar()
    Checkbutton(root, text="Blackened Mushroom", variable=p8).grid(row=9, column=13, sticky=W)
    p9 = IntVar()
    Checkbutton(root, text="Rice and Beans", variable=p9).grid(row=10, column=13, sticky=W)
    p10 = IntVar()
    Checkbutton(root, text="Banzai Veg", variable=p10).grid(row=11, column=13, sticky=W)
    S = Label(root, text="Sauces", fg="green").grid(row=1, column=14, sticky=W)
    s1 = IntVar()
    Checkbutton(root, text="Salsa", variable=s1).grid(row=2, column=14, sticky=W)
    s2 = IntVar()
    Checkbutton(root, text="Guacamole", variable=s2).grid(row=3, column=14, sticky=W)
    s3 = IntVar()
    Checkbutton(root, text="Sour Cream", variable=s3).grid(row=4, column=14, sticky=W)
    s4 = IntVar()
    Checkbutton(root, text="Roasted Pepper", variable=s4).grid(row=5, column=14, sticky=W)
    s5 = IntVar()
    Checkbutton(root, text="Ketchup", variable=s5).grid(row=6, column=14, sticky=W)
    s6 = IntVar()
    Checkbutton(root, text="Ranch", variable=s6).grid(row=7, column=14, sticky=W)
    s7 = IntVar()
    Checkbutton(root, text="Balsamic", variable=s7).grid(row=8, column=14, sticky=W)
    s8 = IntVar()
    Checkbutton(root, text="Mr. Lees", variable=s8).grid(row=9, column=14, sticky=W)
    s9 = IntVar()
    Checkbutton(root, text="Teriyaki", variable=s9).grid(row=10, column=14, sticky=W)
    s10 = IntVar()
    Checkbutton(root, text="Tapatio", variable=s10).grid(row=11, column=14, sticky=W)
    s11 = IntVar()
    Checkbutton(root, text="Cream Cheese", variable=s11).grid(row=12, column=14, sticky=W)
    s12 = IntVar()
    Checkbutton(root, text="Aoli", variable=s12).grid(row=13, column=14, sticky=W)

    root.bind('<Return>', callBack)
    root.mainloop()


if __name__ == '__main__':
    main()