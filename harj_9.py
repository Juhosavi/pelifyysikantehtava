import matplotlib.pyplot as plt
from math import sin, cos, radians

# Fysiikka-asetukset
g = 0  # Painovoima (m/s^2), tällä hetkellä pois päältä
dt = 0.04  # Aikaväli (s)

# Alkuarvot
xlist_kolmio = [0.0]  # Alku x-koordinaatti
ylist_kolmio = [0.0]  # Alku y-koordinaatti
v0 = 20  # Alku nopeus (m/s) käytetään molemmissa monikulmioissa samaa alkunopeutta tällä hetkellä
kulma_kolmio = radians(40)  # Kulma radiaaneina
vx_kolmio = v0 * cos(kulma_kolmio)  # Nopeuden x-komponentti
vya_kolmio = v0 * sin(kulma_kolmio)  # Nopeuden y-komponentti

# X-raja, johon asti piirretään (m)
plot_raja_x = 10

xlist_nelio = [10.0]  # Alku x-koordinaatti
ylist_nelio = [0.0]  # Alku y-koordinaatti
kulma_nelio = radians(145)  # Kulma radiaaneina
vx_nelio = v0 * cos(kulma_nelio)  # Nopeuden x-komponentti
vya_nelio = v0 * sin(kulma_nelio)  # Nopeuden y-komponentti

# Pyörimisen nopeus (rad/s)
kulmanopeus_kolmio = -5  # Kulmanopeus (rad/s)
kulmanopeus_nelio = 5

# Lasketaan pisteet lentoradalle
while True:
    vyl_kolmio = vya_kolmio - g * dt  # Päivitetään y-nopeus
    vyl_nelio = vya_nelio - g * dt
    kolmio_seuraava_x = xlist_kolmio[-1] + vx_kolmio * dt  # Seuraava x-koordinaatti
    kolmio_seuraava_y = ylist_kolmio[-1] + (vya_kolmio + vyl_kolmio) / 2 * dt  # Seuraava y-koordinaatti

    nelio_seuraava_x = xlist_nelio[-1] + vx_nelio * dt
    nelio_seuraava_y = ylist_nelio[-1] + (vya_nelio + vyl_kolmio) / 2 * dt

    if kolmio_seuraava_x >= plot_raja_x:  # Lopetetaan, jos x ylittää rajan
        break

    xlist_kolmio.append(kolmio_seuraava_x)
    ylist_kolmio.append(kolmio_seuraava_y)

    xlist_nelio.append(nelio_seuraava_x)
    ylist_nelio.append(nelio_seuraava_y)
    vya_kolmio = vyl_kolmio  # Päivitetään y-nopeus seuraavalle kierrokselle
    vya_nelio = vyl_nelio



# Kolmion pisteet (suhteelliset koordinaatit)
kolmion_pisteet = [
    (-1, 1),  # Ylä
    (-1, -1),  # Ala
    (1, 0)  # Oikea
]

nelion_pisteet = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

# Piirretään kolmio jokaiselle pisteelle
for i, (x, y) in enumerate(zip(xlist_kolmio, ylist_kolmio)):
    # 1. Laske liikettä johtuvat kulmapisteet (liikutaan radalla)
    liikekulmapisteet = [(x + px, y + py) for px, py in kolmion_pisteet]

    # 2. Laske pyörimisestä johtuvat muutokset
    theta = kulmanopeus_kolmio * i * dt  # Kulma, jolla kolmio pyörii
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

for i, (x, y) in enumerate(zip(xlist_nelio, ylist_nelio)):
    # 1. Laske liikettä johtuvat kulmapisteet (liikutaan radalla)
    liikekulmapisteet = [(x + px, y + py) for px, py in nelion_pisteet]

    # 2. Laske pyörimisestä johtuvat muutokset
    theta = kulmanopeus_nelio * i * dt  # Kulma, jolla neliö pyörii
    pyorityskulmapisteet = []

    # Pyöritetään liikekulmapisteitä
    for px, py in liikekulmapisteet:
        # Siirretään piste (px, py) ja pyöritetään sitä
        new_x = x + (px - x) * cos(theta) - (py - y) * sin(theta)
        new_y = y + (px - x) * sin(theta) + (py - y) * cos(theta)
        pyorityskulmapisteet.append((new_x, new_y))

    pyorityskulmapisteet.append(pyorityskulmapisteet[0])  # Suljetaan yhdistämällä alku- ja loppupiste

    # Piirretään neliö
    nelion_x_koordinaatit, nelion_y_koordinaatit = zip(*pyorityskulmapisteet)
    plt.plot(nelion_x_koordinaatit, nelion_y_koordinaatit, color='red')

# Asetetaan kiinteät koordinaatiston rajat
plt.xlim(-5, 15)
plt.ylim(-2, 12)

# Näytetään kuvaaja
plt.show()