# Testausdokumentti

ohjelman yksikkötestit on mahdollista suorittaa Poetryn avulla. Ensin on asennettava Poetry.
```bash
poetry install
```
Testien suoritus onnistuu ajamalla seuraava komento koodi-kansiossa virtuaaliympäristössä
```bash
coverage run --branch -m pytest src
```
(Huonosti formatoidun) testikattavuusraportin saaa komennolla
```bash
poetry run coverage xml
```


4.6.

Yksikkötestit on aloitettu. Trien setteri ja getteri toimivat kuten haluan. Toistaiseksi suurin osa testaamisesta on tapahtunut manuaalisesti, minkä jälkeen olen tehnyt tätä vastaavan yksikkötestin. Kattavuusraportti näyttää tällä hetkellä hirveältä, joten yritän tehdä sille jotain. Testaamatta on vielä ainakin vääränlaiset syötteet. Kunhan saan oikeanmuotoista opetusdataa, voisin yrittää testata tilanteita, joissa tietynlainen syöte pakottaa tietynlaiseen lopputulokseen. Lopullinen sovellus tulee hyödyntämään satunnaisuutta. Sen testaaminen tulee olemaan vaikeaa.
