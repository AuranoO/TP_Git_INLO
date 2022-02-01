#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An ensemble of Class designed to manage student and grading
@author: Anouar TOUMI
"""


class Person:
    """
    Generic class to create a person object
    """
    def __init__(self, lastname, firstname, phone_number, email):
        """
        Class constructor
        """
        self.lastname = lastname
        self.firstname = firstname
        self.phone_number = phone_number
        self.email = email

    def set_information(self, new_lastname=None, new_firstname=None,
                        new_phone_number=None, new_email=None):
        """
        Method use to update all value set in init
        """
        check_change = ""
        if new_lastname is not None:
            self.lastname = new_lastname
            check_change += "\nLastname was changed"
        if new_firstname is not None:
            self.firstname = new_firstname
            check_change += "\nFirstname was changed"
        if new_phone_number is not None:
            self.phone_number = new_phone_number
            check_change += "\nphone number was changed"
        if new_email is not None:
            self.email = new_email
            check_change += "\nphone number was changed"
        if len(check_change) > 0:
            print(check_change)

    def get_information(self):
        """
        print and return firstname, phone number and email
        """
        print(self.firstname, self.phone_number, self.email)
        return self.firstname, self.phone_number, self.email


class Student(Person):
    """
    Children class of person, having more information especially around subject and grading
    """

    def __init__(self, lastname, firstname, phone_number, email,
                 year_of_subscription, subjects_grades=None):
        """
        Class constructor
        """
        super().__init__(lastname, firstname, phone_number, email)
        self.year_of_subscription = year_of_subscription
        self.subjects_grades = {}
        self.grade = None
        if subjects_grades is not None:
            self.subjects_grades[subjects_grades] = None

    def add_subject_grade(self, subject, grade=None):
        """
        Add a new subject and optionnaly associate a grade to it
        """
        self.grade = grade
        if isinstance(subject, Subject):
            if self.subjects_grades is None:
                self.subjects_grades = {}
            self.subjects_grades[subject.name] = grade
            subject.grades.append(grade)
        else:
            print("Subject doesn't exist, define it please")

    def avg_grade_student(self):
        """
        Take all grades of student to calculate his average value
        """
        total = 0
        count = 0
        for value in self.subjects_grades.values():
            if value is not None:
                total += value
                count += 1
        if count != 0:
            mean = total/count
            print(mean)
            return mean
        print("Student hasn't grades")
        return None

    def not_graded(self):
        """
        Print and return a string containing all subject which don't have a grades
        """
        subject_not_graded = []
        for key, value in self.subjects_grades.items():
            if value is None:
                subject_not_graded.append(key)
        if len(subject_not_graded) == 0:
            print("All subjects has no grades")
            return subject_not_graded
        print("Not graded in " + ", ".join(subject_not_graded))
        return subject_not_graded

    def get_grades(self):
        """
        print and return the dictionary containing all subject and their grades
        """
        if bool(self.subjects_grades) is False:
            print("Has no grades")
            return None
        print(self.subjects_grades)
        return self.subjects_grades


class Subject:
    """
    Builder class creating teaching unite
    """
    def __init__(self, name):
        """
        Class constructor
        """
        self.name = name
        self.grades = []

    def avg_grade(self):
        """
        Take all grades of subject to calculate his average value
        """
        total = 0
        count = 0
        for note in self.grades:
            if note is not None:
                total += note
                count += 1

        if count != 0:
            mean = total/count
            print(mean)
            return mean
        print("Subject has no grades")
        return None

    def __str__(self):
        """
        This method returns a string of all grades in subject
        """
        string = "The Grade in this subject are "
        string += ', '.join(str(e) for e in self.grades)
        return string
