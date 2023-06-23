# Markovin melodiat
Tavoitteena on Markovin ketjuja hyödyntämällä generoida lyhyitä sävelmiä. Syötteenä on tarkoitus toimia joukko MIDI-tiedostoja, jotka luetaan erillisestä kansiosta, ja joita analysoimalla ohjelma pystyisi replikoimaan tyylinmukaisia uusia sävelmiä. Toteutettavassa algoritmissa on pyrkimyksenä voida käyttää mielivaltaisen pituisia ketjuja. Ohjelma hyödyntää trie-tietorakennetta, koska se säästää tallennustilaa. Aikavaativuuden suhteen ei ole sen kummempia tehostamistavoitteita.

### Käyttöohje

Ennen ohjelman käyttöönottoa, varmista, että mido-kirjasto toimii esimkerkiksi asentamalla Poetryn riippuvuudet. Suorita alla mainittu komento koodi-kansiossa:

```bash
poetry install
```

Ohjelmalla ei toistaiseksi ole erillistä käyttöliittymää, vaan käyttäjän tai tilanteen vaatimiin tarpeisiin mukauttaminen tehdään vaihtamalla muuttujien lähtöarvoja ja syötettävää opetusdataa.

Olennaisimmat muuttujat:
- n, joka kuvastaa Markovin ketjun astetta (= sitä, miten pitkiä yhtenäisiä pätkiä opetudatasta ilmenee tulosteessa)
- l, joka kertoo, miten monta nuottia tulosteessa on

Näitä vaihelemalla saa jo erilaisia sävelmiä. Lisäksi käytettävää opetusdataa voi muuttaa halutessaan.

SRC-kansiossa on oma Training data -kansionsa, josta ohjelma hakee opetusdatan. Opetusdatana käytetään midi-tiedostoja. Tiedostot on normalisoitu siten, että sävellajina on C-duuri tai A-molli, ja sävelkorkeus on välillä G3--G5. (Klassisen musiikin termein tämä tarkoittaa väliä pienestä G:stä kaksiviivaiseen G:hen).

Valmiina oleva opetusdata sisältää kansanmusiikkiyhtye Värttinän levyttämiä sävelmiä. Koodissa voi jättää osan tiedostoista pois, tai lisätä uusia omia tiedostoja.

Kun koodin suorittaa, New tunes -kansioon ilmestyy uusi tiedosto nimeltään 'Markovin melodia #n'. Suositeltava tapa käyttää ohjelmaa on pitää auki erillistä ikkunaa, jossa tämä kansio on auki. Uuden tietoston ilmestyessä se on mahdollista avata ja kuunnella. (Ainakin fuksiläppäri kykenee avaamaan .mid-tiedoston ongelmitta.) Mikäli sävelmä miellyttää, voi sen nimetä uudelleen, jottei ohjelma seuraavalla suorituskerralla kirjoita sen päälle toista tiedostoa.

Kuuntelun iloa!

### Testaus
[![cov](https://pmsainio.github.io/tiralabra/badges/coverage.svg)](https://github.com/pmsainio/tiralabra/actions)

ohjelman yksikkötestit on mahdollista suorittaa Poetryn avulla. Ensin on asennettava Poetry.
```bash
poetry install
```
Testien suoritus onnistuu ajamalla seuraava komento koodi-kansiossa virtuaaliympäristössä
```bash
coverage run --branch -m pytest src
```

Koodin laadun voi tarkistaa komennolla
```bash
pylint src
```

### Tekijätietoja
Ohjelmakielenä käytän pythonia, koska se on ainoa, jota osaan sujuvasti matlabin ohella. Opiskelen tietojenkäsittelytieteen kandiohjelmassa. Projektin dokumentointi tapahtuu suomeksi.
