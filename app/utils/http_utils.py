import json
from types import SimpleNamespace
from typing import Any

from django.http import HttpRequest, HttpResponse


class HttpUtils:

    def getBody(request: HttpRequest) -> Any:
        body: Any = None

        if request.body is not None:
            body_unicode = request.body.decode('utf-8')

            try:
                body = json.loads(
                    body_unicode, object_hook=lambda d: SimpleNamespace(**d))
            except ValueError:
                pass

        return body

    def getContent(response: HttpResponse) -> Any:
        body_unicode = response.content.decode('utf-8')
        body = json.loads(
            body_unicode, object_hook=lambda d: SimpleNamespace(**d))

        return body

    def objectToJson(object: Any) -> str:
        result = None
        if object is not None:
            result = json.dumps(object, default=lambda o: o.__dict__)

        return result
