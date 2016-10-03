# Aleks Diamond-Stanic
# 20161003
#
# The main goal of this code is to compile measurements of the cosmic
# baryon density and the cosmic stellar mass density to answer the
# following question: What fraction of baryons have formed stars by
# the present day?
#

import numpy as np
from astropy import units as u
from astropy import constants as const
from astropy.constants import G


# Planck 2013 results. XVI. Cosmological parameters
# http://adsabs.harvard.edu/abs/2014A&amp;A...571A..16P
# taking values from the abstract
omega_b_hsquared_planck = 0.02205
h_planck = 0.673
omega_b_planck = omega_b_hsquared_planck / h_planck**2
print('Omega_baryon(Planck)=', omega_b_planck)

# critial density
rho_crit = 3 * (h_planck * 100.* u.km / u.s / u.Mpc)**2 / (8. * np.pi * const.G)

# Bell et al. (2003), ApJS, 149, 289
# http://adsabs.harvard.edu/abs/2003ApJS..149..289B
# taking values from the abstract and from Table 4
omega_star_h = 2.e-3
omega_star_bell = omega_star_h / h_planck
rho_bell_gband = 5.47e8 * h_planck * const.M_sun / u.Mpc**3 # h Msun / Mpc**3
print('Omega_star(Bell)=', omega_star_bell, rho_bell_gband.cgs / rho_crit.cgs)

# Moustakas et al. (2013), ApJ, 767, 50 
# http://adsabs.harvard.edu/abs/2013ApJ...767...50M
# taking value from Section 5.1
# note: potential issues with h=0.7 vs h=0.673
rho_moustakas = 2.36e8 * const.M_sun / u.Mpc**3
print('Omega_star(Moustakas)=', rho_moustakas.cgs / rho_crit.cgs)

# What does this imply about the fraction of baryons that have formed stars?
star_frac = np.array([omega_star_bell, rho_bell_gband.cgs / rho_crit.cgs, rho_moustakas.cgs / rho_crit.cgs]) / omega_b_planck
print('Fraction of baryons that have formed stars: ', star_frac)


