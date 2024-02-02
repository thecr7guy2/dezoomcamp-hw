import pandas as pd
from datetime import datetime, timedelta
import random 

# Example timestamp
# Define a start and end date
start_date = datetime(2020, 1, 1)
end_date = datetime(2022, 12, 31)

# Generate a random number of days to add
random_number_of_days = random.randint(0, (end_date - start_date).days)

# Optionally, add random hours, minutes, and seconds
random_hours = random.randint(0, 23)
random_minutes = random.randint(0, 59)
random_seconds = random.randint(0, 59)

# Create the random datetime
random_datetime = start_date + timedelta(days=random_number_of_days, 
                                         hours=random_hours, 
                                         minutes=random_minutes, 
                                         seconds=random_seconds)


print(random_datetime)

# Extract the date part
date = random_datetime.date()
# date2 = random_datetime.dt.date

print(date)
# print(date2)