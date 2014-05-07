

class LexNode:

	def __init__(self, val):
		self.val = val
		self.out = dict()

	def addNext(self, next):
		if next.getVal().lower() not in self.out:
			self.out[next.getVal().lower()] = next

	def getNextVals(self):
		return self.out.keys()

	def getNextNode(self, val):
		return self.out[val.lower()]

	def inNext(self, val):
		return val.lower() in self.out

	def getVal(self):
		return self.val