#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Little script to test methods developped in chaine_list.py with unittest"""
__author__ = 'TOUMI Anouar'

import unittest
from chained_list import ChainedList


class Testlist(unittest.TestCase):
    """Class to test ChainedList() methods"""

    def setUp(self):
        """Initialize before every test"""
        self.list = ChainedList()

    def test_list_none(self):
        """Verify if list is Empty at beginning"""
        self.assertIsNone(self.list.first_node)

    def test_list_not_none(self):
        """Verify if after adding a element to list is not empty"""
        self.list.add_node(5)
        self.assertIsNotNone(self.list.first_node)

    def test_list_equal(self):
        """Check is list is still the same after adding and removing a value"""
        list_before = self.list
        self.list.add_node(8)
        self.list.delete_value(8)
        self.assertEqual(list_before, self.list)

    def test_add_first(self):
        """Check if the first value is the one we added"""
        value = 89
        self.list.add_first(value)
        self.assertEqual(value, self.list.first_node.value)

    def test_add_last(self):
        """Check if the last value is the one we added"""
        value = 10
        self.list.add_last(value)
        self.assertEqual(value, self.list.return_last_value())


if __name__ == "__main__":
    unittest.main()
