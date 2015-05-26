CREATE TABLE ogle_macho_allwise_everything AS (
	SELECT m.wisename, m.machoid,m.p0,m.p1,m.v,m.r,m.j,m.h,m.gal_loc,m.sequence,m.k,
	o.ogle3cnt,o.ogle3id,o.field,o.starid,o.type,o.evol,o.spectr,o.I_mean,o.V_mean,o.p,o.I_amp,
	o.match_rad,o.ra,o.decl,o.glon,o.glat,o.w1,o.w1err,o.w1snr,o.w2,o.w2err,o.w2snr,o.w3,o.w3err,o.w3snr,o.w4,o.w4err,o.w4snr,o.ccflag,o.extflg,o.var_flg,o.n2mass,o.jmag,o.jerr,o.hmag,o.herr,o.kmag,o.kerr 
	FROM macho_allwise_allmags AS m INNER JOIN ogle3_allwise_allmags AS o ON m.wisename = o.wisename
);