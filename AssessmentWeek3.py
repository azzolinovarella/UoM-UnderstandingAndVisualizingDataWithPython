import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)

path = "Cartwheeldata.csv"

# First, you must import the cartwheel data from the path given above
df = pd.read_csv(path)  # using pandas, read in the csv data found at the url defined by 'path'

# Next, look at the 'head' of our DataFrame 'df'.
print(df.head())

# If you can't remember a function, open a previous notebook or video as a reference, or use your favorite search engine to look for a solution.

# ## Scatter plots

# First, let's looks at two variables that we expect to have a strong relationship, 'Height' and 'Wingspan'.

# Make a Seaborn scatter plot with x = height and y = wingspan using sns.scatterplot(x, y)

sct_plt1 = sns.scatterplot(x=df.Height, y=df.Wingspan, hue=df.Gender)
plt.show()

# How would you describe the relationship between 'Height' and 'Wingspan'?   
# Questions you can ask:
# * Is it linear?
# * Are there outliers?
# * Are their ranges similar or different?  
# 
# How else could you describe the relationship?

# Now let's look at two variables that we don't yet assume have a strong relationship, 'Wingspan' and 'CWDistance'

# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance
sct_plt2 = sns.scatterplot(x=df.Wingspan, y=df.CWDistance)
plt.show()

# How would you describe the relationship between 'Wingspan' and 'CWDistance'?   
# * Is it linear?
# * Are there outliers?
# * Are their ranges similar or different?  
# 
# How else could you describe the relationship?

# Let makes the same plot as above, but now include 'Gender' as the color scheme by including the argument
# ```
# hue=df['Gender']
# ```
# in the Seaborn function

# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance, and hue = gender
sct_plt3 = sns.scatterplot(x=df.Wingspan, y=df.CWDistance, hue=df.Gender)
plt.show()

# Does does this new information on the plot change your interpretation of the relationship between 'Wingspan' and 'CWDistance'?

# ## Barcharts
# Now lets plot barplots of 'Glasses'

# Make a Seaborn barplot with x = glasses and y = cartwheel distance
barplot1 = sns.barplot(x=df.Glasses, y=df.CWDistance)
plt.show()

# What can you say about the relationship of 'Glasses' and 'CWDistance'?

# Make the same Seaborn barplot as above, but include gender for the hue argument
barplot2 = sns.barplot(x=df.Glasses, y=df.CWDistance, hue=df.Gender)
plt.show()

# How does this new plot change your interpretation about the relationship of 'Glasses' and 'CWDistance'?
boxplot1 = sns.boxplot(df.Wingspan)
plt.show()

boxplot2 = sns.boxplot(df.CWDistance)
plt.show()
