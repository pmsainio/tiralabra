from trie import Trie

"""toistaiseksi tässä tiedostossa vain testaillaan toiminnallisuuksia"""

puu = Trie()

puu.insert([1, 2, 1, 3, 1, 4, 1, 5])

print(puu.root.children.items())
