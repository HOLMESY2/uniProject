import pandas as pd
from geopy.extra.rate_limiter import RateLimiter

df = pd.read_json("Data/2021_NOVEMBER.json")
df.head()
print(df)

geocode = RateLimiter(locator.geocode, min_delay_seconds=1)