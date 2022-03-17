import pandas as pd
from IPython.display import display

class DataInfo:
    _df = None
    
    def __init__(self, df):
        self._df = df
    
    def describe(self):
        display(self.head())
        display(self.isnull())
    
    def head(self):
        return self._df.head()
    
    def isnull(self):
        return self._df.isnull().sum()