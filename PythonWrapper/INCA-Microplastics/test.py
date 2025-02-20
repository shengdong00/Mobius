import os, sys
os.chdir(sys.path[0])

#%matplotlib inline
# Switch to ''%matplotlib ipympl' for interactive plots
import warnings
import imp
import pickle
import lmfit
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

# Styling
warnings.filterwarnings("ignore")
plt.style.use('ggplot')


# Initialise wrapper and test datasets
wrapper_fpath = (r"..\mobius.py")
wr = imp.load_source('mobius', wrapper_fpath)
wr.initialize('..\..\Applications\IncaMicroplastics\incamicroplastics.dll')

# Calibration functions
calib_fpath = (r"..\mobius_calib_uncert_lmfit.py")
cu = imp.load_source('mobius_calib_uncert_lmfit', calib_fpath)


#dataset = wr.DataSet.setup_from_parameter_and_input_files('..\..\Applications\IncaC\Boyne\persist_params_Boyne.dat', '..\..\Applications\IncaC\Boyne\incac_inputs_Boyne.dat')
dataset = wr.DataSet.setup_from_parameter_and_input_files(
    '..\..\Impasse\\best_calibration.dat', # parameters
    '..\..\Impasse\\inputs_Mobius.dat' # inputs
)


print(f"{'Index Sets'.rjust(20)}  Indexes")
print(f"{'--------------'.rjust(20)}  -----------------")
for index_set in dataset.get_index_sets():
    print(f"{index_set.rjust(20)}  " + str(dataset.get_indexes(index_set)))


el = dataset.get_equation_list()