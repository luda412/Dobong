import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
from convert import Convert
from gender import Gender
from passengerClass import PassengerClass

convert = Convert()

# ======= Survivors, Deads classify ========
dead_df = convert.get_deads(convert.df)
survivors_df = convert.get_survivors(convert.df)

# ===== Dead Gender DataFrame =====
dead_gender = Gender(dead_df)
dead_gender.paint_pie_male_female()

# ===== Dead passenger class DataFrame =====
dead_passengers = PassengerClass(dead_df)
dead_passengers.paint_pie_fist_second_third_class()
dead_passengers.paint_bar_fist_second_third_class()

# ===== Survived Gender DataFrame =====
survivors_gender = Gender(survivors_df)
survivors_gender.paint_pie_male_female()

# ===== Survived passenger class DataFrame =====
survivors_passengers = PassengerClass(survivors_df)
survivors_passengers.paint_pie_fist_second_third_class()
survivors_passengers.paint_bar_fist_second_third_class()


""" 
dead_gender = Gender(dead_df) 실행시 아래의 객체를 모두 가지고 있음
Gender
 ├── df            (dead_df 전체)
 ├── male_df       (남자만 필터링된 df)
 └── female_df     (여자만 필터링된 df)

dead_gender.male_df
dead_gender.female_df
이렇게 접근 가능함.
 """
"""
PassengerClass
 ├── df                (전체 DataFrame: 전달받은 df)
 ├── firstClass_df     (1등석만 필터링된 DataFrame)
 ├── secondClass_df    (2등석만 필터링된 DataFrame)
 └── thirdClass_df     (3등석만 필터링된 DataFrame)

passengers = PassengerClass(df)

passengers.firstClass_df
passengers.secondClass_df
passengers.thirdClass_df
 
"""
