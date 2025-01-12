import random
from datetime import datetime, timedelta

# Function to generate a random date and time
def generate_random_datetime(start_date, end_date):
    a = end_date - start_date
    b = random.randint(0, int(a.total_seconds()))
    random_datetime = start_date + timedelta(seconds=b)
    return random_datetime

# Define start and end date range
start_date = datetime(2020, 1, 1)  # Starting date
end_date = datetime(2025, 12, 31)  # Ending date

# Generate a random date and time
random_datetime = generate_random_datetime(start_date, end_date)
print("Random Date and Time:", random_datetime)
