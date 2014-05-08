import lexNode

START = '<START>'
END = '<END>'

class Lexicon:

	def __init__(self):
		self.root = LexNode(START)

	def addWord(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.hasNext(letter):
				curr = curr.getNext(letter)
			else:
				newNode = LexNode(letter)
				curr.addNext(newNode)
				curr = newNode
		endNode = LexNode(END)
		curr.addNext(endNodes)

	def hasWord(self, word):

	def beginsWith(self, word):