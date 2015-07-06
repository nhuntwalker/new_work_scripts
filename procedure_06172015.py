from thesiscode.quality import *
from thesiscode.plotting import *
import pandas as pd

fname = "../samples/macho.tsv"
macho = read_vizier(fname)
macho = Data(macho)
macho.to_irsa("_RAJ2000", "_DEJ2000", "../samples/macho_formatted.dat")
macho.to_table("../samples/macho_table.dat")

fname = "../samples/ogle_lmcsmcbulge.dat"
ogle = read_ogle(fname)
ogle = Data(ogle)
ogle.to_irsa("RA", "Decl", "../samples/ogle_formatted.dat")
ogle.to_table("../samples/ogle_table.dat")

##### After matching to wise #####
macho_matched = read_gator_matched("../samples/macho_allwise_match.tbl", "macho")
ogle_matched = read_gator_matched("../samples/ogle_allwise_match.tbl", "ogle")
