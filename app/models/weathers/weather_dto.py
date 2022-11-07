from app.models.weathers.weather import Weather


class WeatherDto():

    def __init__(self, id: int, description: str, temp: int, lon: int, lat: int):
        self.id = id
        self.description = description
        self.temp = temp
        self.lat = lat
        self.lon = lon

    @classmethod
    def fromWeater(cls, weather: Weather):
        dto = None
        if weather is not None:
            dto = WeatherDto(id=weather.id, description=weather.description,
                             lat=weather.lat, lon=weather.lat, temp=weather.temp)
