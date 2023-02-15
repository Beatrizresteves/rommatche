# coding: utf-8
import json

from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .service import quarto_svc

# from .serializers import QuartoSerializer

from ..commons.django_views_utils import ajax_login_required


# class LatestQuartosList(APIView):
#     def get(self, request, format=None):
#         quartos = Quarto.objects.all()
#         serializer = QuartoSerializer(quartos, many=True)
#         return Response(serializer.data)


@csrf_exempt
@ajax_login_required
def add_quarto(request):
    quarto = quarto_svc.add_quarto(request.POST)
    return JsonResponse(quarto)


@ajax_login_required
def list_quartos(request):
    quartos = quarto_svc.list_quartos()
    return JsonResponse({"quartos": quartos})
