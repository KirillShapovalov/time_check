from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from . import serializers
from .utils import check_time
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def time_check(request):
    if request.method == 'GET':
        if 'checktime' in request.headers:
            try:
                time_value = request.headers.get('checktime')
                res = check_time(time_value)
                result = {
                    'time from headers': bool(res),
                    'time for check': int(time_value),
                    'headers': request.headers
                }
                return Response(result)
            except ValueError:
                raise APIException('Entry data must be an integer!')

        if request.query_params.get('checktime'):
            try:
                time_value = request.query_params.get('checktime')
                res = check_time(time_value)
                result = {
                    'time from parameters': bool(res),
                    'time for check': int(time_value)
                }
                return Response(result)
            except ValueError:
                raise APIException('Entry data must be an integer!')
        else:
            result = {
                'data': 'no entry data'
            }
            return Response(result)

    if request.method == 'POST':
        serializer = serializers.TimeCheckSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            time = serializer.data.get('time')
            result = check_time(time)
            response = {
                'time from post': bool(result),
                'time for check': int(time)
            }
            return Response(response)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
