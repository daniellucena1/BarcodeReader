from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        resposability for intaracting with HTTP
    '''

    def validade_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # logic of deals rules
        print('Estou na minha view')
        # http return
        return HttpResponse(status_code=200, body={"hello": "world"})
