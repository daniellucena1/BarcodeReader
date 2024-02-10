from src.views.http_types.http_response import HttpResponse
from src.errors.errors_type.http_unprocessable_entity import HttpeUnprocessableEntityError

def handler_errors(error: Exception) -> HttpResponse: 
    if isinstance(error, HttpeUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "datail": str(error)
            }]
        }
    )
