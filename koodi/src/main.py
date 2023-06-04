from trie import Trie

"""toistaiseksi tässä tiedostossa vain testaillaan toiminnallisuuksia"""

puu = Trie(3)

tune = [1, 2, 1, 3, 1, 4]
puu.insert(tune)
result = puu.get([1])
print(result)  # Output: [2, 3, 4]

result = puu.get([1, 2])
print(result)  # 1
result = puu.get([2, 3])
print(result)  # []

print("\n")

puu = Trie(1)
tune = [1, 2, 1, 3, 1, 4]
tune_2 = [1, 3, 1, 5, 1, 6, 1, 7]
tune_3 = [1, 3]
puu.insert(tune)
puu.insert(tune_2)
puu.insert(tune_3)

result = puu.get([1])
print(result)  # Output: [2, 3, 4, 5, 6, 7]
print("\n")
result = puu.get([1, 2])
print(result)  # Output: Error
