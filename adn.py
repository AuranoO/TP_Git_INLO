#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    get_valid_adn allows user to check if string is only nucleotide
"""
#Version develop
__author__ = 'Anouar TOUMI'



def is_valid(adn_str: str)->bool:
    not_nucleotide = 0
    for nuc in adn_str:
        if nuc not in ("ATCGatcg"):
            not_nucleotide += 1
        else: 
            pass
    if not_nucleotide == 0:
        return True
    else:
        return False


def get_valid_adn(prompt="Chaine d'ADN : ")->str:
    input_sequence = input(prompt)
    if is_valid(input_sequence) is True:
        print("La chaine d'ADN est valide")
    else:
        print("La chaine d'ADN n'est pas valide")
    return input_sequence
