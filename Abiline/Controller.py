from View import View
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)
        self.open_filetype = ("Textfiles", "*.txt"), ("All files", "*.*")


    def button_nimekiri(self):
        file_path = filedialog.askopenfilename(filetypes=self.open_filetype)
        if file_path:
            with open(file_path, encoding="utf-8") as f:
                self.model.nimed = [line.strip() for line in f]
                self.view.nimekiri_lbox.delete(0, tk.END)
            for nimi in self.model.nimed:
                self.view.nimekiri_lbox.insert(tk.END, nimi)

    def button_ulesanded(self):
        file_path = filedialog.askopenfilename(filetypes=self.open_filetype)
        if file_path:
            with open(file_path, encoding="utf-8") as f:
                self.model.ulesanded = [line.strip() for line in f]
                self.view.ulesanded_lbox.delete(0, tk.END)
            for ulesanne in self.model.ulesanded:
                self.view.ulesanded_lbox.insert(tk.END, ulesanne)

    def button_info(self):
        messagebox.showinfo("Info", "1. Vajuta nupule Nimekiri, et avada nimekirja fail. \n"
                                    "2. Vajuta nupule Ülesanded, et avada ülesannete fail. \n"
                                    "3. Vajuta nupule Genereeri, et genereerida nimele suvaline ülesanne. \n"
                                    "4. Vajuta nupule Salvesta, et salvestada genereeritud ülesanded.")

    def button_generate(self):
        self.view.genereeritud_lbox.delete(0, tk.END)
        self.for_saving = list(self.model.generate(self.model))
        for nimi, ulesanne in self.for_saving:
            self.view.genereeritud_lbox.insert(tk.END, f"{nimi}: {ulesanne}")

    def button_save(self):
        file_path = filedialog.asksaveasfilename(filetypes=self.open_filetype,
                                                 defaultextension=".txt", initialfile="generated_tasks.txt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                for nimi, ulesanne in self.for_saving:
                    f.write(f"{nimi} - {ulesanne}\n")

    def main(self):
        self.view.main()
