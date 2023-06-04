# Markovin melodiat
Tavoitteena on Markovin ketjuja hyödyntämällä generoida lyhyitä sävelmiä. Syötteenä on tarkoitus toimia joukko MIDI-tiedostoja, jotka luetaan erillisestä kansiosta, ja joita analysoimalla ohjelma pystyisi replikoimaan tyylinmukaisia uusia sävelmiä. Toteutettavassa algoritmissa on pyrkimyksenä voida käyttää mielivaltaisen pituisia ketjuja. Ohjelma hyödyntää trie-tietorakennetta, koska se säästää tallennustilaa. Aikavaativuuden suhteen ei ole sen kummempia tehostamistavoitteita.

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
