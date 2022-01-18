# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""  Checking if a str is a valid nucleotides strand or not """
__author__ = 'Anouar TOUMI'

import re


def purify(adn_str: str) -> str or None:
    """
    purify string from some character
    parameter : adn_str is a string
    return : adn_str_purify is the same string purified
    """
    if adn_str is None or len(adn_str) == 0:
        return None
    adn_str_purify = adn_str.replace(
        " ", "").replace("\n", "").replace('\t', '')
    return adn_str_purify


def is_valid(adn_str: str) -> bool:
    """
    Check if string contains only nucleotides
    parameter : adn_str is a string
    return : bool if adn_str is only nucleotides
    """
    if adn_str is None:
        return False
    return bool(re.compile('^[ATCGatcg]+$').search(adn_str))


def get_valid_adn(adn_str: str) -> str:
    """
    Use is_valid() function to check if str are only nucleotides and return str answer
    parameter : adn_str is a string
    return : a string to answer if adn_str is a valid ADN strand or not
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
    return "La chaine d'ADN est valide"
