import pandas as pd

# Load the dataset
file_path = r'D:\NEU\Fall 2023-Sem1\Computation and Vis\Final Project\Transformed data\final_athlete_events_with_gdp.csv'
athlete_events_with_gdp = pd.read_csv(file_path)

# Filter the dataset for the years 1960 to 2016
filtered_athlete_events_with_gdp = athlete_events_with_gdp[(athlete_events_with_gdp['Year'] >= 1960) & (athlete_events_with_gdp['Year'] <= 2016)]

# Calculate the overall mean GDP of the dataset
overall_mean_gdp = filtered_athlete_events_with_gdp['GDP'].mean()

# Fill missing GDP values with the overall mean GDP
filtered_athlete_events_with_gdp['GDP'].fillna(overall_mean_gdp, inplace=True)

# Save the updated dataset with imputed GDP values
updated_file_path = '/path/to/updated_athlete_events_with_gdp_imputed.csv'
filtered_athlete_events_with_gdp.to_csv(updated_file_path, index=False)
