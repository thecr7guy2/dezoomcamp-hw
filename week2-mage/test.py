import pandas as pd

# Example timestamp
timestamp = 1601512279000

# Convert the Unix timestamp in milliseconds to a datetime object
date_time = pd.to_datetime(timestamp, unit='ms')

# Extract the date part
date = date_time.date()

print(date)
