import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord

## Collect and clean OGLE LMC RGB stars

df = pd.read_csv("../contaminants/ogle_lpvs_rgb_lmc.txt",
                 delimiter="\t", header=6)

def output_for_gator(idnum, ra, dec, name, fname):

    head1 = "|id   |ra                   |dec                      |name                                       |\n"
    head2 = "|int  |double               |double                   |char                                       |\n"

    fout = open(fname, 'w')
    fout.write(head1)
    fout.write(head2)

    for ii in range(len(idnum)):
        fmt1 = " %i"
        nspaces1 = " "*(len(str(max(idnum))) - len(str(idnum[ii])) + 2)
        fmt2 = "%.6f"
        nspaces2 = " "*(len(str(max(ra))) - len(str(ra[ii])) + 20)
        fmt3 = "%.6f"
        nspaces3 = " "*(len(str(max(dec))) - len(str(dec[ii])) + 20)
        fmt4 = " %s\n"
        fmt = fmt1+nspaces1+fmt2+nspaces2+fmt3+nspaces3+fmt4

        fout.write(fmt % (idnum[ii], ra[ii], dec[ii], name[ii]))

    fout.close()

# c = SkyCoord(df.RA, df.Decl, unit=(u.hour, u.deg))
# df["ra_deg"] = c.ra.deg
# df["decl_deg"] = c.dec.deg
#
# output_for_gator(range(len(df)), df.ra_deg, df.decl_deg, df["# ID"],
#                  "ogle_rgbs_for_gator.dat")

gator_df = pd.read_csv("../contaminants/lmcrgbs_cleaned_gator.dat")


matched_df = pd.concat((df[['Type', 'Evol', 'Spectr', 'I', 'V', 'P_1', 'A_1', 'P_2', 'A_2', 'P_3', 'A_3']], gator_df), axis=1)
rename_dict = {
"dist_x":"mrad", "j_m_2mass":"jmag", "h_m_2mass":"hmag", "k_m_2mass":"kmag",
"j_msig_2mass":"jerr", "h_msig_2mass":"herr", "k_msig_2mass":"kerr",
"w1mpro":"w1", "w2mpro":"w2", "w3mpro":"w3", "w4mpro":"w4",
"w1sigmpro":"w1err", "w2sigmpro":"w2err", "w3sigmpro":"w3err", "w4sigmpro":"w4err",
"cc_flags":"ccflag", "dec":"decl", "n_2mass":"n2mass",
"r_2mass":"r2mass", "ext_flg":"extflg"
}
matched_df.rename(columns = rename_dict, inplace=True)
matched_df = matched_df.replace("null", np.nan)
float_cols = [
              "I", "V",
              "P_1", "P_2", "P_3",
              "A_1", "A_2", "A_3",
              "mrad", "glat", "glon", "ra", "decl",
              "jmag", "jerr", "hmag", "herr", "kmag", "kerr",
              "n2mass", "r2mass",
              "w1", "w2", "w3", "w4",
              "w1err", "w2err", "w3err", "w4err",
              "w1snr", "w2snr", "w3snr", "w4snr",
              "sigdec", "sigra", "sigradec", "extflg"
              ]
str_cols = [
            "ccflag", "Type", "Evol", "Spectr", "designation",
            "name_01", "var_flg"
]
matched_df[float_cols] = matched_df[float_cols].astype(float)
matched_df[str_cols] = matched_df[str_cols].astype(str)
matched_df = matched_df[matched_df.n2mass == 1]
matched_df.to_csv("../contaminants/lmcrgbs_allwise_allmags.dat", sep=",", index=False)
