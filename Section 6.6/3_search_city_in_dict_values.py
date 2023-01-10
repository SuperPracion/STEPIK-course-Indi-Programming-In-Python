countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()

for country, cities in countries.items():
    if city in cities:
        print(f'INFO: {city} is a city in {country}')
        break
else:
    print(f'ERROR: Country for {city} not found')