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





