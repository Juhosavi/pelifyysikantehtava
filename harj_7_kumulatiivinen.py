import matplotlib.pyplot as plt
from math import sin, cos, radians

# Fysiikka-asetukset
g = 9.81  # Painovoima (m/s^2)
m = 0.1  # Massa (kg)
J = 0.04  # Hitausmomentti (kgm^2)
e = 1  # Sysäyskerroin
dt = 0.06# Aikaväli (s)

# Alkuarvot
xlist = [0.0]  # Alku x-koordinaatti
ylist = [4.0]  # Alku y-koordinaatti
v0 = 9  # Alkunopeus (m/s)
kulma = radians(55)  # Kulma asteina
vx = v0 * cos(kulma)  # Nopeuden x-komponentti
vya = v0 * sin(kulma)  # Nopeuden y-komponentti

# Janan määrittely
jana_p1 = (-2, 0)
jana_p2 = (15, 0)

# Pyörimisen nopeus
w = -3.0  # Kulmanopeus alussa (rad/s)
kulman_kasvu = 0  # Kumulatiivinen kulma

# Kolmion pisteet (suhteelliset koordinaatit)
kolmion_pisteet = [
    (-1, 1),
    (-1, -1),
    (1, 0)
]

#  alustetaan listat
tormayskohta = []
kulmapisteet = []
uudet_kulmapisteet = []

while True:
    vyl = vya - g * dt  # Päivitetään y-nopeus, johon vaikuttaa painovoima
    seuraava_x = xlist[-1] + vx * dt
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt

    kulmapisteet = [(xlist[-1] + px, ylist[-1] + py) for px, py in kolmion_pisteet]

    # Kumulatiivinen kulma
    kulman_kasvu += w * dt
    uudet_kulmapisteet = []

    for px, py in kulmapisteet:  # lasketaan uudet kierrot
        x_pisteen_kierto = (px - xlist[-1]) * cos(kulman_kasvu) - (py - ylist[-1]) * sin(kulman_kasvu)
        y_pisteen_kierto = (px - xlist[-1]) * sin(kulman_kasvu) + (py - ylist[-1]) * cos(kulman_kasvu)
        karjen_uusi_x = xlist[-1] + x_pisteen_kierto
        karjen_uusi_y = ylist[-1] + y_pisteen_kierto
        uudet_kulmapisteet.append((karjen_uusi_x, karjen_uusi_y))

        if karjen_uusi_y <= 0: # jos kärjen y-koordinaatti on 0 tai alle sen, se on kärki joka törmää janaan
            tormayskohta = karjen_uusi_x, 0.0 # tallennetaan törmäyspisteen sijainti (y = 0 koska jana on 0:ssa)

    uudet_kulmapisteet.append(uudet_kulmapisteet[0])
    kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*uudet_kulmapisteet)
    plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

    if tormayskohta:
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl

# Päivitetään arvot törmäyksen jälkeen (kaavalapun kaavoista)
tormaus_x, tormaus_y = tormayskohta
rP = tormaus_x - xlist[-1], tormaus_y - ylist[-1]
w_x_rP = 0 - w * rP[1], (0 - w * rP[0]) * -1
rP_x_n = rP[0] * -1 - 0
VP = vx + w_x_rP[0], vyl + w_x_rP[1]
VP_n = VP[0] * 0, VP[1] * -1
VP_n = VP_n[1]
Impulssi = -1 * (1 + e) * (VP_n / (1 / m + ((rP_x_n ** 2) / J)))
vya = vya + (Impulssi / m * -1)
w = w + (Impulssi / J * rP_x_n)

# Uusi simulaatio törmäyksen jälkeen
x_last = xlist[-1]
y_last = ylist[-1]  # talletetaan viimeisen kolmion x ja y

kulman_kasvu += w * dt

xlist = [] # tyhjennetään vanhoista arvoista
ylist = []
xlist.append(x_last) # lisätään viimeisin vanha arvo takaisin
ylist.append(y_last)

uudet_pisteet = []

i = 1 # tallennetaan viimeisen kolmion kulmapisteet ennen törmäystä, joista jatketaan
while i < len(uudet_kulmapisteet):
    j = uudet_kulmapisteet[i][0] - x_last, uudet_kulmapisteet[i][1] - y_last
    uudet_pisteet.append(j)
    i += 1

while True: # törmäyksen jälkeinen liikerata ja pyöriminen
    vyl = vya - g * dt
    seuraava_x = xlist[-1] + vx * dt
    seuraava_y = ylist[-1] + (vya + vyl) / 2 * dt

    kulmapisteet = [(xlist[-1] + px, ylist[-1] + py) for px, py in uudet_pisteet]
    kulman_kasvu += w * dt
    uudet_kulmapisteet = []

    for px, py in kulmapisteet:
        x_pisteen_kierto = (px - xlist[-1]) * cos(kulman_kasvu) - (py - ylist[-1]) * sin(kulman_kasvu)
        y_pisteen_kierto = (px - xlist[-1]) * sin(kulman_kasvu) + (py - ylist[-1]) * cos(kulman_kasvu)
        karjen_uusi_x = xlist[-1] + x_pisteen_kierto
        karjen_uusi_y = ylist[-1] + y_pisteen_kierto
        uudet_kulmapisteet.append((karjen_uusi_x, karjen_uusi_y))

    uudet_kulmapisteet.append(uudet_kulmapisteet[0])
    kolmion_x_koordinaatit, kolmion_y_koordinaatit = zip(*uudet_kulmapisteet)
    plt.plot(kolmion_x_koordinaatit, kolmion_y_koordinaatit, color='blue')

    if seuraava_x > 15: # lopetetaan tulostus kun mennään ulos koordinaatistosta
        break

    xlist.append(seuraava_x)
    ylist.append(seuraava_y)
    vya = vyl

plt.plot([jana_p1[0], jana_p2[0]], [jana_p1[1], jana_p2[1]], color='red')
plt.xlim(-2, 15)
plt.ylim(-2, 10)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()

