import json, inspect, requests

#stores IP Geo Info
class GeoIP(object):
    def __init__(self, IP):
       self.IP = IP

       r = requests.get('https://freegeoip.net/json/'+str(self.IP))

       dict1 = {}
       dict2 = {}
       temp = json.loads(json.dumps([r.text, dict2]))
       data = json.loads(temp[0])

       self.countryCode = data['country_code']
       self.countryName = data['country_name']
       self.regionCode = data['region_code']
       self.regionName = data['region_name']
       self.city = data['city']
       self.zipCode = data['zip_code']
       self.timeZone = data['time_zone']
       self.latitude = data['latitude']
       self.longitude = data['longitude']
       self.metroCode = data['metro_code']

    def getData(self):
        return self.data

    def __str__(self):
        #provides a dump of all instance variables
        return str(self.__dict__)

    #provides a dump of all instance variables as json
    def json_dump(self):
        return json.dumps(self.__dict__)
