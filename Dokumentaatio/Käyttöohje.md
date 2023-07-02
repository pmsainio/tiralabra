### Käyttöohje

Ennen ohjelman käyttöönottoa, varmista, että mido-kirjasto toimii esimkerkiksi asentamalla Poetryn riippuvuudet. Poetry on alustettu kansioon *koodi*.

```bash
poetry install
```

Ohjelmalla ei ole erillistä käyttöliittymää, vaan käyttäjän tai tilanteen vaatimiin tarpeisiin mukauttaminen tehdään vaihtamalla muuttujien lähtöarvoja ja syötettävää opetusdataa.

Olennaiset muuttujat:
- n, joka kuvastaa Markovin ketjun astetta (= sitä, miten pitkiä yhtenäisiä pätkiä opetudatasta ilmenee tulosteessa)
- l, joka kertoo, miten monta nuottia tulosteessa on

Näitä vaihelemalla saa jo erilaisia sävelmiä. Lisäksi käytettävää opetusdataa voi muuttaa halutessaan.

SRC-kansiossa on oma Training data -kansionsa, josta ohjelma hakee opetusdatan. Opetusdatana käytetään midi-tiedostoja. Tiedostot on normalisoitu siten, että sävellajina on C-duuri tai A-molli, ja sävelkorkeus on välillä G3--G5. (Klassisen musiikin termein tämä tarkoittaa väliä pienestä G:stä kaksiviivaiseen G:hen).

Valmiina oleva opetusdata sisältää kansanmusiikkiyhtye Värttinän levyttämiä sävelmiä. Koodissa voi jättää osan tiedostoista pois, tai lisätä uusia omia tiedostoja.

Kun koodin suorittaa, New tunes -kansioon ilmestyy uusi tiedosto nimeltään 'Markovin melodia #n'. Suositeltava tapa käyttää ohjelmaa on pitää auki erillistä ikkunaa, jossa tämä kansio on auki. Uuden tietoston ilmestyessä se on mahdollista avata ja kuunnella. (Ainakin fuksiläppäri kykenee avaamaan .mid-tiedoston ongelmitta.) Mikäli sävelmä miellyttää, voi sen nimetä uudelleen ja ottaa talteen.

Kuuntelun iloa!
