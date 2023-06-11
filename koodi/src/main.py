from trie import Trie
import midi_parser as mp
import random

"""Ohjelmalla ei toistaiseksi ole omaa käyttöliittymää, vaan koodia mukautetaan omiin tarpeisiin sopivaksi."""

# Haluttu Markovin ketjun aste, n = 6:sta alkaen algoritmi ei tuota juurikaan uusia sävelmiä.
n = 4
l = 20  # Halutun sävelmän pituus
trie = Trie(n)

# Training data / midi -kansioon on laitettu opetusdataa, jonka ohjelma paikantaa tiedoston nimen perusteella.
# Tiedostot on normalisoitu siten, että niiden sävellaji on C tai a, ja ääniala on g--g^2 (tai g3--g5).
# Ainakin fuksiläppäri osaa avata .mid-tiedostot sellaisenaan, mikäli kappaleita haluaa kuunnella ensin itse.

training_data = [mp.extract_pitches("Lemmennosto.mid"),
                 mp.extract_pitches("Matalii ja mustii.mid"),
                 mp.extract_pitches("Pihi neito.mid"),
                 mp.extract_pitches("Riena.mid"),
                 mp.extract_pitches("Ruhverikko.mid"),
                 mp.extract_pitches("Tantsu.mid")]

for tune in training_data:
    trie.insert(tune)

print("\n Yleiskatsaus syötedatasta:\n",
      trie.get([])[0], "\n", trie.get([])[1], "\n")

# Luodaan uusi sävelmä nuotti kerrallaan. Silmukassa seurataan aina yhtä puun oksista, ja otetaan huomioon n edellistä sävelmään tullutta nuottia.
new_tune = []
i = 0
key = []
while len(new_tune) != l:
    for j in range(n):
        note = random.choices(
            trie.get(new_tune[-n:])[0], trie.get(new_tune[-n:])[1], k=1)[0]
        new_tune.append(note)
        if j == n-1 or len(new_tune) == l:
            break

print("uusi sävelmä: ", new_tune)

mp.write_midi_file("Markovin melodia #n", new_tune)
