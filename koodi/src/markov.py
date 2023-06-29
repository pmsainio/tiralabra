from trie import Trie
import random

new_tune = []


def markov(trie: Trie, n, l, key_empty=False):
    while len(new_tune) != l:
        for j in range(n):
            key = trie.get(new_tune[-n:])
            if key != ([], []):
                note = random.choices(
                    key[0], key[1], k=1)[0]
                new_tune.append(note)
            else:
                key_empty = True
                print(
                    "Algoritmi ajautui umpikujaan, joten sävelmä jäi vajaamittaiseksi. Ei hätää.")
                break
            if j == n-1 or len(new_tune) == l:
                break
        if key_empty:
            break
    return new_tune
