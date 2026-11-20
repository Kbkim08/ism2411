# ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer

# Exercise 1
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# Exercise 2
south = df[df['region']=='South']

print(len(south))
print(south.head())

# Exercise 3
top5 = df.sort_values('revenue', ascending = False).head(5)

print(top5)

# Exercise 4
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

# Exercise 5

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())

print(df['per_unit'].mean())

# Exercise 6
print(df['region'].unique())

print(df['region'].value_counts())

# Exercise 7

subset = df[['region', 'product', 'revenue']]

print(subset.shape)

# Exercise 8

df.to_csv('data/explored.csv', index = False)


# Assessment
# 1. Boolean filter will only keep rows that successfully
# meet a condition and move the rows that dont.

# 2. The difference between df['revenue'] and df[['revenue']] is
# that df['revenue'] returns one column, a series, and df[['revenue']]
# returns a DataFrame. Still one column, but in it's DataFrame form.

# 3. Pandas works quickly when it comess to automating data analysis
# on much larger datasets, making the process repeatable and
# alot faster. Meanwhile in Excel, you have to go in manually.