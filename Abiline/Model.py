import random
import tkinter.messagebox


class Model:

    def __init__(self, nimed, ulesanded):
        self.ulesanded = ulesanded
        self.nimed = nimed

    def generate(self):
        if len(self.nimed) > len(self.ulesanded):
            tkinter.messagebox.showwarning(title="Viga", message="Nimede ja ülesannete arv ei ühildu")
            return []

        else:
            random.shuffle(self.ulesanded)
            output = [(nimi, ulesanne) for nimi, ulesanne in zip(self.nimed, self.ulesanded)]

            return output
