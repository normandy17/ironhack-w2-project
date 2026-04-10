import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# import warnings                                              
from sklearn.exceptions import DataConversionWarning          
# warnings.filterwarnings(action='ignore', category=DataConversionWarning)

def read_data(): 
    data= pd.read_csv('C:/Ironhack/ironhack-w2-project/training.csv')
    print(data.head())