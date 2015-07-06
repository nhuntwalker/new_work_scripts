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

ogle = pd.read_csv("../samples/ogle_table.dat", sep="|")
ogle["W_I"] = ogle.I - 1.55*(ogle.V - ogle.I)
ogle = Data(ogle)
ogle.data.Field[ogle.data.glon > 290] = "smc"
ogle.data.Field[ogle.data.glon < 290] = "lmc"
lmc = ogle.data.Field == "lmc"

ogle.cut_me(lmc, cutstr="Selecting only LMC objects")
ogle.cut_me(ogle.data.I > 12.5, cutstr="Enforcing OGLE saturation")

# ogle_plot = Plot(ogle.data, cuts=[ogle.data.Field == "smc", ogle.data.Field == "lmc"])
# ogle_plot.plot_period_mag("P_1", "V", "Log Period", "V Mag")

fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1, wspace=0, hspace=0)
ax = plt.subplot(221)
cut1 = (ogle.data.Spectr == "C-rich") & (ogle.data.Type == "OSARG")
cut2 = (ogle.data.Spectr == "O-rich") & (ogle.data.Type == "OSARG")
ax.scatter(np.log10(ogle.data.P_1[cut1]), ogle.data.W_I[cut1], c='r', s=1, edgecolor="None")
ax.scatter(np.log10(ogle.data.P_1[cut2]), ogle.data.W_I[cut2], c='b', s=1, edgecolor="None")
ax.text(0.9, 0.9, "OSARGs", transform=ax.transAxes, horizontalalignment="right")
ax.set_ylim(6.1, 15)
ax.set_xlim(0.5,3.49)
ax.set_ylabel("$W_I$ [mag]")
ax.get_xaxis().set_visible(False)
ax.invert_yaxis()
ax.minorticks_on()

ax = plt.subplot(223)
cut1 = (ogle.data.Spectr == "C-rich") & (ogle.data.Type == "Mira")
cut2 = (ogle.data.Spectr == "O-rich") & (ogle.data.Type == "Mira")
ax.scatter(np.log10(ogle.data.P_1[cut1]), ogle.data.W_I[cut1], c='r', s=1, edgecolor="None")
ax.scatter(np.log10(ogle.data.P_1[cut2]), ogle.data.W_I[cut2], c='b', s=1, edgecolor="None")
ax.text(0.9, 0.9, "Miras", transform=ax.transAxes, horizontalalignment="right")
ax.set_ylim(6.1, 15)
ax.set_xlim(0.5,3.49)
ax.invert_yaxis()
ax.set_xlabel("log$_{10}$ P [d]")
ax.set_ylabel("$W_I$ [mag]")
ax.minorticks_on()

ax = plt.subplot(224)
cut1 = (ogle.data.Spectr == "C-rich") & (ogle.data.Type == "SRV")
cut2 = (ogle.data.Spectr == "O-rich") & (ogle.data.Type == "SRV")
ax.scatter(np.log10(ogle.data.P_1[cut1]), ogle.data.W_I[cut1], c='r', s=1, edgecolor="None")
ax.scatter(np.log10(ogle.data.P_1[cut2]), ogle.data.W_I[cut2], c='b', s=1, edgecolor="None")
ax.text(0.9, 0.9, "SRVs", transform=ax.transAxes, horizontalalignment="right")
ax.set_ylim(6.1, 15)
ax.set_xlim(0.5,3.49)
ax.get_yaxis().set_visible(False)
ax.set_xlabel("log$_{10}$ P [d]")
ax.invert_yaxis()
ax.minorticks_on()
plt.savefig("../figures/ogle_2mass_pmag.png")
plt.show()

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
fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1, wspace=0)
ax = plt.subplot(111)
cut1 = (ogle_matched.data.Spectr == "C-rich")
cut2 = (ogle_matched.data.Spectr == "O-rich")
ax.scatter(np.log10ogle_matched.data.coljk[cut2], ogle_matched.data.colvi[cut2], c='b', s=1, edgecolor="None")
ax.scatter(np.log10ogle_matched.data.coljk[cut1], ogle_matched.data.colvi[cut1], c='r', s=1, edgecolor="None")
ax.set_ylabel("$(V-I)$")
ax.set_xlabel("$(J-K_s)$")
ax.set_ylim(0,5)
ax.set_xlim(-1,1)
ax.minorticks_on()
plt.savefig("../figures/ogle_2mass_colcol.png")
plt.show()
