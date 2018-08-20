# class SpaceAge(object):
#     def __init__(self, seconds):
#         self._sec = seconds
#         self.earthsec = 31557600
#
#     def on_mercury(self):
#         return round((self._sec/self.earthsec)/0.2408467,2)
#     def on_venus(self):
#         return round((self._sec/self.earthsec)/0.61519726,2)
#     def on_earth(self):
#         return round((self._sec/self.earthsec),2)
#     def on_mars(self):
#         return round((self._sec/self.earthsec)/1.8808158,2)
#     def on_jupiter(self):
#         return round((self._sec/self.earthsec)/11.862615,2)
#     def on_saturn(self):
#         return round((self._sec/self.earthsec)/29.447498,2)
#     def on_uranus(self):
#         return round((self._sec/self.earthsec)/84.016846,2)
#     def on_neptune(self):
#         return round((self._sec/self.earthsec)/164.79132,2)
#     @property
#     def seconds(self):
#         return self._sec

# better solution
class SpaceAge(object):

    planet_times = {
        'mercury' : 0.2408467,
        'venus' : 0.61519726,
        'earth' : 1,
        'mars' : 1.8808158,
        'jupiter' : 11.862615,
        'saturn' : 29.447498,
        'uranus' : 84.016846,
        'neptune' : 164.79132
    }

    earth_seconds = 31557600.0

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, v in self.planet_times.items():
            setattr(self, "on_" + planet, lambda v=v: round(self.seconds / (self.earth_seconds * v), 2))
