import json
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from db_pb2 import GetAllBoxesRequest
import os
import grpc
from db_pb2_grpc import DatabaseServiceStub
from dotenv import load_dotenv
from django.http import JsonResponse
from utils import convert_proto_2_datetime

load_dotenv()

HOST = os.getenv("GRPC_HOST")
PORT = int(os.getenv("GRPC_PORT"))
channel = grpc.insecure_channel(f"{HOST}:{PORT}")
client = DatabaseServiceStub(channel)
class GetBoxes(GenericAPIView):
    def get(self, request):
        request = GetAllBoxesRequest()
        grpc_response = client.GetBoxes(request)
        boxes = grpc_response.box

        qs = []
        for box in boxes:
            temp_dict = {
                "name": box.name,
                "id": box.id,
                "price": box.price,
                "description": box.description,
                "category": box.category,
                "quantity": box.quantity,
                "created_at": str(convert_proto_2_datetime(box.created_at))
            }
            qs.append(temp_dict)

        response = qs
        
        return Response({
            "results": response
        }, status=status.HTTP_200_OK)
