import pandas as pd

# Load the datasets
athlete_events = pd.read_csv('athlete_events.csv')
gdp = pd.read_csv('gdp.csv')  # Assuming 'gdp.csv' is the path to your GDP data
world_cities = pd.read_csv('world_cities.csv')  # Assuming 'world_cities.csv' contains city-country mapping

# Handling null values in athlete_events
numeric_cols = ['Age', 'Height', 'Weight']
for col in numeric_cols:
    athlete_events[col].fillna(athlete_events[col].mean(), inplace=True)
athlete_events['Medal'].fillna('None', inplace=True)

# Filtering the athlete_events data for the year 1960 onwards
athlete_events = athlete_events[athlete_events['Year'] >= 1960]

# Additional code for city to country mapping
city_to_country_specific = {
    "lake placid": "United States",
    "torino": "Italy",
    "athina": "Greece",
    "cortina d'ampezzo": "Italy",
    "montreal": "Canada",
    "chamonix": "France",
    "sankt moritz": "Switzerland",
    # Add more mappings as needed
}

# Update the city to country mapping dictionary with specific cities
athlete_events['City'] = athlete_events['City'].str.lower().str.strip().str.replace('.', '', regex=False)
city_to_country = world_cities.set_index('city')['country'].to_dict()
city_to_country.update(city_to_country_specific)

# Apply the mapping to the 'host_country' column
athlete_events['host_country'] = athlete_events['City'].map(city_to_country)

# Verify there are no more missing 'host_country' values
assert athlete_events['host_country'].isnull().sum() == 0, "There are still missing 'host_country' values"

# Transforming GDP data to a row-based format
gdp_row_based = pd.melt(gdp,
                        id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                        var_name='Year',
                        value_name='GDP')

# Mapping GDP values from the GDP dataset to the athlete events dataset based on 'Year' and 'participant_country'
gdp_dict = gdp_row_based.set_index(['Country Name', 'Year'])['GDP'].to_dict()
athlete_events['GDP'] = athlete_events.apply(
    lambda row: gdp_dict.get((row['participant_country'], str(row['Year'])), None), axis=1
)

# Save the transformed data
athlete_events.to_csv('final_athlete_events_with_gdp.csv', index=False)
