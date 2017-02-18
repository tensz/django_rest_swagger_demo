from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django_rest_swagger_demo import  request_logger


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        request_logger.error(
            '%s %s',
            str(context['view'].get_view_name()),
            str(exc.message)
        )
        return Response({"result": "error", "data": exc.message})
    info = {"result": 'error', 'data': response.data}
    response.data = info
    return response

