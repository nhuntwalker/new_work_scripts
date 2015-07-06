from thesiscode.plotting import Plot
from thesiscode.quality import Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

cut1 = (ogle.data.Spectr == "C-rich") & (ogle.data.Type == "OSARG")
cut2 = (ogle.data.Spectr == "O-rich") & (ogle.data.Type == "OSARG")


fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.scatter(np.log10(ogle.data.P_1[cut1]), ogle.data.W_I[cut1], c='r', s=1, edgecolor="None")
ax.scatter(np.log10(ogle.data.P_1[cut2]), ogle.data.W_I[cut2], c='b', s=1, edgecolor="None")
ax.invert_yaxis()
ax.minorticks_on()
plt.show()
