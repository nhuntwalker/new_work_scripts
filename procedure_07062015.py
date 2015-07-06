from thesiscode.plotting import Plot
from thesiscode.quality import Data, read_gator_2mass_matched, match_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'family' : 'normal',
        'size'   : 12}

matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10)
matplotlib.rcParams["ps.useafm"] = True
matplotlib.rcParams["pdf.use14corefonts"] = True
matplotlib.rcParams["text.usetex"] = True

## Match OGLE and 2MASS
ogle = pd.read_csv("../samples/ogle_table.dat", sep="|")
ogle_2mass = read_gator_2mass_matched("../samples/ogle_2mass_match.tbl", "2mass")
ogle_matched = Data(match_data(ogle, ogle_2mass))
ogle_matched.data["colvi"] = ogle_matched.data.V - ogle_matched.data.I

ogle_matched.data.Field[ogle_matched.data.glon > 290] = "smc"
ogle_matched.data.Field[ogle_matched.data.glon < 290] = "lmc"
lmc = ogle_matched.data.Field == "lmc"

ogle_matched.cut_me(lmc, cutstr="Selecting only LMC objects")
ogle_matched.cut_me(ogle_matched.data.I > 12.5, cutstr="Enforcing OGLE saturation")

fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1, wspace=0, hspace=0)
ax = plt.subplot(221)
cut1 = (ogle_matched.data.Spectr == "C-rich") & (ogle_matched.data.Type == "OSARG")
cut2 = (ogle_matched.data.Spectr == "O-rich") & (ogle_matched.data.Type == "OSARG")
ax.scatter(ogle_matched.data.coljk[cut2], ogle_matched.data.colvi[cut2], c='b', s=1, edgecolor="None")
ax.scatter(ogle_matched.data.coljk[cut1], ogle_matched.data.colvi[cut1], c='r', s=1, edgecolor="None")
ax.text(0.9, 0.9, "OSARGs", transform=ax.transAxes, horizontalalignment="right")
ax.set_ylim(0,5)
ax.set_xlim(0,5)
ax.set_ylabel("$(V-I)$")
ax.get_xaxis().set_visible(False)
ax.minorticks_on()

ax = plt.subplot(223)
cut1 = (ogle_matched.data.Spectr == "C-rich") & (ogle_matched.data.Type == "Mira")
cut2 = (ogle_matched.data.Spectr == "O-rich") & (ogle_matched.data.Type == "Mira")
ax.scatter(ogle_matched.data.coljk[cut2], ogle_matched.data.colvi[cut2], c='b', s=1, edgecolor="None")
ax.scatter(ogle_matched.data.coljk[cut1], ogle_matched.data.colvi[cut1], c='r', s=1, edgecolor="None")
ax.text(0.9, 0.9, "Miras", transform=ax.transAxes, horizontalalignment="right")
ax.set_ylim(0,5)
ax.set_xlim(0,5)
ax.set_xlabel("$(J-K_s)$")
ax.set_ylabel("$(V-I)$")
ax.minorticks_on()

ax = plt.subplot(224)
cut1 = (ogle_matched.data.Spectr == "C-rich") & (ogle_matched.data.Type == "SRV")
cut2 = (ogle_matched.data.Spectr == "O-rich") & (ogle_matched.data.Type == "SRV")
ax.scatter(ogle_matched.data.coljk[cut2], ogle_matched.data.colvi[cut2], c='b', s=1, edgecolor="None")
ax.scatter(ogle_matched.data.coljk[cut1], ogle_matched.data.colvi[cut1], c='r', s=1, edgecolor="None")
ax.text(0.9, 0.9, "SRVs", transform=ax.transAxes, horizontalalignment="right")
ax.set_ylim(0,5)
ax.set_xlim(0,5)
ax.get_yaxis().set_visible(False)
ax.set_xlabel("$(J-K_s)$")
ax.minorticks_on()
plt.show()
