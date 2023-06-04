class TrieNode:  # puun solmu
    def __init__(self):
        self.children = [None for _ in range(25)]  # solmun jälkeläiset
        self.weight = 0  # solmun oma painoarvo TODO


class Trie:
    # Alustetaan puu juurisolmulla. Oksista tulee halutun Markovin kejun pituiset.
    def __init__(self, degree):
        self.root = TrieNode()
        self.degree = degree

    def insert(self, tune):
        for i in range(len(tune)):
            node = self.root
            # syötetään oppimisdata pätkittäin
            subtune = tune[i:i+self.degree+1]
            # print("inserting subtune ", subtune)
            for note in subtune:
                if node.children[note] is None:
                    # uusista arvoista muodostuu uudet solmut
                    node.children[note] = TrieNode()
                # osasyötteen seuraavasta arvosta tulee edellisen jälkeläinen
                node = node.children[note]
                node.weight += 1  # TODO

    def get(self, key):
        if len(key) > self.degree:
            raise ValueError(
                f"Key must be shorter than degree. Current degree is {self.degree}.")  # polku ei voi olla pidempi kuin puun oksat

        children = []
        c_weights = []
        node = self.root
        for i in key:
            node = node.children[i]
            if node is None:
                return children  # Olematon polku palauttaa tyhjän listan.
        for j in range(25):
            if node.children[j] is not None:  # Haetaan kaikki solmun jälkeläiset
                children.append(j)
                c_weights.append(node.children[j].weight)

        return children, c_weights

    def get_weights(self, node: TrieNode):
        pass
