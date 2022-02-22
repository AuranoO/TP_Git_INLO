#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model of the project
@author : Anouar TOUMI
"""

# Imports
import os
import pickle


class Person:
    """
    Class to create a person contact for our phone book
    """

    def __init__(self, nom, prenom, telephone='', adresse='', ville=''):
        """
        Class Constructor
        """
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.adresse = adresse
        self.ville = ville

    def get_nom(self):
        "method return current firstname"
        return self.nom

    def get_prenom(self):
        "method return current lastname"
        return self.prenom

    def get_telephone(self):
        "method return current phone"
        return self.telephone

    def get_adresse(self):
        "method return current adress"
        return self.adresse

    def get_ville(self):
        "method return current city"
        return self.ville

    def __str__(self):
        """
        method to represents the class objects as a string
        """
        fiche = "Nom: " + self.get_nom() + "\n"+"Prénom: " + self.get_prenom() + "\n" + \
            "Téléphone: " + self.get_telephone() + "\n" + "Adresse: " + self.get_adresse() + \
            "\n" + "Ville: " + self.get_ville()
        return fiche


class Phonebook:
    """
    Class to create a phone book containing the different contact (Person)
    """

    def __init__(self):
        """
        Class Constructor
        """
        if os.path.exists('./annuaire.pkl'):
            with open("annuaire.pkl", "rb") as file:
                self.list_person = pickle.load(file)
        else:
            self.list_person = {}

    def insert_person(self, person):
        """
        method to insert a new contact
        """
        if isinstance(person, Person):
            prenom = person.get_prenom()
            nom = person.get_nom()
            self.list_person[f"{prenom} {nom}"] = person

    def delete_person(self, name):
        """
        method to delete a contact from the phonebook
        """
        new_list_person = self.list_person.copy()
        delete = False
        for key in self.list_person.keys():
            if name in key:
                del new_list_person[key]
                delete = True
        self.list_person = new_list_person
        if delete is True:
            return "Le contact a été supprimé"
        return "Le contact n'a pas été trouvé"

    def search_person(self, name):
        """
        method to find a contact in our phonebook
        """
        for key in self.list_person.keys():
            if name in key:
                return self.list_person[key]
        return "Le contact n'a pas été trouvé"

    def save(self):
        """
        method to save the actual phonebook in a file.pkl
        """
        with open('annuaire.pkl', 'wb') as file:
            pickle.dump(self.list_person, file)

    def __str__(self):
        """
        method to represents the class object as a string
        """
        test = ''
        for element in self.list_person:
            test += element
        return test
