from __future__ import print_function, division


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import nsfg
import first

f_resp = open("./code/2002FemResp.dct", 'r') 
nbr_resp = 0
for l_resp in f_resp:
    nbr_resp += 1
f_resp.close()
f_preg = open("./code/2002FemPreg.dct", 'r')
nbr_preg = 0
for l_preg in f_preg:
    nbr_preg += 1
f_preg.close()

print("# of respondents: %d" % (nbr_resp))
print("# of pregnancies: %d" % (nbr_preg))

#Select the birthord column, print the value counts, and compare to results published in the codebook

preg = nsfg.ReadFemPreg()
preg.birthord.value_counts()

