import sys
sys.path.append('../algorithms-project-69/search_engine')

from search_engine import search

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."
doc4 = "I can't shoot straight unless I've had a pint!"

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
    {'id': 'doc4', 'text': doc4},
]

# Теперь наш поиск может находить слова, независимо от знаков препинания
print(search(docs, 'pint'))  # ['doc1']
print(search(docs, 'pint!')) # ['doc1']