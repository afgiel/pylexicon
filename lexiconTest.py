import lexicon

lexicon = lexicon.Lexicon()
lexicon.addWord('homeboy')
lexicon.addWord('AMAZING')
print lexicon.hasWord('homeboy')
print lexicon.beginsWith('home')
print not lexicon.hasWord('home')
print lexicon.hasWord('amazing')
print lexicon.beginsWith('ama')