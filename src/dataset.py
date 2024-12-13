from datasets import load_dataset, config
from tokenizor import Tokenizier
import os 

class DataSetConfig:
    IS_HF_DATA = True 
    HF_DATASET_LINK = '.......'


class PEFTDataSet(object):
    def __init__(self):
        pass

    def _root_location(self,):
        return config.HF_DATASETS_CACHE 

    def _root_file_location(self, dataset, split = None):
        """
        Returns the file location(s) for the specified dataset split(s) from a Hugging Face dataset object.
        Parameters:
            dataset: Hugging Face dataset object.
            split (str or None): The dataset split ('train', 'test', 'validation', etc.).
                                If None, returns file locations for all splits.
        Returns:
            str or dict: The file location if a split is specified, or a dictionary of all splits with their file locations if no split is specified.
        """
        if split:
            if split in dataset and hasattr(dataset[split],"cache_files"):
                return dataset[split].cache_files[0]['filename']
            else:
                return None
        else:
            split_locations ={}
            for split_name in dataset.keys():
                if hasattr(dataset[split_name],"cache_files"):
                    split_locations[split_name]=dataset[split_name].cache_files[0]['filename']
            return split_locations
  
    def _delete_cache(self, dataset):
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
  


