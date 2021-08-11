"""Implementation of the Trie data structure.

Author: Henrik Abel Christensen
"""
from typing import List

from .node import Node


class Trie:
    """A Trie."""
    __root: Node

    def __init__(self):
        """Initializes a new Trie."""
        self.__root = Node()

    def is_empty(self):
        """Returns whether the Trie is empty or not.

        Returns
        -------
        bool
            True if the Trie is empty, otherwise False.
        """
        return len(self.__root) == 0

    def insert(self, word: str) -> None:
        """Adds a word to the Trie.

        Parameters
        ----------
        word : str
            The word to add to the Trie.
        """
        current_node = self.__root
        for idx, char in enumerate(word):
            last_char = False
            if idx == len(word) - 1:
                last_char = True
            current_node = current_node.add_child(char, last_char)

    def contains(self, word: str) -> bool:
        """Returns whether the Trie contains the given word or not.

        Parameters
        ----------
        word : str
            The word to search for in the Trie.

        Returns
        -------
        bool
            True if the given word is in the Trie, otherwise False.
        """
        current_node = self.__root
        for char in word:
            if not current_node.has_child(char):
                return False
            child_node = current_node.get_child(char)
            if child_node is None:
                return False
            current_node = child_node
        return current_node.is_end

    def remove(self, word: str) -> str:
        """Removes the given word from the Trie and returns the removed word.

        Parameters
        ----------
        word : str
            The word to remove from the Trie.

        Returns
        -------
        str
            The removed word if removed successfully,
            otherwise an empty string.

        Raises
        ------
        ValueError
            If the word is an empty string.
        """
        if word == '':
            raise ValueError(f'undefined word: {word}')

        current_node: Node = self.__root
        nodes: List[Node] = list()

        for char in word:
            nodes.insert(0, current_node)
            child_node = current_node.get_child(char)
            if child_node is None:
                return ''
            current_node = child_node
        current_node.is_end = False

        if len(current_node) > 0:
            return word

        i = 1
        for node in nodes:
            node_child = node.remove_child(word[-i])
            if node_child is None:
                break
            i += 1
        return word
