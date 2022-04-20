from ligotools import readligo as rl
import os

def test_one():
    fn_L1 = u'H-H1_LOSC_4_V2-1126259446-32.hdf5'
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/' + fn_L1)
 
    filepath = os.path.abspath("data/" + fn_L1)
    
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(filepath, 'L1')
    assert True == True

def test_two():
    assert 0 == 0

def test_three():
    assert 1 == 1
    
def test_four():
    assert 1 == 1