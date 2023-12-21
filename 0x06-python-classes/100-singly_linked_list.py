#!/usr/bin/python3

"""Define classes for a singly-linked list."""

class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes the node with data and an optional next_node.
        
        Args:
        data (int): The data to be stored in the node.
        next_node (Node): The next node in the linked list (default is None).
        
        Raises:
        TypeError: If data is not an integer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data with type validation.
        
        Args:
        value (int): The data to be set.
        
        Raises:
        TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node with type validation.
        
        Args:
        value (Node or None): The next node in the linked list or None.
        
        Raises:
        TypeError: If value is not a Node object or None.
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object or None")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        
        Args:
        value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if not self.head or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout, one node number by line."""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
