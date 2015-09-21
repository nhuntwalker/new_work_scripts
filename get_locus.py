import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from thesiscode.plotting import *

# # load locus from jim's paper; output a comprehensive file
# columns1 = ["colgi", "N", "colug", "sigug", "colgr", "siggr", "colri", "sigri", "coliz", "sigiz", "colzj", "sigzj", "coljh", "sigjh", "colhk", "sighk"]
# f1 = open("../contaminants/davenportetal14_tbl1.txt").readlines()
# locus1 = {}
# for col in columns1:
#     locus1[col] = []

# for line in f1:
#     splitit = line.split()
#     for ii in range(len(splitit)):
#         locus1[columns1[ii]].append(splitit[ii])

# locus1 = pd.DataFrame(locus1, dtype=float)
# locus1["coljk"] = locus1.coljh + locus1.colhk
# locus1["sigjk"] = np.sqrt((locus1.sigjh)**2 + (locus1.sighk)**2)

# columns2 = ["colgi", "N", "colk1", "sigk1", "col12", "sig12", "Nw3", "col23", "sig23"]
# f2 = open("../contaminants/davenportetal14_tbl2.txt").readlines()
# locus2= {}
# for col in columns2:
#     locus2[col] = []

# for line in f2:
#     splitit = line.split()
#     for ii in range(len(splitit)):
#         locus2[columns2[ii]].append(splitit[ii])

# locus2 = pd.DataFrame(locus2, dtype=float)
# locus2.drop(labels=["N", "colgi"], axis=1, inplace=True)

# locus = pd.concat((locus1, locus2), axis=1)

# # output full locus
# locus.to_csv("../contaminants/davenport14_full_locus.txt", sep=",", index=False)

# load full locus
locus = pd.read_csv("../contaminants/davenport14_full_locus.txt", sep=",")
locus = locus[locus.col12 >= -0.01]
locus.sort(columns="col12", inplace=True)
locus.reset_index(inplace=True)

# load wise objects from direction of LMC
allwise = pd.read_csv("../contaminants/allwise_lmc_cut.dat", sep="\t")
lmc = (allwise.glon < 284) & (allwise.glon > 276.5) & (allwise.glat > -38.2) & (allwise.glat < -28)
allwise = allwise[lmc]
# cut = (allwise.n2mass == 1) & (allwise.w1err < 0.05) & (allwise.w2err < 0.1) & (allwise.w3err < 0.2) & (allwise.jerr < 0.1) & (allwise.kerr < 0.1)
# allwise = allwise[cut]
# cut = allwise.ccflag.str.extract("([000.])").replace("0", True).fillna(False)
# allwise = allwise[cut]
allwise["coljk"] = allwise.jmag - allwise.kmag
allwise["col12"] = allwise.w1 - allwise.w2
allwise["col23"] = allwise.w2 - allwise.w3

coeffs1 = np.polyfit(locus.col12, locus.coljk - locus.sigjk*3, deg=3)
coeffs2 = np.polyfit(locus.col12, locus.coljk + locus.sigjk*3, deg=3)

print coeffs1
print coeffs2

x = locus.col12
loc_cut = (allwise.coljk < coeffs2[3] + coeffs2[2]*allwise.col12 + coeffs2[1]*allwise.col12**2 + coeffs2[0]*allwise.col12**3) & (allwise.coljk > coeffs1[3] + coeffs1[2]*allwise.col12 + coeffs1[1]*allwise.col12**2 + coeffs1[0]*allwise.col12**3)

fig = plt.figure(figsize=(4,4))
fig.subplots_adjust(wspace=0.25, hspace=0.25, left=0.12, right=0.97, top=0.97, bottom=0.1)
ax = plt.subplot(111)
# ax.plot(locus.col12, locus.coljk + locus.sigjk*2, color='r')
ax.scatter(allwise.col12[loc_cut], allwise.coljk[loc_cut], s=5, edgecolor="None", c='k')
ax.plot(x, locus.coljk, color='b', linewidth=2)
ax.plot(x, locus.coljk + locus.sigjk*3, color='r', linewidth=2)
ax.plot(x, locus.coljk - locus.sigjk*3, color='r', linewidth=2)
ax.minorticks_on()
ax.set_ylim(0.25,1.8)
ax.set_xlim(-0.15, 0.4)
ax.set_xlabel("W1 - W2")
ax.set_ylabel("J - K$_s$")
plt.savefig("../figures/lmc_locus_3sig.png")
plt.show()

allwise[loc_cut].to_csv("../contaminants/allwise_lmc_locus.dat", sep=",", index=False)





