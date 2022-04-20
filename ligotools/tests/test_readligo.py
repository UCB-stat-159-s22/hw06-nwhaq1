from ligotools import readligo as rl
import os

def test_one():
    fn_L1 = u'L-L1_LOSC_4_V2-1126259446-32.hdf5'
    
    filepath = os.path.abspath("data/" + fn_L1)
    
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(filepath, 'L1')
    assert strain_L1 is not None  
    assert time_L1 is not None  

def test_two():
    fn_L1 = u'L-L1_LOSC_4_V2-1126259446-32.hdf5'
    filepath = os.path.abspath("data/" + fn_L1)
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(filepath, 'L1')
    
    assert chan_dict_L1 is not None 

def test_three():
    fn_H1 = u'H-H1_LOSC_4_V2-1126259446-32.hdf5'
    filepath = os.path.abspath("data/" + fn_H1)
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(filepath, 'H1')
    assert strain_H1 is not None  
    assert time_H1 is not None  
    
def test_four():
    fn_H1 = u'H-H1_LOSC_4_V2-1126259446-32.hdf5'
    filepath = os.path.abspath("data/" + fn_H1)
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(filepath, 'H1')
    assert chan_dict_H1 is not None  
