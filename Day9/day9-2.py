# Write a function that allow new countries to be added to the travel_log

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_visited, visits_done, cities_visited):
    new_country = {"country": country_visited}, {"visits": visits_done}, {"cities": cities_visited}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


