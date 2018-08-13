import csv
import pygtrie

class listsuggestions():
    """Autocomplete System.
    Maintains a trie with keys from a given corpus of words.
    Gives autocompletion suggestions by retrieving all keys for a give prefix.
    """ 

    def __init__(self, words):
        """Initialize a autocompleter with a given set of words."""
        self.trie = pygtrie.CharTrie((word[0], True) for word in words)
        
    def suggest(self, prefix):
        """Return all words in the corpus starting with a given prefix."""
        try:
            return self.trie.keys(prefix=prefix)
        except KeyError:
            return []

def loader(filename):
	with open(filename, 'r') as f:
	    reader = csv.reader(f)
	    titles = list(reader)
	return titles

if __name__ == '__main__':
	loader()
