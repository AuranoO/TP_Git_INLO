#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create parser to use a fasta input file and verify if sequence inside are valid"""
import argparse
import sys
import adn

__author__ = 'Anouar TOUMI'


def create_parser() -> argparse.ArgumentParser:
    """ Declares new parser and adds parser arguments """
    program_description = ''' reading fasta file and checking sequence format '''
    parser = argparse.ArgumentParser(
        add_help=True, description=program_description)
    parser.add_argument('-i', '--inputfile', default=sys.stdin,
                        help="required path of input file in fasta format", type=argparse.FileType("r"),
                        required=True)
    return parser


def main() -> None:
    """ Main function for reading fasta file and checking sequence format """
    str_seq = ""
    dict_seq = {}
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    fasta_sequence = args["inputfile"].readlines()
    for line in fasta_sequence:
        line = adn.purify(line)
        if line != "":
            if line.startswith(">"):
                str_seq = line.replace(">", "")
                dict_seq[str_seq] = ""
            else:
                dict_seq[str_seq] += line
    for key, value in dict_seq.items():
        value = [adn.get_valid_adn(
            value), "La longueur de la séquence est de " + str(len(value)) + " nucléotides", value]
        dict_seq[key] = value
        print("Pour la séquence " + key + " :", value[0:2])


if __name__ == "__main__":
    main()
