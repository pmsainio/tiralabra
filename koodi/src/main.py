from trie import Trie
import midi_parser as mp

"""Ohjelmalla ei toistaiseksi ole omaa käyttöliittymää, vaan koodia mukautetaan omiin tarpeisiin sopivaksi."""

trie = Trie(3)

# Training data -kansioon on laitettu opetusdataa, jonka ohjelma paikantaa tiedoston nimen perusteella. Lisää omasi, jos haluat.
training_data = [mp.extract_pitches("Lemmennosto.mid"),
                 mp.extract_pitches("Matalii ja mustii.mid"),
                 mp.extract_pitches("Pihi neito.mid"),
                 mp.extract_pitches("Riena.mid"),
                 mp.extract_pitches("Ruhverikko.mid"),
                 mp.extract_pitches("Tantsu.mid")]

for tune in training_data:
    trie.insert(tune)

# Tämä komento kertoo jokaisen käytetyn nuotin ja sen yleisyyden.
print(trie.get([]))
