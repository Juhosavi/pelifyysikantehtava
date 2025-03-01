import matplotlib.pyplot as plt
from math import sin, cos, radians

# Fysiikka-asetukset
g = 9.81  # Painovoima (m/s^2), tällä hetkellä pois päältä
dt = 0.1  # Aikaväli (s)

# Alkuarvot
xlist = [0.0]  # Alku x-koordinaatti
ylist = [4.0]  # Alku y-koordinaatti
v0 = 9.5  # Alku nopeus (m/s)
kulma = radians(60)  # Kulma radiaaneina
vx = v0 * cos(kulma)  # Nopeuden x-komponentti
vya = v0 * sin(kulma)  # Nopeuden y-komponentti

# X-raja, johon asti piirretään (m)
plot_raja_x = 10
plot_raja_y = -2

# Lasketaan pisteet lentoradalle
while True:
    vyl = vya - g * dt  # Päivitetään y-nopeus
    seuraava_x = xlist[-1] + vx * dt  # Seuraava x-koordinaatti
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt  # Seuraava y-koordinaatti

    if seuraava_x >= plot_raja_x or seuraava_y <= plot_raja_y:  # Lopetetaan, jos x ylittää rajan mihin
        # asti haluttiin piirtää, tai y alittaa rajan -2
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl  # Päivitetään y-nopeus seuraavalle kierrokselle

# Kolmion pisteet (suhteelliset koordinaatit)
kolmion_pisteet = [
    (-1, 1),  # Ylä
    (-1, -1),  # Ala
    (1, 0)  # Oikea
]

# Piirretään kolmio jokaiselle pisteelle
for x, y in zip(xlist, ylist):
    kolmion_koordinaatit = [(x + px, y + py) for px, py in kolmion_pisteet]
    kolmion_koordinaatit.append(kolmion_koordinaatit[0])  # Suljetaan kolmio yhdistämällä
    # alku- ja loppupiste

    # Piirretään kolmio
    kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*kolmion_koordinaatit)
    plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

# Asetetaan kiinteät koordinaatiston rajat
plt.xlim(-2, 14)
plt.ylim(-2, 10)

# Näytetään kuvaaja
plt.show()
