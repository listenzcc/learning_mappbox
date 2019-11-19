import json
import random
import webbrowser
from pprint import pprint
from my_styles import styles

# Load location of China cities
with open('locations.json', 'r', encoding='utf-8') as f:
    locations = json.load(f)

# Random select a city
province, cities = random.choice(list(locations.items()))
city, center = random.choice(list(cities.items()))
# Reverse center to match mapbox API
center.reverse()
print(province, city, center)

# See what styles we have
names = styles.get_names()
for j, name in enumerate(names):
    print(j, name)
# Choose one style
i = input('Select a style to browse:')
# Swallow simple errors
try:
    name = names[int(i)]
except ValueError as e:
    name = names[0]
except IndexError as e:
    name = names[0]

# Make legal url
url = styles.make_url(name, 10, center)
pprint(url)

# Request url
webbrowser.open(url['url'])
