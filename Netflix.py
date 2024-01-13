import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Netflix CSV file into a DataFrame
netflix_data = pd.read_csv('netflix.csv')

# Data Exploration
# Display the first few rows of the dataset
print(netflix_data.head())

# Summary statistics of numerical columns
print(netflix_data.describe())

# Data types and missing values
print(netflix_data.info())

# Data Visualization
# Example: Distribution of release years of content
plt.figure(figsize=(12, 6))
sns.histplot(netflix_data['release_year'].dropna(), bins=30, kde=True)
plt.title('Distribution of Release Years of Netflix Content')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.show()

# Example: Pie chart for the distribution of content types (Movies vs. TV Shows)
content_types = netflix_data['type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(content_types, labels=content_types.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff'])
plt.title('Distribution of Content Types on Netflix')
plt.show()

# Genre Analysis
# Example: Count of content in each genre
genres = netflix_data['listed_in'].str.split(', ', expand=True).stack().value_counts()
plt.figure(figsize=(14, 6))
sns.barplot(x=genres.values, y=genres.index, palette='viridis')
plt.title('Number of Titles in Each Genre on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()