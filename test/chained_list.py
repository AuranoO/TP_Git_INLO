#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Create a Node and ChainedList class for INLO Class """
__author__ = 'TOUMI Anouar'


class Node:
    """
    A class that represents nodes in a chained list, each node can hold value
    and a pointer to the next node inside the chained list
    """

    def __init__(self, value):
        """
        Class constructor
        """
        self.value = value
        self.next = None

    def __str__(self):
        """
        Returns a string representation of the node
        """
        string = str(self.value)
        if self.next is not None:
            string += ", " + str(self.next)
        return string


class ChainedList:
    """
    A class of linked lists, will build a linked list object from integer values
    """

    def __init__(self):
        """
        Class constructor
        """
        self.first_node = None

    def add_node(self, value: int):
        """
        Method to add node in the chained list as a sorted list
        """
        node = Node(value)
        if self.first_node is None:
            self.first_node = node
        elif value < self.first_node.value:
            node.next = self.first_node
            self.first_node = node
        else:
            before_node = self.first_node
            after_node = before_node.next
            while after_node is not None and after_node.value < node.value:
                before_node = after_node
                after_node = after_node.next
            before_node.next = node
            node.next = after_node

    def delete_value(self, value: int) -> None:
        """
        This method deletes node where node value = given value
        INCOMPLETE TO MODIFY
        """
        if self.first_node.value == value:
            self.first_node = self.first_node.next
        current_node = self.first_node
        while current_node is not None:
            if current_node.value == value:
                current_node.next = current_node.next.next
            current_node = current_node.next

    def add_last(self, value):
        """ Add value at the last item of list"""
        node_to_add = Node(value)
        if self.first_node is None:
            self.first_node = node_to_add
            return
        node = self.first_node

        while node.next is not None:
            node = node.next
        node.next = node_to_add

    def add_first(self, value):
        """Add value at the first item of list"""
        node_to_add = Node(value)
        node_to_add.next = self.first_node
        self.first_node = node_to_add

    def return_last_value(self):
        """Return last value of the list"""
        node = self.first_node
        while node.next is not None:
            node = node.next
        return node.value

    def __iter__(self):
        """
        Method to make list iterable
        """
        node = self.first_node
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        """
        This method returns a string representation of the object
        """

        if self.first_node is None:
            return "liste vide"
        return str(self.first_node)
