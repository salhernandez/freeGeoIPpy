# freeGeoIPpy
A python wrapper for freegeoip.net
## sample use
```
from freeGeoIPpy import *
geoIP = GeoIP("172.217.5.78")
print str(geoIP)
print geoIP.city
```
