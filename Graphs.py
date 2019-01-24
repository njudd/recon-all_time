import numpy as np
import pandas as pd
import seaborn as sea

# loading data, vectors are unequal length due to processing failures
# this is just a rough check but those subjects should be entirely excluded

path = '/Users/Nick/Projects/Imaging/recon-all_time/time/'

MRI1 = pd.read_csv(path + "MRI1_time.txt", sep=" ", header=None)
MRI2 = pd.read_csv(path + "MRI2_time.txt", sep=" ", header=None)
base = pd.read_csv(path + "base_time.txt", sep=" ", header=None)
MRI1_long = pd.read_csv(path + "MRI1.long_time.txt", sep=" ", header=None)
MRI2_long = pd.read_csv(path + "MRI2.long_time.txt", sep=" ", header=None)

# making a dataframe, I'm sure there is a better way to load... but this is my first real python script
t = pd.concat([MRI1,MRI2, base, MRI1_long, MRI2_long], axis=1)
t.columns = ["MRI1", "MRI2", "base", "MRI1_long", "MRI2_long"]

# usually now I would want to average rows MRI1 & MRI2 into standard_recon
# and MRI1_long with MRI2_long into long_recon, yet the subs don't match
# which is something I need to fix in the bash script...

standard_recon = np.concatenate((np.array(t['MRI1']), np.array(t['MRI2'])), axis=0)
standard_recon = standard_recon[~np.isnan(standard_recon)]

long_recon = np.concatenate((np.array(t['MRI1_long']), np.array(t['MRI2_long'])), axis=0)
long_recon = long_recon[~np.isnan(long_recon)]

# Histograms of different processing times, with average value clearly marked for the 3 processes

t['MRI1']



# Scatterplot of processing time with TIV






