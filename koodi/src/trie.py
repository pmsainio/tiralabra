class TrieNode:  # puun solmu
    def __init__(self):
        self.children = {}  # solmun jälkeläiset
        self.weights = {}  # jälkeläisten painoarvo


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self, root):  # tämä ei toimi vielä
        root = self.root
        children = []
        for note, child in root.children.items():
            children.append(child)
        return str(root) + str(children)

    def insert(self, tune):  # haetaan testidatasta perättäiset alkiot ja asetetaan ne puuhun
        node = self.root
        for note in tune:
            if note not in node.children:
                node.children[note] = TrieNode()
                node.weights[note] = 1
            else:
                node.weights[note] += 1
            node = node.children[note]
