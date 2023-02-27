from tkinter import *
import tkinter.font as tkfont
import tkinter as tk



class View(Tk):
    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model
        # Põhiaken
        self.geometry("1170x600")
        self.title("Task Generator v4.56 © 2023")
        self.configure(bg="#BBD4D2")
        self.resizable(False, False)
        # Fondid
        self.big_font_style = tkfont.Font(family="Courier", size=18, weight="bold")
        self.default_style_bold = tkfont.Font(family="Verdana", size=20, weight="bold")
        self.default_style_vahepealne = tkfont.Font(family="Verdana", size=12, weight="bold")
        self.default_style = tkfont.Font(family="Verdana", size=12)
        # Näitab framed põhiaknas
        self.frame_top, self.frame_one, self.frame_two, self.frame_three, self.frame_four = self.create_all_frames()
        # Näitab nupud põhiaknas
        self.button_nimekiri, self.button_ulesanded, self.button_abi, self.button_generate, \
        self.button_save = self.create_all_buttons()
        # Näitab Labelid põhiaknas
        self.label = self.create_all_labels()
        # Näitab Listboxe põhiaknas
        self.nimekiri_lbox, self.ulesanded_lbox, self.genereeritud_lbox = self.create_all_listboxes()

    def main(self):
        self.mainloop()

        # Framede disain
    def create_all_frames(self):
        self.frame_top = Frame(self, bg="#BBD4D2", height=50, width=1170)
        self.frame_one = Frame(self, bg="#BBD4D2", height=550, width=170)
        self.frame_two = Frame(self, bg="#cfe3e5", height=550, width=300)
        self.frame_three = Frame(self, bg="#cfe3e5", height=550, width=300)
        self.frame_four = Frame(self, bg="#cfe3e5", height=550, width=400)

        self.frame_top.pack(side=TOP)
        self.frame_one.pack(side=LEFT)
        self.frame_two.pack(side=LEFT)
        self.frame_three.pack(side=LEFT)
        self.frame_four.pack(side=LEFT)

        return self.frame_top, self.frame_one, self.frame_two, self.frame_three, self.frame_four

        # Nuppude disain, asukoht aknas ja command
    def create_all_buttons(self):

        self.button_nimekiri = tk.Button(self.frame_one, text="Nimekiri", bg="#999556",
                                         command=self.controller.button_nimekiri,
                                         font=self.default_style, height=1, width=15)
        self.button_nimekiri.place(x=5, y=50, in_=self.frame_one)

        self.button_ulesanded = tk.Button(self.frame_one, text="Ülesanded", bg="#999556",
                                          command=self.controller.button_ulesanded,
                                          font=self.default_style, height=1, width=15)
        self.button_ulesanded.place(x=5, y=90, in_=self.frame_one)

        self.button_info = tk.Button(self.frame_one, text="Info", bg="#BBBDD4",
                                     command=self.controller.button_info, font=self.default_style, height=1, width=15)
        self.button_info.place(x=5, y=510, in_=self.frame_one)

        self.button_generate = tk.Button(self.frame_four, text="Genereeri", bg="#CDE5AE",
                                         command=self.controller.button_generate,
                                         font=self.default_style, height=1, width=15)
        self.button_generate.place(x=5, y=510, in_=self.frame_four)

        self.button_save = tk.Button(self.frame_four, text="Salvesta", bg="#D0AF4C",
                                     command=self.controller.button_save,
                                     font=self.default_style, height=1, width=15)
        self.button_save.place(x=230, y=510, in_=self.frame_four)

        return self.button_nimekiri, self.button_ulesanded, self.button_generate, self.button_info, self.button_save

        # Labelite disain ja asukoht
    def create_all_labels(self):

        pealkiri = Label(self.frame_top, bg="#BBD4D2", text="Task Generator",
                         font=self.big_font_style).grid(row=0, column=0, padx=5, pady=5)

        label_nimekiri = Label(self.frame_two, bg="#cfe3e5", text="Nimekiri:",
                               font=self.default_style_vahepealne).place(x=110, y=10)

        label_ulesanded = Label(self.frame_three, bg="#cfe3e5", text="Ülesanded:",
                                font=self.default_style_vahepealne).place(x=110, y=10)

        genereeritud_ulesanded = Label(self.frame_four, bg="#cfe3e5", text="Genereeritud ülesanded:",
                                       font=self.default_style_vahepealne).place(x=110, y=10)

        return pealkiri, label_nimekiri, label_ulesanded, genereeritud_ulesanded

        # Listboxide suurused ja asukoht
    def create_all_listboxes(self):
        self.nimekiri_lbox = tk.Listbox(self.frame_two, width=80, height=29, bg="#e6efee", relief=FLAT)
        self.nimekiri_lbox.place(x=5, y=33, in_=self.frame_two)

        self.ulesanded_lbox = tk.Listbox(self.frame_three, width=80, height=29, bg="#e6efee", relief=FLAT)
        self.ulesanded_lbox.place(x=5, y=33, in_=self.frame_three)

        self.genereeritud_lbox = tk.Listbox(self.frame_four, width=64, height=29, bg="#e6efee", relief=FLAT)
        self.genereeritud_lbox.place(x=5, y=33, in_=self.frame_four)

        return self.nimekiri_lbox, self.ulesanded_lbox, self.genereeritud_lbox


