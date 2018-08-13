import csv
import pygtrie

class listsuggestions():
    def __init__(self, words):
        self.trie = pygtrie.CharTrie((word[0], True) for word in words)
        
    def suggest(self, prefix):
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
