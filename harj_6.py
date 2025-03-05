import matplotlib.pyplot as plt
from math import sin, cos, radians

# Fysiikka-asetukset
g = 9.81  # Painovoima (m/s^2)
dt = 0.1  # Aikaväli (s)
massa = 1.0  # Kolmion massa (kg)

# Hitausmomentti kolmion ympäri (J = m * sivun_pituus^2 / 6
sivun_pituus = 2.0  # Kolmion sivun pituus
J = massa * (sivun_pituus ** 2) / 6

# Alkuarvot
xlist = [0.0]  # Alku x-koordinaatti
ylist = [4.0]  # Alku y-koordinaatti
v0 = 8  # Alku nopeus (m/s)
kulma = radians(40)  # Kulma radiaaneina
vx = v0 * cos(kulma)  # Nopeuden x-komponentti
vya = v0 * sin(kulma)  # Nopeuden y-komponentti

# Alkuarvot kulmanopeudelle ja kulmakiihtyvyydelle
kulmanopeus = 2.0  # Kulmanopeus (rad/s)
kulmakiihtyvyys = 0.0  # Kulmakiihtyvyys (rad/s^2)

# Janan määrittely (pisteet (-2, -1) ja (15, 1))
jana_p1 = (-2, -1)
jana_p2 = (15, 1)

def piste_janan_alla(x, y, p1, p2):
    """Tarkistaa, onko piste (x, y) janan alapuolella."""
    # Janan yhtälö: y = kx + b
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - k * p1[0]
    return y < k * x + b

# Lasketaan pisteet lentoradalle
while True:
    # Kiihtyvyydet (vain painovoima vaikuttaa)
    ax = 0
    ay = -g

    # Päivitetään nopeudet
    vx += ax * dt
    vyl = vya + ay * dt

    # Seuraavat koordinaatit
    seuraava_x = xlist[-1] + vx * dt
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt

    # Lopetetaan, jos kolmio osuu janaan
    if piste_janan_alla(seuraava_x, seuraava_y, jana_p1, jana_p2):
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl

    # Päivitetään kulmanopeus (momentti = 0, joten kulmanopeus ei muutu ilman ulkoista voimaa)
    kulmanopeus += kulmakiihtyvyys * dt

# Kolmion pisteet (suhteelliset koordinaatit)
kolmion_pisteet = [
    (-1, 1),  # Ylä
    (-1, -1),  # Ala
    (1, 0)  # Oikea
]

# Piirretään kolmio jokaiselle pisteelle
for i, (x, y) in enumerate(zip(xlist, ylist)):
    liikekulmapisteet = [(x + px, y + py) for px, py in kolmion_pisteet]
    theta = kulmanopeus * i * dt
    pyorityskulmapisteet = []

    for px, py in liikekulmapisteet:
        new_x = x + (px - x) * cos(theta) - (py - y) * sin(theta)
        new_y = y + (px - x) * sin(theta) + (py - y) * cos(theta)
        pyorityskulmapisteet.append((new_x, new_y))

    pyorityskulmapisteet.append(pyorityskulmapisteet[0])
    kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*pyorityskulmapisteet)
    plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

# Piirretään jana
plt.plot([jana_p1[0], jana_p2[0]], [jana_p1[1], jana_p2[1]], color='red')

plt.xlim(-2, 15)
plt.ylim(-2, 10)
plt.show()
