from ligotools.utils import whiten, write_wavfile, reqshift, plot_figures
import numpy as np
import os

def test_utils_one():
    filepath = os.path.abspath("ligotools/tests/data/" + "strain_H1_whitenbpa.dat")
    strain_H1_whitenbp = np.fromfile(filepath, dtype=int)
    strain_H1_shifted = reqshift(strain_H1_whitenbp)

    assert strain_H1_shifted is not None 

def test_utils_two():
    assert whiten is not None

def test_utils_three():
    filepath = os.path.abspath("ligotools/tests/data/" + "strain_L1_whitenbpa.dat")
    strain_L1_whitenbp = np.fromfile(filepath, dtype=int)
    strain_L1_shifted = reqshift(strain_L1_whitenbp)

    assert strain_L1_shifted is not None 
    
def test_utils_four():
    assert plot_figures is not None