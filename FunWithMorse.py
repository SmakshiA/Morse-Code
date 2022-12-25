from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image


# imported tkinter and pillow libraries

# function clear widgets clears all the widgets in list widgets
def clear_widgets(self):
    for i in widgets:
        i.destroy()


# dictionary to store alphabets and numbers with their morse code
dict = {" ": "",
        "a": "•-",
        "b": "-•••",
        "c": "-•-•",
        "d": "-••",
        "e": "•",
        "f": "••-•",
        "g": "--•",
        "h": "••••",
        "i": "••",
        "j": "•---",
        "k": "-•-",
        "l": "•-••",
        "m": "--",
        "n": "-•",
        "o": "---",
        "p": "•--•",
        "q": "--•-",
        "r": "•-•",
        "s": "•••",
        "t": "-",
        "u": "••-",
        "v": "•••-",
        "w": "•--",
        "x": "-••-",
        "y": "-•--",
        "z": "--••",
        "1": "•----",
        "2": "••---",
        "3": "•••--",
        "4": "••••-",
        "5": "•••••",
        "6": "-••••",
        "7": "--•••",
        "8": "---••",
        "9": "----•",
        "0": "-----",
        }

# widgets list stores buttons and label on a new frame
widgets = []
# images list
images = []


class Form:

    # default constructor of class Form
    def __init__(self, root):

        def_font = font.Font(family='Times')
        self.f = Frame(root, height=1000, width=1000)
        self.f.propagate(0)
        # set background colour, colour in the form of Hexcode
        self.f.config(bg="#FCF5B2")
        self.f.pack()
        # Label to display the title
        self.intro = Label(self.f, text="Fun with Morse", height=10, width=30, font=(def_font, 35), bg="#FCF5B2",
                           anchor=CENTER)
        # b1 Button to Start
        self.b1 = Button(self.f, text="Start", width=15, height=2, bg="#D0AFF8", command=lambda: self.frame2(),
                         relief=RIDGE)
        # b2 Button to Exit
        self.b2 = Button(self.f, text="Exit", width=15, height=2, bg="#D0AFF8", command=exit, relief=RIDGE)
        self.imgm = Image.open("morse.png")
        # ANTIALIAS is used to reduce visual defects
        self.imagem = self.imgm.resize((400, 400), Image.ANTIALIAS)
        # ImageTk.PhotoImage is used to import Photo
        self.picm = ImageTk.PhotoImage(self.imagem)
        self.panelm = Label(self.f, image=self.picm, anchor=CENTER)
        self.panelm.place(x=300, y=150)
        # append all the widgets to list widgets and place on frame
        widgets.append(self.panelm)
        widgets.append(self.intro)
        widgets.append(self.b1)
        widgets.append(self.b2)
        self.intro.place(x=100, y=-200)
        self.b2.place(x=200, y=600)
        self.b1.place(x=700, y=600)

    # Frame 1 - Introductory
    def frame1(self):
        clear_widgets(self)
        def_font = font.Font(family='Times')
        self.intro = Label(self.f, text="Fun with Morse", height=10, width=30, font=(def_font, 35), bg="#FCF5B2",
                           anchor=CENTER)
        self.b1 = Button(self.f, text="Start", width=15, height=2, bg="#D0AFF8", command=lambda: self.alphabet(),
                         relief=RIDGE)
        self.b2 = Button(self.f, text="Exit", width=15, height=2, bg="#D0AFF8", command=exit, relief=RIDGE)
        # append all the widgets to list widgets
        widgets.append(self.intro)
        widgets.append(self.b1)
        widgets.append(self.b2)
        # place the widgets
        self.intro.place(x=100, y=30)
        self.b2.place(x=200, y=500)
        self.b1.place(x=700, y=500)

    # Frame 2 - Menu
    def frame2(self):
        # clears all the widgets on previous frame
        clear_widgets(self)
        self.title2 = Label(self.f, text="Pick an action", height=10, width=30, font=("Helvetica 15 underline", 35),
                            bg="#FCF5B2", anchor=CENTER, fg="black")
        self.title2.place(x=90, y=-200)
        self.alpha = Button(self.f, text="Alphabet", width=15, height=2, bg="#D0AFF8", command=lambda: self.alphabet(),
                            relief=RIDGE)
        self.phrases = Button(self.f, text="Phrases", width=15, height=2, bg="#D0AFF8",
                              command=lambda: self.phrasesf1(), relief=RIDGE)
        self.funfacts = Button(self.f, text="Fun Facts", width=15, height=2, bg="#D0AFF8", command=lambda: self.txt(),
                               relief=RIDGE)
        # append all the widgets to list widgets
        widgets.append(self.title2)
        widgets.append(self.alpha)
        widgets.append(self.phrases)
        widgets.append(self.funfacts)
        # place the widgets
        self.alpha.place(x=200, y=200)
        self.phrases.place(x=200, y=500)
        self.funfacts.place(x=700, y=200)

        self.prev = Button(self.f, text="Exit", width=15, height=2, bg="#D0AFF8", command=lambda: exit(), relief=RIDGE)
        self.prev.place(x=450, y=620)
        widgets.append(self.prev)
        self.encode = Button(self.f, text="Encode Message", width=15, height=2, bg="#D0AFF8",
                             command=lambda: self.testing(),
                             relief=RIDGE)
        widgets.append(self.encode)
        self.encode.place(x=700, y=500)
        self.imgd = Image.open("d.png")
        self.imaged = self.imgd.resize((300, 400), Image.ANTIALIAS)
        self.picd = ImageTk.PhotoImage(self.imaged)
        self.paneld = Label(self.f, image=self.picd, anchor=CENTER)
        self.paneld.place(x=360, y=180)
        widgets.append(self.paneld)

    # Frame of Aphabet Guide
    def alphabet(self):
        self.img = Image.open("alphabet.png")
        clear_widgets(self)
        self.alphabet_title = Label(self.f, text="Alphabet Guide", height=10, width=30,
                                    font=("Helvetica 15 underline", 35), bg="#FCF5B2", anchor=CENTER, fg="black")
        self.image = self.img.resize((800, 450), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(self.image)
        self.panel = Label(self.f, image=self.pic, anchor=CENTER)

        self.alphabet_title.place(x=90, y=-200)
        self.prev = Button(self.f, text="Previous", width=15, height=2, bg="#D0AFF8", command=lambda: self.frame2(),
                           relief=RIDGE)
        self.prev.place(x=450, y=620)
        widgets.append(self.panel)
        widgets.append(self.alphabet_title)
        widgets.append(self.prev)
        self.panel.place(x=100, y=150)

    # Frame 1 of Phrases
    def phrasesf1(self):
        clear_widgets(self)
        self.phrases_title = Label(self.f, text="Common Phrases", height=10, width=30,
                                   font=("Helvetica 15 underline", 35), bg="#FCF5B2", anchor=CENTER, fg="black")
        widgets.append(self.phrases_title)
        self.phrases_title.place(x=90, y=-200)

        self.b0 = Button(self.f, text="Good Morning", width=25, height=2, bg="#D0AFF8", command=lambda: self.gm(),
                         relief=RIDGE)
        self.b0.place(x=80, y=170)

        self.b1 = Button(self.f, text="Hello", width=25, height=2, bg="#D0AFF8", command=lambda: self.hello(),
                         relief=RIDGE)
        self.b1.place(x=80, y=280)

        self.b2 = Button(self.f, text="Thank You", width=25, height=2, bg="#D0AFF8", command=lambda: self.thank_you(),
                         relief=RIDGE)
        self.b2.place(x=80, y=370)

        self.b3 = Button(self.f, text="Sorry", width=25, height=2, bg="#D0AFF8", command=lambda: self.sorry(),
                         relief=RIDGE)
        self.b3.place(x=80, y=460)

        self.next = Button(self.f, text="Next", width=25, height=2, bg="#D0AFF8", command=lambda: self.phrasesf2(),
                           relief=RIDGE)
        self.next.place(x=800, y=620)
        self.prev = Button(self.f, text="Previous", width=25, height=2, bg="#D0AFF8", command=lambda: self.frame2(),
                           relief=RIDGE)
        self.prev.place(x=100, y=620)
        widgets.append(self.prev)

        widgets.append(self.b0)
        widgets.append(self.b1)
        widgets.append(self.b2)
        widgets.append(self.b3)

        widgets.append(self.next)

    # Frame 2 of Phrases
    def phrasesf2(self):
        clear_widgets(self)
        self.b4 = Button(self.f, text="Please", width=25, height=2, bg="#D0AFF8", command=lambda: self.please(),
                         relief=RIDGE)
        self.b4.place(x=80, y=170)
        self.b5 = Button(self.f, text="Goodbye", width=25, height=2, bg="#D0AFF8", command=lambda: self.goodbye(),
                         relief=RIDGE)
        self.b5.place(x=80, y=280)
        self.b6 = Button(self.f, text="Ask", width=25, height=2, bg="#D0AFF8", command=lambda: self.ask(), relief=RIDGE)
        self.b6.place(x=80, y=370)
        self.b7 = Button(self.f, text="Name", width=25, height=2, bg="#D0AFF8", command=lambda: self.name(),
                         relief=RIDGE)
        self.b7.place(x=80, y=460)
        widgets.append(self.b4)
        widgets.append(self.b5)
        widgets.append(self.b6)
        widgets.append(self.b7)
        self.prev = Button(self.f, text="Previous", width=15, height=2, bg="#D0AFF8", command=lambda: self.phrasesf1(),
                           relief=RIDGE)
        self.prev.place(x=100, y=620)
        widgets.append(self.prev)
        self.back_main = Button(self.f, text="Return to Menu", width=15, height=2, bg="#D0AFF8",
                                command=lambda: self.frame2(), relief=RIDGE)
        self.back_main.place(x=800, y=620)
        widgets.append(self.back_main)

    # Frame of Fun Facts
    def txt(self):
        clear_widgets(self)

        self.f["bg"] = "#FCF5B2"
        # Import a .txt file using File Handling concept
        f = open(r"Facts.txt")
        self.d2 = Label(root, height=20, width=60, font=("Arial", 20), text=f.read(), bg="#FCF5B2")
        self.d2.place(x=10, y=-23)

        self.prev = Button(self.f, text="Previous", width=15, height=2, bg="#D0AFF8", command=lambda: self.frame2(),
                           relief=RIDGE)
        self.prev.place(x=450, y=650)
        widgets.append(self.d2)
        widgets.append(self.prev)

    # Function to display Good Morning image
    def gm(self):
        self.imggm = Image.open("Good Morning.png")
        self.imagegm = self.imggm.resize((500, 70), Image.ANTIALIAS)
        self.picgm = ImageTk.PhotoImage(self.imagegm)
        self.panelgm = Label(self.f, image=self.picgm, anchor=CENTER)
        self.panelgm.place(x=400, y=150)
        widgets.append(self.panelgm)

    # Function to display Hello image
    def hello(self):
        self.imgh = Image.open("Hello.png")
        self.imageh = self.imgh.resize((500, 70), Image.ANTIALIAS)
        self.pich = ImageTk.PhotoImage(self.imageh)
        self.panelh = Label(self.f, image=self.pich, anchor=CENTER)
        self.panelh.place(x=400, y=260)
        widgets.append(self.panelh)

    # Function to display Thank you image
    def thank_you(self):
        self.imgt = Image.open("Thank you.png")
        self.imaget = self.imgt.resize((500, 70), Image.ANTIALIAS)
        self.pict = ImageTk.PhotoImage(self.imaget)
        self.panelt = Label(self.f, image=self.pict, anchor=CENTER)
        self.panelt.place(x=400, y=350)
        widgets.append(self.panelt)

    # Function to display Sorry image
    def sorry(self):
        self.imgs = Image.open("Sorry.png")
        self.images = self.imgs.resize((500, 70), Image.ANTIALIAS)
        self.pics = ImageTk.PhotoImage(self.images)
        self.panels = Label(self.f, image=self.pics, anchor=CENTER)
        self.panels.place(x=400, y=440)
        widgets.append(self.panels)

    # Function to display Please image
    def please(self):
        self.imgp = Image.open("Please.png")
        self.imagep = self.imgp.resize((500, 70), Image.ANTIALIAS)
        self.picp = ImageTk.PhotoImage(self.imagep)
        self.panelp = Label(self.f, image=self.picp, anchor=CENTER)
        self.panelp.place(x=400, y=150)
        widgets.append(self.panelp)

    # Function to display Good Bye image
    def goodbye(self):
        self.imgg = Image.open("Good Bye.png")
        self.imageg = self.imgg.resize((500, 70), Image.ANTIALIAS)
        self.picg = ImageTk.PhotoImage(self.imageg)
        self.panelg = Label(self.f, image=self.picg, anchor=CENTER)
        self.panelg.place(x=400, y=260)
        widgets.append(self.panelg)

    # Function to display Ask image
    def ask(self):
        self.imga = Image.open("Ask.png")
        self.imagea = self.imga.resize((500, 70), Image.ANTIALIAS)
        self.pica = ImageTk.PhotoImage(self.imagea)
        self.panela = Label(self.f, image=self.pica, anchor=CENTER)
        self.panela.place(x=400, y=350)
        widgets.append(self.panela)

    # Function to display Name image
    def name(self):
        self.imgn = Image.open("Name.png")
        self.imagen = self.imgn.resize((500, 70), Image.ANTIALIAS)
        self.picn = ImageTk.PhotoImage(self.imagen)
        self.paneln = Label(self.f, image=self.picn, anchor=CENTER)
        self.paneln.place(x=400, y=440)
        widgets.append(self.paneln)

    # Frame to encode any message
    def testing(self):
        clear_widgets(self)
        self.title3 = Label(self.f, text="Encode your message!", height=10, width=30,
                            font=("Helvetica 15 underline", 35), bg="#FCF5B2", anchor=CENTER, fg="black")
        widgets.append(self.title3)
        self.title3.place(x=90, y=-200)
        # Text Box to take input from user
        self.msg = Text(self.f, height=5, width=50, fg="black", bg="white", font=("Arial", 20))
        self.enc = Button(self.f, text="Encode", width=15, height=2, bg="#D0AFF8", command=lambda: self.printInput(),
                          relief=RIDGE)
        self.enc.place(x=450, y=500)
        widgets.append(self.enc)
        self.msg.place(x=110, y=110)
        widgets.append(self.msg)
        self.prev = Button(self.f, text="Previous", width=15, height=2, bg="#D0AFF8", command=lambda: self.frame2(),
                           relief=RIDGE)
        self.prev.place(x=100, y=620)
        widgets.append(self.prev)

    # Function to display encoded message
    def printInput(self):
        # store input from text box in String variable
        inp = self.msg.get(1.0, "end-1c")
        inp = inp.lower()
        morse_string = ""
        for i in inp:
            for j in dict:
                if i == j:
                    morse_string += dict[i] + " "
                    if i == " ":
                        morse_string += "/"

        self.title4 = Label(self.f, text="Encoded message : ", height=3, width=30, font=("Helvetica 15 underline", 20),
                            bg="#FCF5B2", anchor=E, fg="black")
        widgets.append(self.title4)
        self.title4.place(x=-110, y=280)
        self.title4 = Label(self.f, text=morse_string, height=1, width=40, font=("Helvetica 15 underline", 20),
                            bg="#FCF5B2", fg="black")
        widgets.append(self.title4)
        self.title4.place(x=40, y=350)


# root object of class Tkinter
root = Tk()
root.title("Fun with Morse")
# create object of class myForm
myForm = Form(root)
root.mainloop()
