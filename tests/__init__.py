import sys
from pathlib import Path


trie_path = Path(__file__).parent.joinpath('..', 'trie').resolve()

sys.path.append(trie_path)
