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
    RequestStatus,
)
import db_pb2_grpc
import os
from db_actions import (
    get_box,
    get_all_boxes,
    get_box_by_category,
    get_box_by_datetime,
    create_box,
    update_box,
    delete_box,
)
from dotenv import load_dotenv
import datetime
from utils import (
    convert_proto_2_datetime,
    convert_datetime_2_proto_timestamp,
)

load_dotenv()


PORT = int(os.getenv("GRPC_PORT"))


class DbService(db_pb2_grpc.DatabaseServiceServicer):
    def GetBox(self, request, context):
        document = get_box(request.id)
        created_at_pt = convert_datetime_2_proto_timestamp(document["created_at"])

        document["created_at"] = created_at_pt
        return GetBoxResponse(
            box = document,
            status = RequestStatus.OK
        )

    def GetBoxes(self, request, context):
        documents = get_all_boxes()
        
        documents_array = []

        for document in documents:
            created_at_pt = convert_datetime_2_proto_timestamp(document["created_at"])
            document["created_at"] = created_at_pt

            documents_array.append(document)

        return GetBoxesResponse(
            box = documents_array,
            status = RequestStatus.OK
        )
    
    def CreateBox(self, request, context):
        box_data = request.box
        create_box(box_data)

        return CreateBoxResponse(
            status = RequestStatus.OK
        )

    def UpdateBox(self, request, context):
        new_box_data = request.box
        update_box(new_box_data)

        return UpdateBoxResponse(
            status = RequestStatus.OK
        )

    def DeleteBox(self, request, context):
        box_id = request.id
        delete_box(box_id)

        return DeleteBoxResponse(
            status = RequestStatus.OK
        )

    def GetBoxesInCategory(self, request, context):
        category = request.category
        documents = get_box_by_category(category)
        
        documents_array = []

        for document in documents:
            created_at_pt = convert_datetime_2_proto_timestamp(document["created_at"])
            document["created_at"] = created_at_pt

            documents_array.append(document)
        
        return GetBoxesResponse(
            box = documents_array,
            status = RequestStatus.OK
        )

    def GetBoxesInTimeRange(self, request, context):
        start_time_pt = request.start_time
        end_time_pt = request.end_time

        start_time = convert_proto_2_datetime(start_time_pt)
        end_time = convert_proto_2_datetime(end_time_pt)

        documents = get_box_by_datetime(start_time, end_time)

        documents_array = []

        for document in documents:
            created_at_pt = convert_datetime_2_proto_timestamp(document["created_at"])
            document["created_at"] = created_at_pt

            documents_array.append(document)

        return GetBoxesResponse(
            box = documents_array,
            status = RequestStatus.OK

        )


def serve():
    print("Initializing the server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    db_pb2_grpc.add_DatabaseServiceServicer_to_server(

        DbService(), server

    )

    server.add_insecure_port(f"[::]:{PORT}")

    server.start()

    server.wait_for_termination()


if __name__ == "__main__":

    serve()