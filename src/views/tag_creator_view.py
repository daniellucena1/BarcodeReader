from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import CreateTagController

class TagCreatorView:
    '''
        resposability for intaracting with HTTP
    '''

    def validade_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = CreateTagController()

        body = http_request.body
        product_code = body["product_code"]

        # logic of business rules
        formatted_response = tag_creator_controller.create(product_code)

        # http return
        return HttpResponse(status_code=200, body=formatted_response)
