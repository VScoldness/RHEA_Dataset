from RHEA import RHEA
import numpy as np

# how to get lattice constant (A) of a RHEA at 300K
alloys = "25_25_25_25"
state = 'random'
lc = RHEA().getLC_300K()[state][alloys]
print(lc)

# how to get WCP of a CSRO RHEA at 300K
alloys = "25_25_25_25"
wcp = RHEA().getWCP_300K()[alloys]
print(np.array(wcp))