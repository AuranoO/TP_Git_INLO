#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Little script to test class and methods developped in chaine_list.py"""
__author__ = 'TOUMI Anouar'

import random
import chained_list


if __name__ == "__main__":
    # create a chained list
    cl = chained_list.ChainedList()
    # add random node in list
    for i in range(3):
        cl.add_node(random.randint(-100, 100))
        print(cl)
    # add and delete a specific node by value
    cl.add_node(-5)
    print(cl)
    cl.delete_value(-5)
    print(cl)
    # check iterability of my class
    for i in cl:
        print(i)
