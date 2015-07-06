from thesiscode.quality import *
from thesiscode.plotting import *
import pandas as pd

# f1 = "../samples/simbad_agbs.txt"
# f2 = "../samples/simbad_cstars1.txt"
# f3 = "../samples/simbad_cstars2.txt"
# f4 = "../samples/simbad_sstars.txt"
# f5 = "../samples/simbad_miras.txt"
# f6 = "../samples/simbad_ohir.txt"

# agbs = read_simbad(f1)
# cstars1 = read_simbad(f2)
# cstars2 = read_simbad(f3)
# sstars = read_simbad(f4)
# miras = read_simbad(f5)
# ohir = read_simbad(f6)

# all_simbad = pd.concat([agbs,cstars1,cstars2,sstars,miras,ohir], ignore_index=True)
# ##### check for duplicates in all_simbad #####
# all_simbad = all_simbad.drop_duplicates(subset="identifier")
# all_simbad.reset_index(drop=True, inplace=True)

# all_simbad = Data(all_simbad)
# all_simbad.to_table("../samples/simbad_table.dat")
# all_simbad.to_irsa("ra","decl","../samples/simbad_formatted.dat")

# ##### After matching to WISE #####
# all_simbad = Data(pd.read_csv("../samples/simbad_table.dat", sep="|"))
# simbad_matched = read_gator_matched("../samples/simbad_allwise_match.tbl", "simbad")
# simbad = match_data(all_simbad.data, simbad_matched)

# ##### Retrieving from last time #####
# ogle = Data(pd.read_csv("../samples/ogle_table.dat", sep="|"))
# ogle_matched = read_gator_matched("../samples/ogle_allwise_match.tbl", "ogle")
# macho = Data(pd.read_csv("../samples/macho_table.dat", sep="|"))
# macho_matched = read_gator_matched("../samples/macho_allwise_match.tbl", "macho")

# ogle = match_data(ogle.data, ogle_matched)
# macho = match_data(macho.data, macho_matched)

# simbad = Data(simbad)
# macho = Data(macho)
# ogle = Data(ogle)

# simbad.to_table("../samples/simbad_allwise_allmatches.dat")
# macho.to_table("../samples/macho_allwise_allmatches.dat")
# ogle.to_table("../samples/ogle_allwise_allmatches.dat")

simbad = Data(pd.read_csv("../samples/simbad_allwise_allmatches.dat", sep="|"))
macho = Data(pd.read_csv("../samples/macho_allwise_allmatches.dat", sep="|"))
ogle = Data(pd.read_csv("../samples/ogle_allwise_allmatches.dat", sep="|"))

simbad.clean_me()
macho.clean_me()
ogle.clean_me()

simbad.display_stats()
macho.display_stats()
ogle.display_stats()