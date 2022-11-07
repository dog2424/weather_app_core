from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from http.client import BAD_REQUEST, CREATED, NOT_FOUND, OK
from app.utils.http_utils import HttpUtils
from app.models.list_response import ListResponse


class WeatherController:

    def weathers(request: HttpRequest) -> HttpResponse:
        if request.method == "GET":

            ListResponse: ListResponse = None
            status: int = BAD_REQUEST
