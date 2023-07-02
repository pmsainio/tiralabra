# Testausdokumentti

ohjelman yksikkötestit on mahdollista suorittaa Poetryn avulla. Ensin on asennettava Poetry kansion *koodi* sisällä
.
```bash
poetry install
```
Testien suoritus onnistuu ajamalla seuraava komento koodi-kansiossa virtuaaliympäristössä
```bash
pytest
```
Testikattavuusraportin saa luotua komennolla
```bash
coverage html
```

### Yksikkötesteistä

Trie-tietorakenteen testaaminen yksikkötestein oli mutkatonta. Rakenne ei vaadi muuta kuin setterin ja getterin, ja näiden ollessa kunnossa pystyi testaamaan myös virhetilanteita ja solmujen painojen kasvua. Syystä, jota en osaa selittää, getterin testi ei raportin mukaan kata getterin toimintaa, mikä hämmentää minua. Joka tapauksessa manuaalisten testausten myötä olen kuitenkin satavarma, että getteri toimii halutulla tavalla.

### Manuaalisesta testauksesta

Markovin ketjun generoinnissa hyödynnettiin satunnaisuutta, joten yksikkötestejä oli mahdotonta alkaa rakentamaan. Heti juurisolmusta alkaen tehty arpominen johtaa väistämättä siihen, että mikäli juuresta lähtee edes kaksi oksaa, voi lopputulos vaihdella. Markovin ketjun toimintaa on siis tarkasteltu mm. välitulostusten avulla. Esimerkiksi, jos halutaan luoda kolmannen asteen ketjua, ja sävelmän viimeiset kolme säveltä ovat [3, 3, 2], on mahdollista varmistaa, että funktion käyttämä avain on [3, 3, 2]. Mikäli haku puusta avaimella [3, 3, 2] antaa lapset [1, 2, 3], on mahdollista varmistaa, että uuteen sävelmään seuraavaksi valittu sävel on joku näistä.

Lisäksi koodissa on mahdollista törmätä virhetilanteeseen, jossa hakuavain vie jollekin puun lehdistä, eikä hakureitin päässä olevalla solmulla näin ollen ole enää jälkeläisiä. Näin voi käydä esimerkiksi, kun syötetyn opetusdatan loppuosa ja avain täsmäävät. Tällaisia virhetilanteita varten tehtyjä ilmoituksia on testattu ajamalla koodia, kunnes virhetilanne tulee uudestaan vastaan.

### Testaus koodin ulkopuolella

Jonkin verran varmistusta ohjelman toiminnan oikeellisuudesta olen tehnyt myös korvakuulolta. Esimerkiksi asettaessa ketjun asteeksi riittävän korkean luvun (kuten 7) olen voinut todeta, että ohjelma toisintaa yksi yhteen jotakin tiettyä opetustadana annettua sävelmää. Pienemmällä asteluvulla puolestaan on voinut huomata generoidun sävelmän olevan satunnaisempi, vaikka syötteenä olisi ollut vain yksi opetusdatana annettavista sävelmistä.

Opetusdatan ja kirjoitettujen tiedostojen vertailun yhteydessä olen myös voinut todeta midi-toiminnallisuuksien eli tiedostojen lukemisen ja kirjoittamisen toimivan virheettömästi.
