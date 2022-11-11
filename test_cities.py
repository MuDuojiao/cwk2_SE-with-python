from cities import City, CityCollection
from utils import read_attendees_file
from pytest import raises
import pandas

global collection, conference_city
collection = read_attendees_file('test.csv')
conference_city = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)

def test_invalid_num():
    with raises(ValueError):
        City('Zurich','SW',-1,47.22,8.33)

def test_invalid_lat():
    with raises(ValueError):
        City('Zurich','SW',1,100,100)

def test_invalid_lon():
    with raises(ValueError):
        City('Zurich','SW',1,47.22,200)

# City methods work correctly for all modes of transportation
def test_distance_to():
    conference_city = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)
    # 1,China,,Haikou,20.0423626,110.3409936,11579.579297576207
    Haikou = City('Haikou','China',1,20.0423626,110.3409936)
    assert int(Haikou.distance_to(conference_city)) == 7191

def test_tran_public():
    conference_city = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)
    test_city = City('Test','Test',3,37.7792808,-122.5)
    assert int(test_city.co2_to(conference_city)) == 102578

def test_tran_short():
    conference_city = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)
    test_city = City('Test','Test',3,37.7792808,-122)
    assert int(test_city.co2_to(conference_city)) == 665562

def test_tran_long():
    conference_city = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)
    test_city = City('Test','Test',3,40,-122)
    assert int(test_city.co2_to(conference_city)) == 4109742

def test_counties():
    countries_list = ['Algeria','Argentina','Armenia','China','India']
    assert collection.countries().sort() == countries_list.sort()

def test_attendees():
    assert collection.total_attendees() == 15

def test_travel_by_country():
    countryList = ['Algeria', 'Argentina', 'Armenia', 'China', 'India']
    distList = [17280.57675345718, 89291.27281642753,2993.719887070337, 7191.6986821142455, 50319.82969563662]
    finalDict = {}
    for i in range(len(countryList)):
        finalDict[countryList[i]] = distList[i]
    assert collection.travel_by_country(conference_city) == finalDict

def test_co2_by_country():
    countryList = ['Algeria', 'Argentina', 'Armenia', 'China', 'India']
    co2List = [5184173.026037154, 26787381.84492826,748429.9717675842, 1797924.6705285613, 15095948.908690985]
    finalDict = {}
    for i in range(len(countryList)):
        finalDict[countryList[i]] = co2List[i]
    assert collection.co2_by_country(conference_city) == finalDict

def test_sorted():
    Algiers = City('Algiers','Algeria',1,28.0000272,2.9999825)
    Buenos = City('Buenos Aires','Argentina',5,-34.6075616,-58.437076)
    Córdoba = City('Córdoba','Argentina',1,-32.0967361,-63.7940923)
    San = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)
    new_collection = CityCollection([Algiers,Buenos,Córdoba,San])
    emisList = [6650925.536438199, 15213617.035507616, 21941482.06965358, 27995521.955375608]
    cityList = ['Buenos Aires','Algiers','Córdoba','San Francisco']
    finalList = []
    for i in range(4):
        finalList.append((cityList[i],emisList[i]))
    print(new_collection.sorted_by_emissions())
    print(finalList)
    assert new_collection.sorted_by_emissions() == finalList

# csvData = pandas.read_csv('test.csv')
# cityList = list(csvData['city'])
# countryList = list(csvData['country'])
# numList = list(csvData['N'])
# lat = list(csvData['lat'])
# lon = list(csvData['lon'])
# all = []
# for i in range(len(numList)):
#     city = City(cityList[i],countryList[i],numList[i],lat[i],lon[i])
#     all.append(city)
# # conf = all[0] # 42758749.790461935
# # new_collection = CityCollection(all[1:])
# # emission = new_collection.total_co2(conf)
# # print(emission)


# Algiers = City('Algiers','Algeria',1,28.0000272,2.9999825)
# Buenos = City('Buenos Aires','Argentina',5,-34.6075616,-58.437076)
# Córdoba = City('Córdoba','Argentina',1,-32.0967361,-63.7940923)
# San = City('San Francisco', 'United States', 0, 37.7792808, -122.4192363)


# new_collection = CityCollection([Algiers,Buenos,Córdoba,San])
# test_sorted()
# # Algiers
# coll1 = CityCollection([Buenos,Córdoba,San])
# emis1 = coll1.total_co2(Algiers)
# print(emis1)
# # Buenos
# coll2 = CityCollection([Algiers,Córdoba,San])
# emis2 = coll2.total_co2(Buenos)
# print(emis2)
# # Córdoba
# coll3 = CityCollection([Algiers,Buenos,San])
# emis3 = coll3.total_co2(Córdoba)
# print(emis3)
# # San
# coll4 = CityCollection([Algiers,Buenos,Córdoba])
# emis4 = coll4.total_co2(San)
# print(emis4)

# emisList = [emis1,emis2,emis3,emis4]
# print(sorted(emisList))
# # for i in range(len(sorted(emisList))):
# #     print(sorted(emisList)[i].ind)
# print(sorted(emisList).index)
# # [6650925.536438199, 15213617.035507616, 21941482.06965358, 27995521.955375608]

# # print(emiList)

# # # [5184173.026037154, 18968813.03457246, 3842535.8947659936, 3976032.915589805, 748429.9717675842, 1797924.6705285613, 15095948.908690985]
# # # [5184173.026037154, 26787381.84492826,748429.9717675842, 1797924.6705285613, 15095948.908690985]
# # one = [18968813.03457246, 3842535.8947659936, 3976032.915589805] # 26787381.84492826
# # print(sum(one))

