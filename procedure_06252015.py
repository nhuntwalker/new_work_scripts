from thesiscode.quality import *
from thesiscode.plotting import *
import pandas as pd

simbad = Data(pd.read_csv("../samples/simbad_allwise_allmatches.dat", sep="|"))
macho = Data(pd.read_csv("../samples/macho_allwise_allmatches.dat", sep="|"))
ogle = Data(pd.read_csv("../samples/ogle_allwise_allmatches.dat", sep="|"))

simbad.clean_me()
macho.clean_me()
ogle.clean_me()

simbad.cut_me((simbad.data["coljk"] > 1.1) & (simbad.data["col23"] > 0.3), "J-K > 1.1 and W2-W3 > 0.3")
simplot = Plot(simbad.cutdata)
simplot.plot_colorcolor_completeness(simbad.cleaned, "coljk", "col23", "J-K", "W2-W3", xlims=(-0.5,5), ylims=(-0.5,5), vmin=0.0, vmax=1.0, cbar=True)
simplot.reset_figure()
simplot.plot_galactic_completeness(simbad.cleaned, "glon", "glat", xlims=(-180,180), vmin=0.0, vmax=1.0, cbar=True)
simplot.reset_figure()

macho.cut_me((macho.data["coljk"] > 1.1) & (macho.data["col23"] > 0.3), "J-K > 1.1 and W2-W3 > 0.3")
machoplot = Plot(macho.cutdata)
machoplot.plot_colorcolor_completeness(macho.cleaned, "coljk", "col23", "J-K", "W2-W3", xlims=(-0.5,5), ylims=(-0.5,5), vmin=0.0, vmax=1.0, cbar=True)
machoplot.reset_figure()
machoplot.plot_galactic_completeness(macho.cleaned, "glon", "glat", xlims=(-180,180), vmin=0.0, vmax=1.0, cbar=True)
machoplot.reset_figure()

ogle.cut_me((ogle.data["coljk"] > 1.1) & (ogle.data["col23"] > 0.3), "J-K > 1.1 and W2-W3 > 0.3")
ogleplot = Plot(ogle.cutdata)
ogleplot.plot_colorcolor_completeness(ogle.cleaned, "coljk", "col23", "J-K", "W2-W3", xlims=(-0.5,5), ylims=(-0.5,5), vmin=0.0, vmax=1.0, cbar=True)
ogleplot.reset_figure()
ogleplot.plot_galactic_completeness(ogle.cleaned, "glon", "glat", xlims=(-180,180), vmin=0.0, vmax=1.0, cbar=True)
ogleplot.reset_figure()
