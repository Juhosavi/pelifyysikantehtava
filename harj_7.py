import matplotlib.pyplot as plt
from math import sin, cos, radians

"""GLOBAALIT MUUTTUJAT"""

# Fysiikka-asetukset
g = 9.81  # Painovoima (m/s^2), tällä hetkellä pois päältä
m = 0.2  # massa kg, ei vaikuta muuhun kuin törmäykseen, koska painovoima ainoa vaikuttava voima
J = 0.5  # hitausmomentti kgm^2
e = 1  # sysäyskerroin
dt = 0.1  # Aikaväli (s)

# Alkuarvot
xlist = [0.0]  # Alku x-koordinaatti
ylist = [4.0]  # Alku y-koordinaatti
v0 = 8  # Alkunopeus (m/s)
kulma = radians(55)  # Kulma asteina, joka muutetaan tässä radiaaneiksi radians-funktiolla
vx = v0 * cos(kulma)  # Nopeuden x-komponentti
vya = v0 * sin(kulma)  # Nopeuden y-komponentti

# Janan määrittely (pisteet (-2, -1) ja (15, 1))
jana_p1 = (-2, 0)
jana_p2 = (15, 0)

# X-raja, johon asti piirretään (m)
plot_raja_x = 15

# Pyörimisen nopeus (rad/s)
w = -0.8  # Kulmanopeus alussa (rad/s)

# Kolmion pisteet (suhteelliset koordinaatit)
kolmion_pisteet = [
    (-1, 1),
    (-1, -1),
    (1, 0)
    ]

tormayskohta = []
kulmapisteet = []
uudet_kulmapisteet = []

# Lasketaan kolmion CM-sijainteja ja lisätään ne listoihin niin kauan, kunnes annettu raja tulee vastaan
while True:
    vyl = vya - g * dt  # Päivitetään y-nopeus (tässä painovoima pois päältä, joten ei kuitenkaan muutu)
    seuraava_x = xlist[-1] + vx * dt  # Seuraava x-koordinaatti, lisätään edelliseen sijaintiin uusi sijainti ajanhetken dt kuluttua
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt  # Seuraava y-koordinaatti, lasketaan keskinopeus (alkunopeus+loppunopeus jaettuna 2)
    # ja sitten sen avulla lasketaan kuljettu matka, joka lisätään viimeiseen y-sijaintiin


    for i, (x, y) in enumerate(zip(xlist, ylist)):
        # uudet kulmapisteet ennen pyöritystä (liikutaan koordinaatistossa)
        kulmapisteet = [(x + px, y + py) for px, py in kolmion_pisteet]
        # eli lisätään myös kulmapisteiden #sijainneille aiemmassa loopissa lasketut kolmion uudet CM-sijainnit
        # koordinaatistossa ennen kuin pyöritetään pisteitä

        # pyörimisestä johtuvat muutokset
        theta = w * i * dt  # uusi kulma, jolla kolmio pyörii (kulmanopeus rad/s * deltatime = rad)
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

            if karjen_uusi_y <= 0:# tämä kohta tallentaa törmäävän kärjen sijainnin
                tormayskohta = karjen_uusi_x, karjen_uusi_y

        uudet_kulmapisteet.append(uudet_kulmapisteet[0])  # Suljetaan kolmio yhdistämällä alku- ja loppupiste

        # Piirretään kolmio
        kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*uudet_kulmapisteet)
        plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

    if tormayskohta:  # jos tormäyskohta-lista ei ole tyhjä, eli jokin kulma on törmännyt janaan
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl  # Päivitetään y:n alkunopeus silmukan seuraavalle kierrokselle


# seuraavaksi lasketaan törmäyksestä johtuvat muutokset

rP = tormayskohta[0] - xlist[-1], tormayskohta[1] - ylist[-1]
w_x_rP = 0 - w * rP[1], (0 - w * rP[0]) * -1
rP_x_n = rP[0] * -1 - 0

VP = vx + w_x_rP[0], vyl + w_x_rP[1]
VP_n = VP[0] * 0, VP[1] * -1  # m/s
VP_n = VP_n[1]

I = -1 * (1 + e) * (VP_n / (1/m + ((rP_x_n**2) / J)))  # törmäysimpulssin suuruus

vya = vya + (I/m * -1)
w = w + (I/J * rP_x_n)

print(w)


xlist_last = xlist[-1]
ylist_last = ylist[-1]

xlist = []
ylist = []

xlist.append(xlist_last)
ylist.append(ylist_last)
uudet_kulmapisteet2 = [uudet_kulmapisteet[0], uudet_kulmapisteet[1], uudet_kulmapisteet[2]]
print(uudet_kulmapisteet)
print(uudet_kulmapisteet2)



while True:
    vyl = vya - g * dt  # Päivitetään y-nopeus (tässä painovoima pois päältä, joten ei kuitenkaan muutu)
    seuraava_x = xlist[-1] + vx * dt  # Seuraava x-koordinaatti, lisätään edelliseen sijaintiin uusi sijainti ajanhetken dt kuluttua
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt  # Seuraava y-koordinaatti, lasketaan keskinopeus (alkunopeus+loppunopeus jaettuna 2)
    # ja sitten sen avulla lasketaan kuljettu matka, joka lisätään viimeiseen y-sijaintiin


    for i, (x, y) in enumerate(zip(xlist, ylist)):
        # uudet kulmapisteet ennen pyöritystä (liikutaan koordinaatistossa)
        kulmapisteet1 = [(x + px, y + py) for px, py in kolmion_pisteet]
        # eli lisätään myös kulmapisteiden #sijainneille aiemmassa loopissa lasketut kolmion uudet CM-sijainnit
        # koordinaatistossa ennen kuin pyöritetään pisteitä

        # pyörimisestä johtuvat muutokset
        theta = w * i * dt  # uusi kulma, jolla kolmio pyörii (kulmanopeus rad/s * deltatime = rad)
        uudet_kulmapisteet3 = []  # nollataan lista tässä vaiheessa ennen seuraavaa silmukkaa


        # Lasketaan uudessa sijainnissa olevan kolmion pisteiden pyöriminen
        for px, py in kulmapisteet1:
            # Siirretään piste (px, py) ja pyöritetään sitä
            x_pisteen_kierto = (px - x) * cos(theta) - (py - y) * sin(theta)  # (px - x) on tässä rpCM
            # eli CM:stä kärkeen kulkevan vektorin x-komponentti
            karjen_uusi_x = x + x_pisteen_kierto  # lisätään keskipisteen sijaintiin uusi pisteen kierto

            y_pisteen_kierto = (px - x) * sin(theta) + (py - y) * cos(theta)
            karjen_uusi_y = y + y_pisteen_kierto

            uudet_kulmapisteet3.append((karjen_uusi_x, karjen_uusi_y))

            if karjen_uusi_y <= 0:# tämä kohta tallentaa törmäävän kärjen sijainnin
                tormayskohta = karjen_uusi_x, karjen_uusi_y

        uudet_kulmapisteet3.append(uudet_kulmapisteet3[0])  # Suljetaan kolmio yhdistämällä alku- ja loppupiste

        # Piirretään kolmio
        kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*uudet_kulmapisteet3)
        plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

    if seuraava_x > 15:
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl  # Päivitetään y:n alkunopeus silmukan seuraavalle kierrokselle


# Piirretään jana
plt.plot([jana_p1[0], jana_p2[0]], [jana_p1[1], jana_p2[1]], color='red')

# Asetetaan kiinteät koordinaatiston rajat
plt.xlim(-2, 15)
plt.ylim(-2, 10)

plt.xlabel("x (m)")
plt.ylabel("y (m)")

# Näytetään kuvaaja
plt.show()