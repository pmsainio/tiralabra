# Testausdokumentti

ohjelman yksikkötestit on mahdollista suorittaa Poetryn avulla. Ensin on asennettava Poetry.
```bash
poetry install
```
Testien suoritus onnistuu ajamalla seuraava komento koodi-kansiossa virtuaaliympäristössä
```bash
coverage run --branch -m pytest src
```
Testikattavuusraportin saa luotua komennolla
```bash
coverage html
```


#### 4.6.

Yksikkötestit on aloitettu. Trien setteri ja getteri toimivat kuten haluan. Toistaiseksi suurin osa testaamisesta on tapahtunut manuaalisesti, minkä jälkeen olen tehnyt tätä vastaavan yksikkötestin. Kattavuusraportti näyttää tällä hetkellä hirveältä, joten yritän tehdä sille jotain. Testaamatta on vielä ainakin vääränlaiset syötteet. Kunhan saan oikeanmuotoista opetusdataa, voisin yrittää testata tilanteita, joissa tietynlainen syöte pakottaa tietynlaiseen lopputulokseen. Lopullinen sovellus tulee hyödyntämään satunnaisuutta. Sen testaaminen tulee olemaan vaikeaa.

#### 24.6.

Testikattavuutta on laajennettu hieman. Tällä hetkellä testin kohteena on myös virhetilanteita, joita ei pitäisi sattua ohjelman normaalikäytössä, mutta minusta niiden on hyvä olla olemassa siltä varalta, että koodi muuttuu. Jotkut ongelmat, kuten puun päätyminen umpikujaan, ovat vaikeita testata yksikkötesteillä, sillä ne esiintyvät sattumanvaraisesti.
