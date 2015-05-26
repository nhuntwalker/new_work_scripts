-- DROP TABLE macho_allwise_allmags;

CREATE TABLE macho_allwise_allmags AS (
	SELECT m.machoid,m.p0,m.p1,m.v,m.r,m.j,m.h,m.gal_loc,m.sequence,m.k,
	w.wisename,w.match_rad,w.ra,w.decl,w.glon,w.glat,w.w1,w.w1err,w.w1snr,w.w2,w.w2err,w.w2snr,w.w3,w.w3err,w.w3snr,w.w4,w.w4err,w.w4snr,w.ccflag,w.extflg,w.var_flg,w.n2mass,w.jmag,w.jerr,w.hmag,w.herr,w.kmag,w.kerr,w.macho_ra,w.macho_decl
	FROM macho_lpvs AS m INNER JOIN macho_allwise AS w ON m.machoid = w.machoid
);

ALTER TABLE macho_allwise_allmags ADD INDEX wisename(wisename);
ALTER TABLE macho_allwise_allmags ADD INDEX p0(p0);
ALTER TABLE macho_allwise_allmags ADD INDEX p1(p1);
ALTER TABLE macho_allwise_allmags ADD INDEX v(v);
ALTER TABLE macho_allwise_allmags ADD INDEX r(r);
ALTER TABLE macho_allwise_allmags ADD INDEX j(j);
ALTER TABLE macho_allwise_allmags ADD INDEX h(h);
ALTER TABLE macho_allwise_allmags ADD INDEX gal_loc(gal_loc);
ALTER TABLE macho_allwise_allmags ADD INDEX sequence(sequence);
ALTER TABLE macho_allwise_allmags ADD INDEX k(k);
ALTER TABLE macho_allwise_allmags ADD INDEX match_rad(match_rad);
ALTER TABLE macho_allwise_allmags ADD INDEX ra(ra);
ALTER TABLE macho_allwise_allmags ADD INDEX decl(decl);
ALTER TABLE macho_allwise_allmags ADD INDEX glon(glon);
ALTER TABLE macho_allwise_allmags ADD INDEX glat(glat);
ALTER TABLE macho_allwise_allmags ADD INDEX w1(w1);
ALTER TABLE macho_allwise_allmags ADD INDEX w1err(w1err);
ALTER TABLE macho_allwise_allmags ADD INDEX w1snr(w1snr);
ALTER TABLE macho_allwise_allmags ADD INDEX w2(w2);
ALTER TABLE macho_allwise_allmags ADD INDEX w2err(w2err);
ALTER TABLE macho_allwise_allmags ADD INDEX w2snr(w2snr);
ALTER TABLE macho_allwise_allmags ADD INDEX w3(w3);
ALTER TABLE macho_allwise_allmags ADD INDEX w3err(w3err);
ALTER TABLE macho_allwise_allmags ADD INDEX w3snr(w3snr);
ALTER TABLE macho_allwise_allmags ADD INDEX w4(w4);
ALTER TABLE macho_allwise_allmags ADD INDEX w4err(w4err);
ALTER TABLE macho_allwise_allmags ADD INDEX w4snr(w4snr);
ALTER TABLE macho_allwise_allmags ADD INDEX ccflag(ccflag);
ALTER TABLE macho_allwise_allmags ADD INDEX extflg(extflg);
ALTER TABLE macho_allwise_allmags ADD INDEX var_flg(var_flg);
ALTER TABLE macho_allwise_allmags ADD INDEX n2mass(n2mass);
ALTER TABLE macho_allwise_allmags ADD INDEX jmag(jmag);
ALTER TABLE macho_allwise_allmags ADD INDEX hmag(hmag);
ALTER TABLE macho_allwise_allmags ADD INDEX kmag(kmag);
