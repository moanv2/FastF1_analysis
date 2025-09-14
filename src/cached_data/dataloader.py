import fastf1

# Tell FastF1 to use your raw folder for caching
fastf1.Cache.enable_cache('data/raw/')  # This line is key!

# Now when you load data, it goes to data/raw/
session = fastf1.get_session(2024, 'Monaco', 'R')
session.load()  # Downloads and saves to data/raw/