import pandas as pd
import matplotlib.pyplot as plt

# Function to categorize GDP into numerical ranges
def categorize_gdp_numerical(gdp):
    if gdp < 1e9:
        return 'Less than 1 billion'
    elif gdp < 1e10:
        return '1 billion to 10 billion'
    elif gdp < 1e11:
        return '10 billion to 100 billion'
    elif gdp < 1e12:
        return '100 billion to 1 trillion'
    else:
        return 'More than 1 trillion'

# Function to categorize GDP into economic terms
def categorize_gdp_categorical(gdp):
    if gdp < 1e10:
        return 'Low-Income Economies'
    elif gdp < 1e11:
        return 'Lower-Middle-Income Economies'
    elif gdp < 1e12:
        return 'Upper-Middle-Income Economies'
    else:
        return 'High-Income Economies'

# Load the dataset
file_path = r'D:\NEU\Fall 2023-Sem1\Computation and Vis\Final Project\Tableau IP\updated_athlete_events_with_gdp_imputed.csv'  # Replace with your file path
olympic_data = pd.read_csv(file_path)

# Apply the GDP categorizations
olympic_data['GDP Numerical Category'] = olympic_data['GDP'].apply(categorize_gdp_numerical)
olympic_data['GDP Categorical Category'] = olympic_data['GDP'].apply(categorize_gdp_categorical)

# Filter only medal winners
medal_winners = olympic_data[olympic_data['Medal'].notnull()]

# Aggregating medal counts for numerical categorization
medals_by_numerical_gdp = medal_winners.groupby('GDP Numerical Category')['Medal'].count().reset_index()

# Aggregating medal counts for categorical categorization
medals_by_categorical_gdp = medal_winners.groupby('GDP Categorical Category')['Medal'].count().reset_index()

# Creating bar charts for the distribution of medals in different GDP ranges
plt.figure(figsize=(12, 6))

# Bar chart for numerical categorization
plt.subplot(1, 2, 1)
plt.bar(medals_by_numerical_gdp['GDP Numerical Category'], medals_by_numerical_gdp['Medal'], color='lightblue')
plt.title('Medals Distribution - Numerical Categorization')
plt.xlabel('GDP Numerical Category')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)

# Bar chart for categorical categorization
plt.subplot(1, 2, 2)
plt.bar(medals_by_categorical_gdp['GDP Categorical Category'], medals_by_categorical_gdp['Medal'], color='lightgreen')
plt.title('Medals Distribution - Categorical Categorization')
plt.xlabel('GDP Categorical Category')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Define the path for the final CSV file
final_csv_path = r'D:\NEU\Fall 2023-Sem1\Computation and Vis\Final Project\Tableau IP\Final 2.csv'  # Replace with your desired output path

# Selecting columns to include in the final CSV file
columns_to_include = ['Name', 'Sex', 'Age', 'Team', 'Year', 'Season', 'Sport', 'Event', 'Medal',
                      'GDP', 'GDP Numerical Category', 'GDP Categorical Category',
                      'participant_country', 'Participant_Continent']

# Save the updated DataFrame to a CSV file
olympic_data[columns_to_include].to_csv(final_csv_path, index=False)
