import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

class Convert:
    file_name = "week5/titanic.csv"

    def __init__(self):
        self.df = self.read_file_to_df()
    
    def read_file_to_df(self):
        data = pd.read_csv(self.file_name)
        df = pd.DataFrame(data)
        return df
    
    def get_survivors(self, df):
        return  df[df['survived'] == 1].copy()
    
    def get_deads(self, df):
        return df[df['survived'] == 0].copy()
