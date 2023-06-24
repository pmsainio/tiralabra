from trie import Trie
import midi_parser as mp
import random
import datetime

"""Ohjelmalla ei toistaiseksi ole omaa käyttöliittymää, vaan koodia mukautetaan omiin tarpeisiin sopivaksi."""

# Haluttu Markovin ketjun aste, n = 6:sta alkaen algoritmi ei tuota juurikaan uusia sävelmiä.
n = 5
l = 20  # Haluttu sävelmän pituus
trie = Trie(n)

# Training data / midi -kansioon on laitettu opetusdataa, jonka ohjelma paikantaa tiedoston nimen perusteella.
# Tiedostot on normalisoitu siten, että niiden sävellaji on C tai a, ja ääniala on g--g^2 (tai g3--g5).
# Ainakin fuksiläppäri osaa avata .mid-tiedostot sellaisenaan, mikäli kappaleita haluaa kuunnella ensin itse.

training_data = [mp.extract_pitches("Lemmennosto.mid"),
                 mp.extract_pitches("Matalii ja mustii.mid"),
                 mp.extract_pitches("Pihi neito.mid"),
                 # mp.extract_pitches("Riena.mid"),
                 mp.extract_pitches("Ruhverikko.mid"),
                 mp.extract_pitches("Tantsu.mid")]

for tune in training_data:
    trie.insert(tune)

print("\n Yleiskatsaus syötedatasta:\n sävelet:",
      trie.get([])[0], "\n painot:", trie.get([])[1], "\n")

# Luodaan uusi sävelmä nuotti kerrallaan. Silmukassa seurataan aina yhtä puun oksista, ja otetaan huomioon n edellistä sävelmään tullutta nuottia.
new_tune = []
key_empty = False

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

print("uusi sävelmä: ", new_tune)

mp.write_midi_file(f"Markovin melodia {datetime.datetime.now()}", new_tune)
