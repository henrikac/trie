import unittest

from trie.node import Node


class TestNode(unittest.TestCase):
    def test_new_node_has_no_children(self):
        """Test that a new node has no children."""
        node = Node()
        self.assertEqual(len(node), 0)

    def test_new_node_is_not_a_word(self):
        """Test that a new node by default is not a word."""
        node = Node()
        self.assertFalse(node.is_end)

    def test_add_child(self):
        """Test that nodes can add child nodes."""
        root = Node()
        root.add_child('a', True)
        self.assertEqual(len(root), 1)
        self.assertTrue(root.has_child('a'))

    def test_add_child_can_change_is_end_from_false_to_true(self):
        """Test that add child can change is_end from false to true."""
        root = Node()
        child = root.add_child('a', False)
        child = root.add_child('a', True)
        self.assertEqual(len(root), 1)
        self.assertTrue(child.is_end)

    def test_add_child_cannot_change_is_end_from_true_to_false(self):
        """Test that add child cannot change is_end from true to false."""
        root = Node()
        child = root.add_child('a', False)
        child = root.add_child('a', True)
        child = root.add_child('a', False)
        self.assertEqual(len(root), 1)
        self.assertTrue(child.is_end)

    def test_add_child_raises_value_error_if_given_empty_child(self):
        """Test that add child raises a ValueError
        if the given child is an empty string.
        """
        root = Node()
        with self.assertRaises(ValueError):
            root.add_child('', True)

    def test_add_child_raises_value_error_if_given_invalid_child(self):
        """Test that add child raises a ValueError
        if the given child is longer than one character.
        """
        root = Node()
        with self.assertRaises(ValueError):
            root.add_child('hi', True)

    def test_remove_child(self):
        """Test that node can remove child nodes."""
        root = Node()
        root.add_child('a', True)
        removed_child = root.remove_child('a')
        self.assertEqual(len(root), 0)
        self.assertIsNotNone(removed_child)

    def test_remove_child_returns_none_if_unknown_child(self):
        """Test that remove child returns None if given unknown child."""
        root = Node()
        removed_child = root.remove_child('a')
        self.assertIsNone(removed_child)

    def test_remove_child_raises_value_error_if_child_is_empty_string(self):
        """Test that remove child raises a ValueError
        if the given child is an empty string.
        """
        root = Node()
        with self.assertRaises(ValueError):
            root.remove_child('')


if __name__ == '__main__':
    unittest.main()
