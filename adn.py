#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  Checking if a str is a valid nucleotides strand or not """

import re

__author__ = 'Anouar TOUMI'


def purify(adn_str: str) -> str or None:
    """
    purify a string from some character
    """
    if adn_str is None or len(adn_str) == 0:
        return None
    adn_str_purify = adn_str.replace(" ", "").replace("\n", "").replace('\t', '')
    return adn_str_purify

def is_valid(adn_str: str) -> bool:
    """
    Check is purified string contains only nucleotides
    """
    if adn_str is None:
        return False
    return bool(re.compile('^[ATCGatcg]+$').search(adn_str))


def get_valid_adn(adn_str: str) -> str:
    """
    Use is_valid() function to check if str are only nucleotides and return str answer
    """
    if is_valid(adn_str) is False:
        nuc_count = 1
        for i in adn_str:
            if i not in "ATCGatcg":
                answer = "La chaine d'ADN n'est pas valide" + \
                    " car le nucléotide en postion: " + \
                    str(nuc_count) + " est " + i
                return answer
            nuc_count += 1
    else:
        return "La chaine d'ADN est valide"
