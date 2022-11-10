from cities import City, CityCollection
from pathlib import Path
import csv

# cities = read_attendees_file('attendee_locations.csv')
def read_attendees_file(filepath: Path) -> CityCollection:
    mycsv = open(filepath,'r')
    myfile = csv.DictReader(mycsv)
    cityList = []
    for row in myfile:
        name = row['city']
        country = row['country']
        number = int(row['N'])
        lat = float(row['lat'])
        lon = float(row['lon'])
        city = City(name=name,country=country,numAtt=number,lat=lat,lon=lon)
        cityList.append(city)
    city_collection = CityCollection(cityList)
    return city_collection