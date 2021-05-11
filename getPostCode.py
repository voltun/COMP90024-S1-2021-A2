from geopy.geocoders import Nominatim

def getPostCode(lat,long):
    coordinates = "{},{}".format(lat,long)
    geolocator = Nominatim(user_agent="test_app")
    #location = geolocator.reverse(-38.0649, 145.336)
    location = geolocator.reverse(coordinates)
    #using postcode as not all locations have suburbs listed
    try:
        return location.raw['address']['postcode']
    except:
        return None
