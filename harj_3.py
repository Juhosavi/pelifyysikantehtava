import matplotlib.pyplot as plt
from math import sin, cos, radians

# Fysiikka-asetukset
g = 0  # Painovoima (m/s^2), tällä hetkellä pois päältä
dt = 0.2  # Aikaväli (s)

# Alkuarvot
xlist = [0.0]  # Alku x-koordinaatti
ylist = [0.0]  # Alku y-koordinaatti
v0 = 5  # Alku nopeus (m/s)
kulma = radians(40)  # Kulma asteina, joka muutetaan tässä radiaaneiksi radians-funktiolla
vx = v0 * cos(kulma)  # Nopeuden x-komponentti
vya = v0 * sin(kulma)  # Nopeuden y-komponentti

# X-raja, johon asti piirretään (m)
plot_raja_x = 10

# Pyörimisen nopeus (rad/s)
angular_speed = -1  # Kulmanopeus (rad/s)

# Lasketaan kolmion CM-sijainteja ja lisätään ne listoihin niin kauan, kunnes annettu raja tulee vastaan
while True:
    vyl = vya - g * dt  # Päivitetään y-nopeus (tässä painovoima pois päältä, joten ei kuitenkaan muutu)
    seuraava_x = xlist[-1] + vx * dt  # Seuraava x-koordinaatti, lisätään edelliseen sijaintiin uusi sijainti ajanhetken dt kuluttua
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt  # Seuraava y-koordinaatti, lasketaan keskinopeus (alkunopeus+loppunopeus jaettuna 2)
    # ja sitten sen avulla lasketaan kuljettu matka, joka lisätään viimeiseen y-sijaintiin

    if seuraava_x >= plot_raja_x:  # Lopetetaan kolmion uuden sijainnin laskeminen jos
        # kolmion keskipisteen uusi x-koordinaatti ylittää alussa määritellyn rajan
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl  # Päivitetään y:n alkunopeus silmukan seuraavalle kierrokselle

# Kolmion pisteet (suhteelliset koordinaatit)
kolmion_pisteet = [
    (-1, 1),  # Ylä
    (-1, -1),  # Ala
    (1, 0)  # Oikea
]

# lasketaan uudet kulmapisteet ja niiden kierrot
for i, (x, y) in enumerate(zip(xlist, ylist)):
    # uudet kulmapisteet ennen pyöritystä (liikutaan koordinaatistossa)
    kulmapisteet = [(x + px, y + py) for px, py in kolmion_pisteet]
    # eli lisätään myös kulmapisteiden #sijainneille aiemmassa loopissa lasketut kolmion uudet CM-sijainnit
    # koordinaatistossa ennen kuin pyöritetään pisteitä

    # pyörimisestä johtuvat muutokset
    theta = angular_speed * i * dt  # uusi kulma, jolla kolmio pyörii (kulmanopeus rad/s * deltatime = rad)
    uudet_kulmapisteet = []  # nollataan lista tässä vaiheessa ennen seuraavaa silmukkaa

    # Lasketaan uudessa sijainnissa olevan kolmion pisteiden pyöriminen
    for px, py in kulmapisteet:
        # Siirretään piste (px, py) ja pyöritetään sitä
        x_pisteen_kierto = (px - x) * cos(theta) - (py - y) * sin(theta)  # (px - x) on tässä rpCM
        # eli CM:stä kärkeen kulkevan vektorin x-komponentti
        karjen_uusi_x = x + x_pisteen_kierto  # lisätään keskipisteen sijaintiin uusi pisteen kierto

        y_pisteen_kierto = (px - x) * sin(theta) + (py - y) * cos(theta)
        karjen_uusi_y = y + y_pisteen_kierto

        uudet_kulmapisteet.append((karjen_uusi_x, karjen_uusi_y))

    uudet_kulmapisteet.append(uudet_kulmapisteet[0])  # Suljetaan kolmio yhdistämällä alku- ja loppupiste

    # Piirretään kolmio
    kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*uudet_kulmapisteet)
    plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

# Asetetaan kiinteät koordinaatiston rajat
plt.xlim(-2, 15)
plt.ylim(-2, 10)

plt.xlabel("x (m)")
plt.ylabel("y (m)")

# Näytetään kuvaaja
plt.show()
