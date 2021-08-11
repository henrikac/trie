"""Implementation of a Trie node.

Author: Henrik Abel Christensen
"""
from __future__ import annotations

from typing import Dict, Union


class Node:
    """A Trie node.

    Attributes
    ----------
    is_end : bool
            Tells if the node is the end of a word.
    """
    __children: Dict[str, Node]
    is_end: bool

    def __init__(self) -> None:
        """Initializes a new node."""
        self.__children = dict()
        self.is_end = False

    def __len__(self) -> int:
        """Returns the number of child nodes.

        Returns
        -------
        int
            The number of child nodes.
        """
        return len(self.__children)

    def has_child(self, child: str) -> bool:
        """Returns True if the given child is in the node, otherwise False.

        Returns
        -------
        bool
            True if child is in the node, otherwise False.
        """
        return child in self.__children

    def add_child(self, child: str, end_of_word: bool) -> Node:
        """Adds a child to the node.

        Parameters
        ----------
        child : str
            The name of the child.
        end_of_word : bool
            If the child is the end of a word.

        Returns
        -------
        Node
            The added child.

        Raises
        ------
        ValueError
            If the length of the child is not equal to 1.
        """
        if len(child) != 1:
            raise ValueError(f'invalid child: {child}')
        if not self.has_child(child):
            self.__children[child] = Node()
        if end_of_word:
            self.__children[child].is_end = True
        return self.__children[child]

    def get_child(self, child: str) -> Union[Node, None]:
        """Returns the given child if in the node.

        Returns
        -------
        Node
            The given child if in the node, otherwise None.
        """
        return self.__children.get(child)

    def remove_child(self, child: str) -> Union[Node, None]:
        """Removes a child from the node.

        Parameters
        ----------
        child : str
            The child to remove.

        Returns
        -------
        Node
            The removed child node if removed successfully, otherwise None.

        Raises
        ------
        ValueError
            If the given child is an empty string.
        """
        if child == '':
            raise ValueError(f'undefined child: {child}')
        child_to_remove = self.__children.get(child)
        if child_to_remove is None or child_to_remove.is_end:
            return None
        if len(child_to_remove) == 0:
            del self.__children[child]
            return child_to_remove
        return None
