# The goal here is to filter objects into one of 6 categories
# based on galactic (l,b) position
# a) |b| > 5, > 20 radius around (l,b) = (0,0), and not in LMC/SMC
# b) |b| < 5, > 20 radius around (l,b) = (0,0), and not in LMC/SMC, |l| < 90
# c) |b| < 5, > 20 radius around (l,b) = (0,0), and not in LMC/SMC, |l| > 90
# d) 10 < r_GC < 20
# e) 3 < r_GC < 10
# f) r_GC < 3

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd 

# galactic positions of the LMC and SMC so that I can mask them out
lmc_gal = {"glon": 280.46539559 - 360, "glat": -32.88924276}
smc_gal = {"glon": 302.79695857 - 360, "glat": -44.29929833}

def switchboard(df):
    # need to center the galactic longitude at zero, going from -180 to 180
    df.glon[df.glon > 180] = df.glon[df.glon > 180] - 360

    # add column for galacto-centric radius
    df["r_GC"] = np.sqrt((df.glon)**2 + (df.glat)**2)

    # add column for lmc/smc-centric radius for creating the magellanic mask
    df["r_lmc"] = np.sqrt((df.glon - lmc_gal["glon"])**2 + (df.glat - lmc_gal["glat"])**2)
    df["r_smc"] = np.sqrt((df.glon - smc_gal["glon"])**2 + (df.glat - smc_gal["glat"])**2)

    # mask the clouds
    magellanic_mask = (df.r_lmc < 10) | (df.r_smc < 5)
    df = df[~magellanic_mask]

    # add column for specifying which region each object belongs to, 0-5 = a-f
    df["region"] = np.zeros(len(df))

    # assign regions
    df.region[(abs(df.glat) > 5) &  (df.r_GC > 20)] = 0
    df.region[(abs(df.glat) < 5) &  (df.r_GC > 20) & (abs(df.glon) < 90)] = 1
    df.region[(abs(df.glat) < 5) &  (df.r_GC > 20) & (abs(df.glon) > 90)] = 2
    df.region[(df.r_GC < 20) & (df.r_GC > 10)] = 3
    df.region[(df.r_GC < 10) & (df.r_GC > 3)] = 4
    df.region[(df.r_GC < 3)] = 5

    return df

ras = np.arange(0, 360, 10)
regions = np.arange(0, 6, 1)
obj_dir = "/Users/Nick/Documents/AGBstuff/new_work/agb_candidates/"

data = switchboard(pd.read_csv(obj_dir + "candidates_ra_0_10.dat", sep=","))
for ii in range(1, len(ras)):
    d = switchboard(pd.read_csv(obj_dir + "candidates_ra_{0}_{1}.dat".format(ras[ii], ras[ii]+10), sep=","))
    data = pd.concat((data, d))

for reg in regions:
    data[data["region"] == reg].to_csv(obj_dir + "candidates_region_{0}.dat".format(reg), sep=",", index=False)

print("All files read and partitioned")
# plt.scatter(data.ra[data.region == 0], data.decl[data.region == 0], s=1, edgecolor="None", c='k')
# plt.scatter(data.ra[data.region == 1], data.decl[data.region == 1], s=1, edgecolor="None", c='r')
# plt.scatter(data.ra[data.region == 2], data.decl[data.region == 2], s=1, edgecolor="None", c='g')
# plt.scatter(data.ra[data.region == 3], data.decl[data.region == 3], s=1, edgecolor="None", c='b')
# plt.scatter(data.ra[data.region == 4], data.decl[data.region == 4], s=1, edgecolor="None", c='orange')
# plt.scatter(data.ra[data.region == 5], data.decl[data.region == 5], s=1, edgecolor="None", c='purple')
# plt.xlim(-180,180)
# plt.ylim(-90,90)
# plt.show()
