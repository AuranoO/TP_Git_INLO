#!/usr/bin/env python3
# coding: utf-8
"""
Class Controller of the project
@author : Olivier CHABROL / Anouar TOUMI
"""

# Imports
from view_obj import View
from model import Phonebook
from model import Person


class Controller():
    """
    Class to implement a controller.
    """

    def __init__(self):
        """
        Class Constructor
        """
        self.view = View(self)
        self.model = Phonebook()

    def start_view(self):
        """
        Create tkinter window trought method defined in View class
        """
        self.view.create_fields()
        self.view.main()

    def search(self):
        """
        Use search_person method to find a person with his firstname or lastname in memory
        """
        if len(self.view.get_value("Nom")) > 0:
            name = self.view.get_value("Nom")
            self.view.popup(self.model.search_person(name))

        elif len(self.view.get_value("Prenom")) > 0 and len(self.view.get_value("Nom")) == 0:
            name = self.view.get_value("Prenom")
            self.view.popup(self.model.search_person(name))
        else:
            self.view.popup("Veuillez inserer un nom ou un prénom")

    def delete(self):
        """
        Use delete_person method to delete information of a person
        with his firstname or lastname in memory
        """
        if len(self.view.get_value("Nom")) > 0:
            name = self.view.get_value("Nom")
            self.view.popup(self.model.delete_person(name))

        elif len(self.view.get_value("Prenom")) > 0 and len(self.view.get_value("Nom")) == 0:
            name = self.view.get_value("Prenom")
            self.view.popup(self.model.delete_person(name))
        else:
            self.view.popup("Veuillez inserer un nom ou prénom")

    def insert(self):
        """
        Create a Person object and insert into a dictonnary
        """
        if len(self.view.get_value("Nom")) > 0 and len(self.view.get_value("Prenom")) > 0:
            person = Person(self.view.get_value("Nom"),
                            self.view.get_value("Prenom"),
                            self.view.get_value("Telephone"),
                            self.view.get_value("Adresse"),
                            self.view.get_value("Ville"))

            self.model.insert_person(person)
            self.view.popup("Le contact a été ajouté")
        else:
            self.view.popup("Veuillez inserer un nom et un prénom")

    def button_press_handle(self, button_id):
        """
        Link usage of a button and his associate method
        """
        print("[Controller][button_press_handle] " + button_id)
        if button_id == "Chercher":
            self.search()
        elif button_id == "Effacer":
            self.delete()
        elif button_id == "Inserer":
            self.insert()
        elif button_id == "Quitter":
            self.model.save()
            self.view.quit()
        else:
            pass


if __name__ == "__main__":
    controller = Controller()
    controller.start_view()
