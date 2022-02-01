#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Test class and method create in unvisersity_class.py
@author: Anouar TOUMI
"""
# Import
import university_class as uc

# Define teaching Unit
prog = uc.Subject('Prog')
genomic = uc.Subject('Genomic')
physic = uc.Subject('Physic')
algo = uc.Subject('Algo')
immuno = uc.Subject('Immuno')

# Create Students
alex = uc.Student('Alex', 'BLANC', '0445', 'alex@ok.com', '2018')
anouar = uc.Student('Anouar', 'TOUMI', '0152',
                    'aurano@ok.com', '2016', physic.name)
warren = uc.Student('Warren', "JHIN", "0000", "nunu@mendes.com", '2020')

# Get the grades of each Student
anouar.get_grades()
alex.get_grades()

# Set a specific information
alex.set_information(new_phone_number='05456')
alex.get_information()

# Append teaching unit and grade for it
alex.add_subject_grade(prog, 10)
anouar.add_subject_grade(prog, 20)

# Get the grade of a Specific teaching unit (__str__ method)
print(prog)

# Check the good way to append teaching unit to a student
alex.add_subject_grade('bio', 12)
anouar.add_subject_grade(genomic, 12)
anouar.add_subject_grade(physic)
anouar.add_subject_grade(algo)
anouar.add_subject_grade(immuno)

# Get the name of teaching unit without grades
anouar.not_graded()
alex.not_graded()

# Check grades of this student
anouar.get_grades()

# Get average of Student's grades
anouar.avg_grade_student()
alex.avg_grade_student()
warren.avg_grade_student()

# Get average of the teaching unit
prog.avg_grade()
immuno.avg_grade()
