import lexNode

START = '<START>'
END = '<END>'

class Lexicon:

	def __init__(self):
		self.root = LexNode(START)

	def addWord(self, word):
		word = word.strip()
		for letter in word:
			
