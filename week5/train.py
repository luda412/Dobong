import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

class Train:
    file_name = "week5/train.csv"
    
    def read_file_to_df(self):
        data = pd.read_csv(self.file_name)
        df = pd.DataFrame(data)
        return df
    
    def get_survivors(self, df):
        survived_df = df[df['Survived'] == 1].copy()
        return survived_df

    
    def get_survivors_male(self, df):
        survived_male_df = df[(df['Survived'] == 1) & (df['Sex'] == 'male')].copy()
        return survived_male_df
    
    def get_survivors_female(self, df):
        survived_female_df = df[(df['Survived'] == 1) & (df['Sex'] == 'female')].copy()
        return survived_female_df

    def paint_pie_male_female(self, survived_male_df, survived_female_df):
        male_num = len(survived_male_df)
        female_num = len(survived_female_df)

        labels = ['Male', 'Female']
        sizes = [male_num, female_num]

        plt.figure(figsize=(6,6))
        plt.pie(sizes, labels = labels, autopct='%.1f%%', startangle=90)
        plt.title('Survivors Rage by Sex')
        plt.axis('equal')
        plt.show()

train = Train()
df = train.read_file_to_df()
survived_df = train.get_survivors(df)
print("----- Survived DataFrame -----")
print(survived_df)

survived_male_df = train.get_survivors_male(df)
print("----- Survived Male DataFrame -----")
print(survived_male_df)

survived_female_df = train.get_survivors_female(df)
print("----- Survived Female DataFrame -----")
print(survived_female_df)

train.paint_pie_male_female(survived_male_df, survived_female_df)

