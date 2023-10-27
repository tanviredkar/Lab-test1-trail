#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('shopping.csv')
df.head()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('shopping.csv')

plt.figure(figsize=(8, 6))
plt.scatter(df['Fresh'], df['Frozen'], alpha=0.5) 
plt.title('Scatter Plot of Fresh vs. Frozen')
plt.xlabel('Fresh')
plt.ylabel('Frozen')
plt.grid(True)

plt.show()


# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('shopping.csv')
selected_features = df[['Milk', 'Detergents_Paper', 'Delicassen']]
plt.figure(figsize=(8, 6))
correlation_matrix = selected_features.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, mask=correlation_matrix.isnull())
plt.title('Correlation Heatmap')
plt.show()
correlation_coefficients = correlation_matrix.stack().reset_index()
correlation_coefficients.columns = ['Feature 1', 'Feature 2', 'Correlation']
correlation_values = correlation_coefficients[correlation_coefficients['Feature 1'] != correlation_coefficients['Feature 2']]
correlation_values.reset_index(drop=True, inplace=True)
correlation_values


# In[4]:


import pandas as pd

# Read in the dataset shopping.csv
df = pd.read_csv('shopping.csv')

# Display the last five records of the dataset
last_five_records = df.tail()

# Print the last five records
print(last_five_records)


# In[ ]:




