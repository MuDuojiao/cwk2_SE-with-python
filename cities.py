from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt

@ dataclass
class City:
    # name: str
    # country: str
    # numAtt: int
    # lat: float
    # lon: float

    def __init__(self,name:str,country:str,numAtt:int,lat:float,lon:float) -> None:
        if numAtt < 0:
            raise ValueError('**The number of attendees must be positive integer**')
        if lat<-90 or lat>90:
            raise ValueError('**Latitude should be restricted to the -90 to 90**')
        if lon<-180 or lon>1800:
            raise ValueError('**Longitude should be restricted to the -180 to 180**')
        self.name = name
        self.country = country
        self.numAtt = numAtt
        self.lat = lat
        self.lon = lon
            
    def distance_to(self, other: 'City') -> float:
        lat1 = self.lat
        lon1 = self.lon
        lat2 = other.lat
        lon2 = other.lon
        R = 6371
        part1 = math.sin((lat2-lat1)/2)**2
        part2 = math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
        distance = 2*R*math.asin(math.sqrt(part1+part2))
        return distance
        
    def co2_to(self, other: 'City') -> float:
        dist = self.distance_to(other)
        co2 = 0
        if dist<=1000:
            co2 = 200*dist
        elif dist>1000 and dist<=8000:
            co2 = 250*dist
        elif dist>8000:
            co2 = 300*dist
        return co2

class CityCollection:
    def __init__(self,cities:List[City]) -> None:
        self.cities = cities

    # should return a list of *unique* countries that the cities in the collection belong to
    # 返回的是国家的list
    def countries(self) -> List[str]:
        counList = []
        cities = self.cities
        for i in range(len(cities)):
            counList.append(cities[i].country)
        return list(set(counList))

    # the number of all the attendees
    def total_attendees(self) -> int:
        cities = self.cities
        attendees = []
        for i in range(len(cities)):
            attendees.append(cities[i].numAtt)
        return sum(attendees)

    # 所有attendees的旅行距离
    def total_distance_travel_to(self, city: City) -> float:
        tra_by_coun = self.travel_by_country(city)
        total = 0
        for i in tra_by_coun:
            total += tra_by_coun[i]
        return total

    # country:distance 每个国家的旅行总距离
    # 该国家的人数 * 该国家到 city 的距离
    def travel_by_country(self, city: City) -> Dict[str, float]:
        cities = self.cities
        tra_by_coun = {}
        for i in range(len(cities)):
            name = cities[i].name
            numAtt = cities[i].numAtt
            dist = cities[i].distance_to(city)
            tra_by_coun[name] = numAtt*dist
        return tra_by_coun

    # 所有参会人的 CO2 消耗
    def total_co2(self, city: City) -> float:
        co2_by_coun = self.co2_by_country(city)
        total = 0
        for i in co2_by_coun:
            total += co2_by_coun[i]
        return total

    # 每个国家参会人的 CO2 消耗
    def co2_by_country(self, city: City) -> Dict[str, float]:
        cities = self.cities
        co2_by_coun = {}
        for i in range(len(cities)):
            name = cities[i].name
            numAtt = cities[i].numAtt
            co2 = cities[i].co2_to(city)
            co2_by_coun[name] = numAtt*co2
        return co2_by_coun
        
    def summary(self, city: City):
        cities = self.cities
        hostCity = city.name
        hostCountry = city.country
        print('Host city:', hostCity, '(',hostCountry,')')
        totalCO2 = round(self.total_co2(city)/1000)
        print('Total CO2:',totalCO2)
        totalAtt = self.total_attendees()
        print('Total attendees travelling to', hostCity, 'from', len(cities), 'different cities:', totalAtt)

    # 返回一个被排列的List [city_name,co2_emissions]
    # 这个城市 以及 这个城市作为举办城市的CO2的总排放量 
    # 根据所有 attendees 的 CO2 emission 排列
    # lowest --> highest
    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        cities = self.cities
        totalList = []
        for i in range(len(cities)):
            city = cities[i]
            total_co2 = self.total_co2(city)
            city_tuple = (city.name,total_co2)
            totalList.append(city_tuple)
        sorted_by_emission = sorted(totalList, key=lambda tup: tup[1])
        return sorted_by_emission


    def plot_top_emitters(self, city: City, n: int=10, save: bool=False):
        co2_by_country = self.co2_by_country(city) # {country:distance}
        sorted_co2 = sorted(zip(co2_by_country.values(), co2_by_country.keys()),reverse=True)
        n_countries = sorted_co2[:n] # 前n个 里面的每个元素的类型是 元组
        others = sorted_co2[n:] # 后面所有
        other_sum = 0
        for i in range(len(others)):
            other_sum += others[i][0]
        other = (other_sum,'All other countries')
        n_countries.append(other)
        fig=plt.figure()
        for i in range(len(n_countries)):
            plt.bar(n_countries[i][1],n_countries[i][0]/1000)
        plt.title('Total emissions from each country(top' + str(n)+')')
        plt.ylabel('Total emissions(tonnes CO2)')
        plt.show()
        if save is True:
            name = city.name.lower().replace(' ','_') + '.png'
            fig.savefig('./'+name)
        else:
            plt.show()



# zurich = City('Zurich','SW',1,47.22,8.33)
# greenwich = City('London','UK',15,0,0)
# conference_city = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)
# buenos_aries = City('Buenos aries','SW',5,-34.6075616,-58.437076)
# list_of_cities = [zurich,greenwich,conference_city]
# city_collection = CityCollection(list_of_cities)

# collection = read_attendees_file('attendee_locations.csv')
# countries = collection.countries()
# attendees = collection.total_attendees()
# travel_by_country = collection.co2_by_country(zurich)

# print(max(travel_by_country,key=lambda x:travel_by_country[x]))
# collection.plot_top_emitters(zurich)