-- DROP TABLE ogle3_allwise_allmags;

CREATE TABLE ogle3_allwise_allmags AS (
	SELECT o.ogle3cnt,o.ogle3id,o.field,o.starid,o.type,o.evol,o.spectr,o.I_mean,o.V_mean,o.p,o.I_amp,
	w.wisename,w.match_rad,w.ra,w.decl,w.glon,w.glat,w.w1,w.w1err,w.w1snr,w.w2,w.w2err,w.w2snr,w.w3,w.w3err,w.w3snr,w.w4,w.w4err,w.w4snr,w.ccflag,w.extflg,w.var_flg,w.n2mass,w.jmag,w.jerr,w.hmag,w.herr,w.kmag,w.kerr,w.ogle_ra,w.ogle_decl
	FROM ogle3_agbs AS o INNER JOIN ogle3_allwise AS w ON o.ogle3cnt = w.ogleid
);

ALTER TABLE ogle3_allwise_allmags ADD INDEX wisename(wisename);
ALTER TABLE ogle3_allwise_allmags ADD INDEX type(type);
ALTER TABLE ogle3_allwise_allmags ADD INDEX evol(evol);
ALTER TABLE ogle3_allwise_allmags ADD INDEX spectr(spectr);
ALTER TABLE ogle3_allwise_allmags ADD INDEX I_mean(I_mean);
ALTER TABLE ogle3_allwise_allmags ADD INDEX V_mean(V_mean);
ALTER TABLE ogle3_allwise_allmags ADD INDEX p(p);
ALTER TABLE ogle3_allwise_allmags ADD INDEX I_amp(I_amp);
ALTER TABLE ogle3_allwise_allmags ADD INDEX match_rad(match_rad);
ALTER TABLE ogle3_allwise_allmags ADD INDEX ra(ra);
ALTER TABLE ogle3_allwise_allmags ADD INDEX decl(decl);
ALTER TABLE ogle3_allwise_allmags ADD INDEX glon(glon);
ALTER TABLE ogle3_allwise_allmags ADD INDEX glat(glat);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w1(w1);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w1err(w1err);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w1snr(w1snr);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w2(w2);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w2err(w2err);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w2snr(w2snr);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w3(w3);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w3err(w3err);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w3snr(w3snr);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w4(w4);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w4err(w4err);
ALTER TABLE ogle3_allwise_allmags ADD INDEX w4snr(w4snr);
ALTER TABLE ogle3_allwise_allmags ADD INDEX ccflag(ccflag);
ALTER TABLE ogle3_allwise_allmags ADD INDEX extflg(extflg);
ALTER TABLE ogle3_allwise_allmags ADD INDEX var_flg(var_flg);
ALTER TABLE ogle3_allwise_allmags ADD INDEX n2mass(n2mass);
ALTER TABLE ogle3_allwise_allmags ADD INDEX jmag(jmag);
ALTER TABLE ogle3_allwise_allmags ADD INDEX hmag(hmag);
ALTER TABLE ogle3_allwise_allmags ADD INDEX kmag(kmag);
