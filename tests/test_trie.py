import unittest

from trie.trie import Trie


class TestTrie(unittest.TestCase):
    def test_trie_insert(self):
        """Test that a word can be inserted into the Trie."""
        trie = Trie()
        trie.insert('word')
        self.assertFalse(trie.is_empty())

    def test_trie_contains_word(self):
        """Test that contains returns True if the given word is in the Trie."""
        insert_words = [
            "aragon",
            "build",
            "building",
            "home",
            "word",
            "work",
        ]
        fill_words = [
            "amazon",
            "lemon",
            "monkey",
            "open",
        ]
        trie = Trie()
        for word in insert_words:
            trie.insert(word)
        for word in [*insert_words, *fill_words]:
            has_word = trie.contains(word)
            if word in insert_words:
                self.assertTrue(has_word)
            else:
                self.assertFalse(has_word)

    def test_remove_word(self):
        """Test that words can be removed from Trie."""
        trie = Trie()
        trie.insert('word')
        trie.remove('word')
        self.assertTrue(trie.is_empty())

    def test_remove_word_without_messing_up_other_words(self):
        """Test that removing a word does not mess up other words."""
        trie = Trie()
        trie.insert('build')
        trie.insert('building')
        trie.insert('builder')
        trie.insert('moose')
        trie.remove('build')
        trie.remove('moose')
        self.assertFalse(trie.contains('build'))
        self.assertTrue(trie.contains('building'))
        self.assertTrue(trie.contains('builder'))
        self.assertFalse(trie.contains('moose'))


if __name__ == '__main__':
    unittest.main()
