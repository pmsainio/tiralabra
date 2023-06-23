# Trie-tietorakenteessa syötedata tallennetaan merkki / alkio kerrallaan puuhun siten,
# että seuraava alkio on aina edellisen lapsi. Itse lapsisolmu ei saa mitään arvoa, vaan
# sen indeksi kertoo meille tarvittavan tiedon. Eri syötteet tallentuvat siis eri poluiksi
# juurisolmusta lähtien.

class TrieNode:  # puun solmu
    def __init__(self):
        self.children = [None for _ in range(25)]  # solmun jälkeläiset
        self.weight = 0  # solmun oma painoarvo


class Trie:
    # Alustetaan puu juurisolmulla. Oksista tulee halutun Markovin kejun pituiset.
    def __init__(self, degree):
        self.root = TrieNode()
        self.degree = degree

    def insert(self, tune):
        # Syötetään oppimisdata pätkittäin puuhun. Joka alkiosta lähtien tallennetaan uusi pätkä.
        for i in range(len(tune)):
            node = self.root
            subtune = tune[i:i+self.degree+1]
            for note in subtune:
                if node.children[note] is None:
                    node.children[note] = TrieNode()
                node = node.children[note]
                node.weight += 1

    def get(self, key):
        # Haetaan annetun polun päästä löytyvien solmujen indeksit ja niiden painot.
        if len(key) > self.degree:
            raise ValueError(
                f"Key must be shorter than degree. Current degree is {self.degree}.")  # polku ei voi olla pidempi kuin puun oksat

        children = []
        c_weights = []
        node = self.root
        for i in key:
            node = node.children[i]
            if node is None:
                print("The tree ran into a dead end. No worries.")
                return children, c_weights
        for j in range(25):
            if node.children[j] is not None:
                children.append(j)
                c_weights.append(node.children[j].weight)

        return children, c_weights
