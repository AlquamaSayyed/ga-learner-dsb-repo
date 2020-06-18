# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)

data.hist('Rating')

data = data[data['Rating']<=5]

data.hist('Rating')
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null], keys=['Total','Percent'], axis=1)

print(missing_data)

data.dropna(inplace = True)

total_null_1 = data.isnull().sum()

percent_null_1 = (total_null_1/data.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1],keys=['Total','Percent'], axis=1)

print(missing_data_1)
# code ends here


# --------------

#Code starts here
g = sns.catplot(data = data, x='Category', y='Rating', kind='box', height=10)

g.set_xticklabels(rotation=90)
g.set(title = "Rating vs Category [BoxPlot]")
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

data['Installs'] = data['Installs'].str.replace(r'\D', '').astype(int)
#print(data['Installs'])

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

ax = sns.regplot(data = data, x="Installs", y="Rating")
ax.set(title = 'Rating vs Installs [RegPlot]')


#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())

data['Price'] = data['Price'].str.replace(r'\D', '').astype(float)

ax = sns.regplot(x="Price", y="Rating", data=data) 
ax.set(title = 'Rating vs Price [RegPlot]')


#Code ends here


# --------------
#Code starts here
print(data['Genres'].unique())

data['Genres'] = data.Genres.str.split(';').str[0]
#print(data['Genres'])

gr_mean = data[['Genres','Rating']].groupby(['Genres'], as_index=False).mean()

gr_mean = gr_mean.sort_values(['Rating'])

print(gr_mean.head())
print(gr_mean.tail())

#Code ends here


# --------------

#Code starts here

print(data['Last Updated'])

data['Last Updated'] = pd.to_datetime(data['Last Updated'])

max_date = max(data['Last Updated'])

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

ax = sns.regplot(x="Last Updated Days", y="Rating", data=data)

ax.set(title = 'Rating vs Last Updated [RegPlot]')
#Code ends here


