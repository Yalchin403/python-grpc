from concurrent import futures
import random
import grpc

from db_pb2 import (
    Box,
    RequestStatus,
    GetBoxRequest,
    GetBoxResponse,
    GetAllBoxesRequest,
    GetBoxesResponse,
    CreateBoxRequest,
    CreateBoxResponse,
    UpdateBoxRequest,
    UpdateBoxResponse,
    DeleteBoxRequest,
    DeleteBoxResponse,
    GetBoxesInCategoryRequest,
    GetBoxesInTimeRangeRequest,
)
import db_pb2_grpc


class DbService(db_pb2_grpc.DatabaseServiceServicer):
    def GetBox(self, request, context):
        return super().GetBoxResponse(request, context)

    def GetBoxes(self, request, context):
        return super().GetBoxesResponse(request, context)
    
    def CreateBox(self, request, context):
        return super().CreateBoxResponse(request, context)

    def UpdateBox(self, request, context):
        return super().UpdateBoxResponse(request, context)

    def DeleteBox(self, request, context):
        return super().DeleteBoxResponse(request, context)

    def GetBoxesInCategory(self, request, context):
        return super().GetBoxesResponse(request, context)

    def GetBoxesInTimeRange(self, request, context):
        return super().GetBoxesResponse(request, context)



def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    db_pb2_grpc.add_DatabaseServiceServicer_to_server(

        DbService(), server

    )

    server.add_insecure_port("[::]:8000")

    server.start()

    server.wait_for_termination()



if __name__ == "__main__":

    serve()