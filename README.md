# freeGeoIPpy
A python wrapper for freegeoip.net
## sample use
### input
```
from freeGeoIPpy import *
geoIP = GeoIP("172.217.5.78")
print str(geoIP)
print geoIP.city
```
### putput
```
{'city': u'Mountain View', 'countryCode': u'US', 'IP': '172.217.5.78', 'zipCode': u'94043', 'longitude': -122.0574, 'countryName': u'United States', 'regionCode': u'CA', 'metroCode': 807, 'latitude': 37.4192, 'timeZone': u'America/Los_Angeles', 'regionName': u'California'}
Mountain View
```
