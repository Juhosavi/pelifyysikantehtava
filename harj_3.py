import matplotlib.pyplot as plt
from math import sin, cos, radians

# Fysiikka-asetukset
g = 0  # Painovoima (m/s^2), tällä hetkellä pois päältä
dt = 0.04  # Aikaväli (s)

# Alkuarvot
xlist = [0.0]  # Alku x-koordinaatti
ylist = [0.0]  # Alku y-koordinaatti
v0 = 20  # Alku nopeus (m/s)
kulma = radians(40)  # Kulma radiaaneina
vx = v0 * cos(kulma)  # Nopeuden x-komponentti
vya = v0 * sin(kulma)  # Nopeuden y-komponentti

# X-raja, johon asti piirretään (m)
plot_raja_x = 10

# Pyörimisen nopeus (rad/s)
angular_speed = -5  # Kulmanopeus (rad/s)

# Lasketaan pisteet lentoradalle
while True:
    vyl = vya - g * dt  # Päivitetään y-nopeus
    seuraava_x = xlist[-1] + vx * dt  # Seuraava x-koordinaatti
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt  # Seuraava y-koordinaatti

    if seuraava_x >= plot_raja_x:  # Lopetetaan, jos x ylittää rajan
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
for i, (x, y) in enumerate(zip(xlist, ylist)):
    # 1. Laske liikettä johtuvat kulmapisteet (liikutaan radalla)
    liikekulmapisteet = [(x + px, y + py) for px, py in kolmion_pisteet]

    # 2. Laske pyörimisestä johtuvat muutokset
    theta = angular_speed * i * dt  # Kulma, jolla kolmio pyörii
    pyorityskulmapisteet = []

    # Pyöritetään liikekulmapisteitä
    for px, py in liikekulmapisteet:
        # Siirretään piste (px, py) ja pyöritetään sitä
        new_x = x + (px - x) * cos(theta) - (py - y) * sin(theta)
        new_y = y + (px - x) * sin(theta) + (py - y) * cos(theta)
        pyorityskulmapisteet.append((new_x, new_y))

    pyorityskulmapisteet.append(pyorityskulmapisteet[0])  # Suljetaan kolmio yhdistämällä alku- ja loppupiste

    # Piirretään kolmio
    kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*pyorityskulmapisteet)
    plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

# Asetetaan kiinteät koordinaatiston rajat
plt.xlim(-2, 15)
plt.ylim(-2, 10)

# Näytetään kuvaaja
plt.show()
