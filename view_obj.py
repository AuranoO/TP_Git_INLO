#!/usr/bin/env python3
# coding: utf-8
"""
Class View of the project

@author : Olivier CHABROL
"""

# Imports
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
from tkinter import messagebox


class View(Tk):
    """
    View class to create the window and the widgets
    """
    def __init__(self, controller):
        """
        Class Constructor
        """
        super().__init__()
        self.controller = controller
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.entries = ["Nom", "Prenom", "Telephone", "Adresse", "Ville"]
        self.buttons = ["Chercher", "Inserer", "Effacer", "Quitter"]
        self.model_list_fields = []
        self.file_name = None
        self.windows = {}
        self.windows["fenetreResult"] = ...
        self.windows["fenetreErreur"] = ...

    def get_value(self, key):
        """
        Method to get a value from an entry
        """
        return self.widgets_entry[key].get()

    def create_fields(self):
        """
        Method to create the diffenrents fields of the phonebook (name, last name, adress...)
        """
        i, j = 0, 0

        for idi in self.entries:
            lab = Label(self, text=idi.capitalize())
            self.widgets_labs[idi] = lab
            lab.grid(row=i, column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            self.widgets_entry[idi] = entry
            entry.grid(row=i, column=1)

            i += 1

        for idi in self.buttons:
            buttonw = Button(self, text=idi, command=(
                lambda button=idi: self.controller.button_press_handle(button)))
            self.widgets_button[idi] = buttonw
            buttonw.grid(row=i+1, column=j)

            j += 1

    def quit(self):
        """
        Quit button using a messagebox to ask if sure to quit the phonebook.
        """
        response = messagebox.askokcancel(
            "Quitter", "êtes-vous sûr de vouloir quitter")
        if response:
            self.destroy()

    def popup(self, str):
        """
        Method to create a PopUp and display the information as a contact or an error message
        """
        messagebox.showinfo("Information", str)

    def main(self):
        """
        Method to create and display (mainloop) our window
        """
        print("[View] main")
        self.title("Annuaire")
        self.mainloop()
