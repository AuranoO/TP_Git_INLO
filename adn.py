#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version develop
__author__ = 'Anouar TOUMI'


def purify(adn_str: str)->str:
    """
    efe
    """

    return adn_str


def is_valid(adn_str: str) -> bool:
    """
    efg
    """
    if adn_str is None or len(adn_str) == 0:
        return False
    for nuc in adn_str:
        if nuc not in "ATCGatcg":
            return False
        else:
            return True


def get_valid_adn(prompt="Donner votre chaine d'ADN : "):
    """
    efeg
    """
    input_sequence = input(prompt)
    if is_valid(input_sequence) is not True:
        print("La chaine d'ADN n'est pas valide")
    else:
        print("La chaine d'ADN est valide" + "\n" + input_sequence)
