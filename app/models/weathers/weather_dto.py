from app.models.weathers.weather import Weather


class WeatherDto():

    def __init__(self, id: int, description: str, temp: int, lon: int, lat: int):
        self.id = id
        self.description = description
        self.temp = temp
        self.lat = lat
        self.lon = lon

    @classmethod
    def fromWeather(cls, weather: Weather):
        dto = None
        if weather is not None:
            dto = WeatherDto(id=weather.id, description=weather.description,
                             lat=weather.lat, lon=weather.lat, temp=weather.temp)

        return dto

    @classmethod
    def toWeather(cls, weatherDto) -> Weather:

        weather = Weather()

        if hasattr(weatherDto, 'id'):
            weather.id = weatherDto.id
        if hasattr(weatherDto, 'lat'):
            weather.lat = weatherDto.lat
        if hasattr(weatherDto, 'lon'):
            weather.lon = weatherDto.lon
        if hasattr(weatherDto, 'temp'):
            weather.temp = weatherDto.temp
        if hasattr(weatherDto, 'description'):
            weather.description = weatherDto.description

        return weather
