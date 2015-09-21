import pandas as pd
import numpy as np
import os

def add_colors(df):
    df["coljh"] = df.jmag - df.hmag
    df["coljk"] = df.jmag - df.kmag
    df["colj1"] = df.jmag - df.w1
    df["colj2"] = df.jmag - df.w2
    df["colj3"] = df.jmag - df.w3
    df["colj4"] = df.jmag - df.w4

    df["colhk"] = df.hmag - df.kmag
    df["colh1"] = df.hmag - df.w1
    df["colh2"] = df.hmag - df.w2
    df["colh3"] = df.hmag - df.w3
    df["colh4"] = df.hmag - df.w4

    df["colk1"] = df.kmag - df.w1
    df["colk2"] = df.kmag - df.w2
    df["colk3"] = df.kmag - df.w3
    df["colk4"] = df.kmag - df.w4

    df["col12"] = df.w1 - df.w2
    df["col13"] = df.w1 - df.w3
    df["col14"] = df.w1 - df.w4
    df["col23"] = df.w2 - df.w3
    df["col24"] = df.w2 - df.w4
    df["col34"] = df.w3 - df.w4

    return df
    
def read_gator(infile):
    readin = open(infile,'r').readlines()
    data = readin[84:]

    columns = readin[80].split('|')
    colnames = []

    data_dict = {}

    for ii in range(1,len(columns)-1):
        the_name = columns[ii].strip()
        colnames.append(the_name)
        data_dict[the_name] = []

    for ii in range(len(data)):
        line = data[ii].split()
        for jj in range(len(colnames)):
            data_dict[colnames[jj]].append(line[jj])

    df = pd.DataFrame(data_dict)
    df = df.replace("null", np.nan)
    
    rename_these = {
        "designation":"wisename","cc_flags":"ccflag", 
        "dec":"decl","ext_flg":"extflg","w1mpro":"w1", 
        "w2mpro":"w2", "w3mpro":"w3", "w4mpro":"w4",
        "w1sigmpro":"w1err", "w2sigmpro":"w2err", 
        "w3sigmpro":"w3err", "w4sigmpro":"w4err",
        "j_m_2mass":"jmag", "h_m_2mass":"hmag", 
        "k_m_2mass":"kmag", "j_msig_2mass":"jerr", 
        "h_msig_2mass":"herr", "k_msig_2mass":"kerr",
        "n_2mass":"n2mass", "r_2mass":"r2mass", 
        "var_flg":"varflg"
        }
    df.rename(columns=rename_these, inplace=True)

    retype_these = "decl,ra,w1,w2,w3,w4,w1err,w2err,w3err,w4err,w1snr,w2snr,w3snr,w4snr,jmag,hmag,kmag,jerr,herr,kerr,n2mass,r2mass,extflg,glon,glat,sigra,sigdec,sigradec"
    retype_these = retype_these.split(",")
    df[retype_these] = df[retype_these].astype(float)
    
    df = add_colors(df)
    
    return df

def photo_cuts(df):
    sat = {"w1":2.0, "w2":1.5, "w3":-3.0, "k":8.5}
    fnt = {"w1":16.83, "w2":15.6, "w3":11.32, "k":15.5}
    snr = 3
    
    cuts = (df.w1 > sat["w1"]) & (df.w2 > sat["w2"]) & (df.w3 > sat["w3"]) & (df.kmag > sat["k"]) & (df.w1 < fnt["w1"]) & (df.w2 < fnt["w2"]) & (df.w3 < fnt["w3"]) & (df.kmag < fnt["k"]) & (df.w1snr > snr) & (df.w2snr > snr) & (df.w3snr > snr) & (df.ccflag.map(lambda flag: flag.startswith("00")))

    return df[cuts]

def agb_cuts(df):
    cuts = (df.coljk > 1.1) & (df.col23 < 2.5) & (df.col23 > -0.1)
    
    return df[cuts]

def remove_ysos(df):
    cuts = (df.col12 < 0.2) | (df.col12 > 0.75*df.col23 - 0.33) | (df.col12 < -1. * df.col23 + 1.5)
    
    return df[cuts]

filedir = "/Users/Nick/Documents/AGBstuff/new_work/allsky_gator/"
files = [filedir + f for f in os.listdir("../allsky_gator") if f.endswith(".tbl")]

outdir = "/Users/Nick/Documents/AGBstuff/new_work/agb_candidates/"
files = files[18:]
for f in files:
    ra1 = f.split("/")[-1].split("_")[2]
    ra2 = f.split("/")[-1].split("_")[3].split(".")[0]
    newfile = outdir+"candidates_ra_"+ra1+"_"+ra2+".dat"

    df = remove_ysos(agb_cuts(photo_cuts(read_gator(f))))
    df.to_csv(newfile, sep=",", index=False)




