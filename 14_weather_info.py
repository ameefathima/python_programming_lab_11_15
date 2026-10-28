# Program to Process Weather Information Using JSON and Pandas

import json
import pandas as pd

# Sample JSON dataset
data = '''
{
    "weather": [
        {"location": {"city": "Kochi"}, "temperature": 30, "humidity": 75},
        {"location": {"city": "Thrissur"}, "temperature": 32, "humidity": 70},
        {"location": {"city": "Kozhikode"}, "temperature": 29, "humidity": 80}
    ]
}
'''

# Parse JSON data
weather_data = json.loads(data)

# Convert JSON into tabular format
df = pd.json_normalize(weather_data["weather"])

# Rename columns correctly
df = df.rename(columns={
    "location.city": "City",
    "temperature": "Temperature",
    "humidity": "Humidity"
})

# Display weather information
print("Weather Information:")
print(df)

# Calculate average temperature and humidity
print("\nAverage Temperature:", round(df["Temperature"].mean(), 2))
print("Average Humidity:", round(df["Humidity"].mean(), 2))

# Display weather details for each city
print("\nWeather Report for Each City:")
for index, row in df.iterrows():
    print(row["City"], "- Temperature:", row["Temperature"],
          "°C, Humidity:", row["Humidity"], "%")