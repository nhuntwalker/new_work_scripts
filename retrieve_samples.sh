mysql -u root --password=root -D agbtables -e "SELECT w.ogleid, w.wisename, w.match_rad, w.ra, w.decl, w.glon, w.glat, w.w1, w.w1err, w.w1snr, w.w2, w.w2err, w.w2snr, w.w3, w.w3err, w.w3snr, w.w4, w.w4err, w.w4snr, w.ccflag, w.extflg, w.var_flg, w.n2mass, w.jmag, w.jerr, w.hmag, w.herr, w.kmag, w.kerr, o.spectr AS startype FROM ogle3_agbs AS o INNER JOIN ogle3_allwise_allmags AS w ON o.ogle3cnt = w.ogleid;" > ../samples/ogle3_allwise_allmags.dat

mysql -u root --password=root -D agbtables -e "SELECT w.machoid, w.wisename, w.match_rad, w.ra, w.decl, w.glon, w.glat, w.w1, w.w1err, w.w1snr, w.w2, w.w2err, w.w2snr, w.w3, w.w3err, w.w3snr, w.w4, w.w4err, w.w4snr, w.ccflag, w.extflg, w.var_flg, w.n2mass, w.jmag, w.jerr, w.hmag, w.herr, w.kmag, w.kerr, m.sequence AS startype FROM macho_lpvs AS m INNER JOIN macho_allwise_allmags AS w ON m.machoid = w.machoid;" > ../samples/macho_allwise_allmags.dat

mysql -u root --password=root -D agbtables -e "SELECT w.simbadid, w.wisename, w.match_rad, w.ra, w.decl, w.glon, w.glat, w.w1, w.w1err, w.w1snr, w.w2, w.w2err, w.w2snr, w.w3, w.w3err, w.w3snr, w.w4, w.w4err, w.w4snr, w.ccflag, w.extflg, w.var_flg, w.n2mass, w.jmag, w.jerr, w.hmag, w.herr, w.kmag, w.kerr, s.startype FROM simbad_agbs AS s INNER JOIN simbad_allwise_allmags AS w ON s.simbadid = w.simbadid;" > ../samples/simbad_allwise_allmags.dat
