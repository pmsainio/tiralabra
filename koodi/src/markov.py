from trie import Trie
import random

new_tune = []


def markov(trie: Trie, n, l, key_empty=False):
    while len(new_tune) != l:
        for j in range(n):
            # käytetään hakuavaimena uuden sävelmän n viimeistä alkiota
            key = trie.get(new_tune[-n:])
            # mikäli haku johtaa puun lehteen, puu on umpikujassa
            if key == ([], []) and len(new_tune) > 0:
                key_empty = True
                print(
                    "Algoritmi ajautui umpikujaan, joten sävelmä jäi vajaamittaiseksi. Ei hätää.")
                break
            else:
                note = random.choices(
                    key[0], key[1], k=1)[0]  # valitaan uusi sävel arpomalla vaihtoehdoista
                new_tune.append(note)
            if j == n-1 or len(new_tune) == l:
                break
        if key_empty:
            break
    return new_tune
