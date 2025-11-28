import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
class PassengerClass:

    def __init__(self, df):
        self.df = df
        self.firstClass_df = self.df[self.df['class'] == 'First'].copy()
        self.secondClass_df = self.df[self.df['class'] == 'Second'].copy()
        self.thirdClass_df = self.df[self.df['class'] == 'Third'].copy()

    def paint_pie_fist_second_third_class(self):
        first_num = len(self.firstClass_df)
        second_num = len(self.secondClass_df)
        third_num = len(self.thirdClass_df)

        labels = ['First Class', 'Second Class', 'Third Class']
        sizes = [first_num, second_num, third_num]

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)
        print(f"========================\n{self.firstClass_df['survived']}")
        if(self.firstClass_df['survived'].iloc[0] == 1):
            plt.title('Survivors Range by Class')
        else:
            plt.title('Deads Range by Class')
        plt.axis('equal')
        plt.show()
    
    def paint_bar_fist_second_third_class(self):
        first_num = len(self.firstClass_df)
        second_num = len(self.secondClass_df)
        third_num = len(self.thirdClass_df)

        labels = [
            f'First Class ({first_num} 명)', 
            f'Second Class ({second_num} 명)', 
            f'Third Class ({third_num} 명)'
            ]
        sizes = [first_num, second_num, third_num]
        
        plt.figure(figsize=(6, 6))
        plt.bar(labels, sizes)
    
        if self.firstClass_df['survived'].iloc[0] == 1:
            plt.title('Survivors Range by Class')
        else:
            plt.title('Deads Range by Class')

        plt.xlabel('Passenger Class')
        plt.ylabel('Number of Passengers')
        plt.show()

