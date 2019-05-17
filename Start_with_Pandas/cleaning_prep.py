import pandas as pd
from pandas import Series, DataFrame 
import numpy as np
import matplotlib as mp
import seaborn as sb
import scipy as sp


raw_df = pd.read_csv("C:/Users/vipatha/Documents/2. 2019_DeepDives/Softlines_DeepDive/DD-Analysis/All_Softlines_CPLF/softlines_neg.csv",encoding = "ISO-8859-1")

raw_df.head()