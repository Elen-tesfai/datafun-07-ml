import pandas as pd

# Load the data
nyc_df = pd.read_csv("GlobalLandTemperaturesByCity.csv")

# Filter for New York City
nyc_df = nyc_df[nyc_df['City'] == 'New York']

# Convert 'dt' to datetime
nyc_df['dt'] = pd.to_datetime(nyc_df['dt'])

# Filter for January data
january_data = nyc_df[nyc_df['dt'].dt.month == 1]

# Drop rows with missing AverageTemperature
january_data = january_data.dropna(subset=['AverageTemperature'])

# Extract the year for feature
january_data['Year'] = january_data['dt'].dt.year

# Display the first few rows of the prepared DataFrame
print(january_data[['dt', 'AverageTemperature', 'Year']].head())