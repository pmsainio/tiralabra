# Toteutusraportti

### Nykytoteutus
Ohjelma koostuu kahdesta moduulista ja pääohjelmasta:
- Trie-tietorakenne, johon varastoidaan opetusdata. Kunkin solmun lapsen indeksi määrittää seuraavan sävelen sävelkorkeuden. Lisäksi puussa pidetään karttaa kunkin solmun painosta.
- Midi-moduuli, jossa on funktiot opetusdatan käsittelyyn sekä ohjelman tulosteen (= uuden sävelmän) muuttamiseen tiedostoksi.
- Pääohjelma, jossa opetusdata luetaan, ja jossa tuloste kasataan Trie-puun pohjalta.

Trien aika- ja tilavaativuus on O(n).

### Kehittämiskohteita
Ohjelmassa on seuraavia puutteita / rajoitteita:
- Koodissa ei huomioida opetusdatan rytmiä. Nykyiselle opetusdatalle on tyylinmukaista, että melodia koostuu perättäisistä kahdeksasosanuoteista, jolloin tämä rajoite voi muodostaa ongelmia sitten, kun opetusdatana käytetään jotain muuta kuin kansanmusiikkia.
- Ohjelmasta voisi tehdä helppokäyttöisemmän, mikäli siinä olisi mukana kjäyttöliittymä. Omaan yksityiseen käyttööni tämä ei vaikuta.


Lähteet:

https://en.wikipedia.org/wiki/Trie
