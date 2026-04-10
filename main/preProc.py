import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# import warnings                                              
from sklearn.exceptions import DataConversionWarning          
# warnings.filterwarnings(action='ignore', category=DataConversionWarning)

def read_data(): 
    data= pd.read_csv('C:/Ironhack/ironhack-w2-project/training.csv')
    return data

def read_real_data(): 
    data= pd.read_csv('C:/Ironhack/ironhack-w2-project/REAL_DATA.csv')
    return data

def one_hot_encode_state_holidays(df):
    data= pd.get_dummies(df, columns=['state_holiday'], dtype=int)
    return data

def one_hot_encode_date(df):
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df['year'] = df['date'].dt.year.astype(int)
    df['month'] = df['date'].dt.month.astype(int)
    df['day'] = df['date'].dt.day.astype(int)
    df['day_of_week'] = df['date'].dt.dayofweek.astype(int)
    df['week_of_year'] = df['date'].dt.isocalendar().week.astype(int)
    df = df.drop(columns=['date'])
    return df

def clean_data(df):
    df.drop(columns=['Unnamed: 0', 'store_ID'], inplace=True)
    df_1=one_hot_encode_state_holidays(df)
    df_2=one_hot_encode_date(df_1)
    return df_2

def clean_real_data(df):
    df.drop(columns=['index', 'store_ID'], inplace=True)
    df_1=one_hot_encode_state_holidays(df)
    df_2=one_hot_encode_date(df_1)
    return df_2

data=clean_data(read_data())
real_data=clean_real_data(read_real_data())

print(data.head())
print(real_data.head())




