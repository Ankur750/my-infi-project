from django.contrib.gis.utils import GeoIP
g = GeoIP()
ip = request.META.get('REMOTE_ADDR', None)
if ip:
    city = g.city(ip)['city']
else:
    city = 'Rome' # default city

# proceed with city
