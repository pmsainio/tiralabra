# Toteutusraportti

### Nykytoteutus
Ohjelma koostuu kolmesta moduulista ja pääohjelmasta:
- Trie-tietorakenne, johon varastoidaan opetusdata. Kunkin solmun lapsen indeksi määrittää seuraavan sävelen sävelkorkeuden. Lisäksi puussa pidetään karttaa kunkin solmun painosta.
- Markov-niminen moduuli, jolla generoidaan Markovin ketjua hyödyntäen uutta sävelmää. Solmujen lapset ja painot antavat vaihtoehdot, joista uusi sävel arvotaan.
- Midi-moduuli, jossa on funktiot opetusdatan käsittelyyn sekä ohjelman tulosteen (= uuden sävelmän) muuttamiseen tiedostoksi.
- Pääohjelma, jonne annetaan  parametrit:
  - puun syvyys eli Markovin ketjun aste
  - halutun sävelmän pituus nuottien määränä

Opetusdatan lukeminen, puun rakentaminen, uuden sävelmän generoiminen sekä tiedoston kirjoittaminen hoidetaan main-ohjelman kautta. Kyseinen tiedosto toimii myös ohjelman käyttöliittymänä. Trien aika- ja tilavaativuus on O(n).

Lisäksi rakenteeseen kuuluu oleellisesti opetusdatalle ja generoiduille sävelmille tarkoitetut kansiot.

### Kehittämiskohteita
Ohjelmassa on seuraavia puutteita / rajoitteita:
- Koodissa ei huomioida opetusdatan rytmiä. Nykyiselle opetusdatalle on tyylinmukaista, että melodia koostuu perättäisistä kahdeksasosanuoteista, jolloin tämä rajoite voi muodostaa ongelmia sitten, kun opetusdatana käytetään jotain muuta kuin kansanmusiikkia.
- Ohjelmasta voisi ehkä tehdä helppokäyttöisemmän, mikäli siinä olisi mukana käyttöliittymä. Omaan yksityiseen käyttööni tämä ei vaikuta.


Lähteet:

https://en.wikipedia.org/wiki/Trie
