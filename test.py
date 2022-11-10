print('Hello')

data = [(1,2,3), (4,5,6), (7,3,9)]
sorted_by_second = sorted(data, key=lambda tup: tup[1])

list = [(699815.6704092632, 'Salta'), (950677.5971336586, 'Córdoba'), (956005.681820109, 'Pergamino'), (1614266.8042488508, 'Algiers'), (3236959.610817559, 'Haikou'), (5235357.798854528, 'La Plata'), (8338306.132888891, 'Gyumri'), (9098891.520818884, 'Hainan'), (10573304.449569643, 'Goa'), (10690504.806883264, 'Mendoza'), (11104298.429366708, 'Gandhinagar'), (18049501.420299888, 'Yerevan'), (22447556.426435165, 'Buenos Aires'), (26989085.442221146, 'Guwahati')]
print(list[:3])
others = list[3:]
print(others)

def get(a:int=1):
    print(a)

get(5)

name = 'La Plata'
print(name.lower().replace(' ','_') + '.png')