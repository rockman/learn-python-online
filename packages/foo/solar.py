
from .alpha import sun
from .beta.moon import the_moon


SOLAR_PUBLIC = 'SOLAR_PUBLIC'
_SOLAR_PRIVATE = '_SOLAR_PRIVATE' 

def the_solar():
    return sun.the_sun(), the_moon()
