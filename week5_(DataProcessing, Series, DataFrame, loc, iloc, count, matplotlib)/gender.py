import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

class Gender:

    def __init__(self, df):
        self.df = df
        self.male_df = self.df[self.df['sex'] == 'male'].copy()
        self.female_df = self.df[self.df['sex'] == 'female'].copy()
    
    def paint_pie_male_female(self):
        male_num = len(self.male_df)
        female_num = len(self.female_df)

        labels = ['Male', 'Female']
        sizes = [male_num, female_num]

        plt.figure(figsize=(6,6))
        plt.pie(sizes, labels = labels, autopct='%.1f%%', startangle=90)
        print(f"=======================\n{self.male_df['survived']}")
        if(self.male_df['survived'].iloc[0] == 1):
            plt.title('Survivors Rage by Sex')
        else:
            plt.title('Deads Rage by Sex')
        plt.axis('equal')
        plt.show()

