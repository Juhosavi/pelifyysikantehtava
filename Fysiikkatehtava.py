import matplotlib.pyplot as plt
import numpy as np

# Alkuperäiset kärkipisteet
pisteet0 = np.array([(0.1, 0), (0, 0.1), (-0.1, 0), (0, -0.1)])

# Massakeskipiste ja orientaatio
xcm = 0
ycm = 0
phi = 0
g = 9.81

#alkutilanne

vxcm = -1 # m/s
vycm = 2  # m/s
kulmanopeus = 5 # rad / s
dt = 0.2  #sekuntia
# Päivitetään uusi kulma ajan dt jälkeen
uusiphi = phi + kulmanopeus * dt

# Massa ja hitausmomentti
m = 1
j = 0.03

#kärkipiste lasku
x_uudet = pisteet0[:, 0] * np.cos(phi) - pisteet0[:, 1] * np.sin(phi) + xcm
y_uudet = pisteet0[:, 0] * np.sin(phi) + pisteet0[:, 1] * np.cos(phi) + ycm



vycm = vycm - g * dt

xcm = xcm + vxcm * dt
ycm = ycm + vycm * dt
phi = phi + kulmanopeus * dt

# Siirretään kärkipisteet massakeskipisteen sijainnin mukaan
xcords0, ycords0 = zip(*pisteet0)
xcords = [x + xcm for x in xcords0] + [xcords0[0] + xcm]
ycords = [y + ycm for y in ycords0] + [ycords0[0] + ycm]

# Piirretään monikulmio
plt.plot(xcords, ycords)
plt.grid()
plt.show()
