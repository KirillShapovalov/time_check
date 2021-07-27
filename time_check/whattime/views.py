from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
import re
from urllib.parse import urlparse

from . import serializers


class TimeCheck(APIView):
    serializer_class = serializers.TimeCheckSerializer
    time_api_url = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
    url = 'http://127.0.0.1:8000/timecheck/'
    delta = 500

    def check_time(self, value):
        response = requests.get(self.time_api_url)
        if response.status_code == 200:
            time = response.json().get('unixtime')
            valid = abs(int(time) - int(value)) < self.delta
            return bool(valid)

    # def get(self):
    #     headers = {
    #         'check_time': '1627226722'
    #     }
    #     response = requests.get(self.url, headers=headers)
    #     check_time = self.request.query_params.get('check_time')
    #     r_head = response.request.headers['check_time']
    #     res_head = self.check_time(r_head)
    #     result_head = {
    #         'time': bool(res_head)
    #     }
    #     return Response(result_head)

    def get(self, time_check):
        time_check = self.request.query_params.get('checktime')
        res_par = self.check_time(time_check)
        result_par = {
            'time': bool(res_par)
        }
        return Response(result_par)

    def post(self, request):
        serializer = serializers.TimeCheckSerializer(data=request.data)
        if serializer.is_valid():
            time = serializer.data.get('time')
            result = self.check_time(time)
            response = {
                'time': bool(result)
            }
            return Response(response)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
