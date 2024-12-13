from datasets import load_dataset
from tokenizor import Tokenizier

class DataSetConfig:
    IS_HF_DATA = True 
    HF_DATASET_LINK = '.......'


class PEFTDataSet(object):
    def __init__(self):
        pass

    def _location(self):
        pass 

    def _delete(self):
        pass 

    def _get_samples(self):
        pass 

    def _analysis(self):
        # Like to know number datapoints 
        # What is the input given to the Training 
        pass 
        

class PEFTDataAnalyzer(object):
    def __init__(self, data :PEFTDataSet, tokenizer : Tokenizier ):

        pass
  


