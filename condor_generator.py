import numpy as np
import os


## Purpose is to generate my CONDOR config file and individual job shell scripts

############################################################################
## Open CONDOR config file for writing. Start with the header information.
############################################################################
outfile = open('../dust_extinction/condor_extinction_run.cfg','w')
outfile.write('Notification = never\n')
outfile.write('getenv = true\n')
outfile.write('Executable = /astro/users/nmhw/research/agbstuff/new_work/scripts/execution_shellscript.csh\n')
outfile.write('Initialdir = /astro/users/nmhw/research/agbstuff/new_work/dust_extinction/\n')
outfile.write('Universe = vanilla\n\n')

outfile.write('Log = /astro/users/nmhw/research/agbstuff/new_work/dust_extinction/mylog.log\n')
outfile.write('Error = /astro/users/nmhw/research/agbstuff/new_work/dust_extinction/myerr.err\n\n')

# miss = [39,40,41]
# for i in miss:
for i in range(29):
	outfile.write('Output = /astro/users/nmhw/research/agbstuff/new_work/dust_extinction/candidate_outs/run%i.out\n' % i)
	outfile.write('Arguments = %i\n' % i)
	outfile.write('Queue\n\n')

outfile.close()
