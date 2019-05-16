import pandas as pd
from pandas import Series, DataFrame
#Series and DataFrame are the workhorse of pandas 

#Lets start with: Series([], index =[]). Series is a arry like object 

# CREATING PANDAS SERIES 
pathas = pd.Series(["vijay", "heidi", "heidi", 3])
print(pathas) # when i print a Series, series automatically provides the index number

# HOW TO ACCESS AN ELEMENT IN PANDAS 
print(pathas[0]) #very similar to accessing an element from a list 

# HOW TO CHANGES THE INDEX of SERIES 
pathas = pd.Series(["vijay", "heidi", "heidi", 3], index = ["worst", "the best", "awesome baby", "random"])
print(pathas) #pretty straight forward to change the default index of a series 

#HOW TO FILTER PANDAS 
ages = [10,20,30,40]
pets_names = ["mickey", "rosie", "kitty", "rufus"]
my_data = pd.Series(ages, index = pets_names)
print(my_data) #expected an index of names and column of ages

multiply_series = my_data * 2
print(multiply_series)

filter_series = my_data[my_data > 20]
print(filter_series)

exp_series = my_data ** 2
print(exp_series)

# DATAFRAMES is excel. A rectangular table of data and contains an ordered collection of columns
#The DataFrame has both a row and column index; it can be thought of as a dict of Series all sharing the same index

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

print(data)

df = pd.DataFrame(data)
print(df)

# HOW TO REORDER COLUMNS 
df = pd.DataFrame(data, columns = ["year", "state", "pop"])
print(df)

# How to retrieve columns (dict notation)
df.year

# HOW TO RETRIEVE COLUMNS (Attribute NOTATION)
df['year']

# CHANGE COLUMN NAMES
df.columns

df.columns = ["years", "states", "population"]
df

# HOW TO CHANGE COLUMN NAMES OF DATAFRAME 

# USING RENAME FUNCTION
df.rename(columns={'population':'pops'}, inplace=True)
df


# HOW TO RETRIEVE ROW
#Rows can also be retrieved by position or name with the special loc attribute:

# Lets first index rows 
df2 = pd.DataFrame(data, index = ['first','second','thrid','fourth','fivth', 'sixth'])

df2

#HOW TO RETRIEVE ROW USING INDEX for a DF
df2.loc["sixth"]

# HOW TO RETREIEVE ROW WITHOUT A INDEX

#USE ILOC

df2.iloc[5]

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['col_one', 'col_two'])

df

# HOW TO SUM BY TOTAL COLUMN
df.sum()


