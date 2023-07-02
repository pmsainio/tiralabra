from trie import Trie
import midi_parser as mp
from markov import markov
from datetime import datetime

"""Ohjelmalla ei toistaiseksi ole omaa käyttöliittymää, vaan koodia mukautetaan omiin tarpeisiin sopivaksi."""

# Haluttu Markovin ketjun aste, n = 6:sta alkaen algoritmi ei tuota juurikaan uusia sävelmiä.
n = 3
l = 40  # Haluttu sävelmän pituus
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

new_tune = markov(trie, n, l)

print("uusi sävelmä: ", new_tune)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

mp.write_midi_file(f"Markovin melodia {timestamp}", new_tune)
