# Trie

Implementation of the [Trie](https://en.wikipedia.org/wiki/Trie) data structure in Python.  

## Requirements
+ Python 3.6+

## Usage

```python
from trie import Trie


my_trie = Trie()

my_trie.insert('moose')
my_trie.insert('mouse')
my_trie.insert('dragon')

my_trie.contains('mouse')  # => True
my_trie.contains('dragon')  # => True
my_trie.contains('moose')  # => True

my_trie.remove('moose')
my_trie.contains('moose')  # => False
```
