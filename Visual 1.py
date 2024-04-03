import pandas as pd

# Load the dataset
file_path = r'D:\NEU\Fall 2023-Sem1\Computation and Vis\Final Project\Tableau IP\updated_athlete_events_with_gdp_imputed.csv'
new_data = pd.read_csv(file_path)

# Creating the required table from the new data

# Grouping by year, participant country, and participant continent
new_grouped_data = new_data.groupby(['Year', 'participant_country', 'Participant_Continent','host_country'])

# Calculating the number of each type of medal won
new_medal_counts = new_grouped_data['Medal'].value_counts().unstack().fillna(0)
new_medal_counts = new_medal_counts[['Bronze', 'Gold', 'Silver']]  # Reordering columns

# Calculating total medals
new_medal_counts['Total Medals'] = new_medal_counts.sum(axis=1)

# Getting GDP of the country that year
new_gdp_data = new_grouped_data['GDP'].mean()  # Assuming mean GDP of that year represents the country's GDP

# Season
new_season_data = new_grouped_data['Season'].first()  # Assuming the first entry represents the season for that year

# Counting Indoor and Outdoor game medals
new_indoor_outdoor_medal_counts = new_grouped_data['Sport Indoor/Outdoor'].value_counts().unstack().fillna(0)
new_indoor_outdoor_medal_counts.columns = ['Indoor Games Medal Count', 'Outdoor Games Medal Count']

# Merging all the calculated data
new_final_table = pd.concat([new_medal_counts, new_gdp_data, new_season_data, new_indoor_outdoor_medal_counts], axis=1)

# Resetting index for better readability
new_final_table.reset_index(inplace=True)

# Displaying the first few rows of the table
print(new_final_table.head())
new_final_table.to_csv(r'D:\NEU\Fall 2023-Sem1\Computation and Vis\Final Project\Tableau IP\final.csv')
