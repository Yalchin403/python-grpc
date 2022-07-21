import grpc
from db_pb2_grpc import DatabaseServiceStub
from db_pb2 import (
    Box,
    GetAllBoxesRequest,
    GetBoxRequest,
    GetBoxesInCategoryRequest,
    GetBoxesInTimeRangeRequest,
    DeleteBoxRequest,
    UpdateBoxRequest,
    CreateBoxRequest,
)
import os
from dotenv import load_dotenv
import datetime
from utils import convert_datetime_2_proto_timestamp, convert_proto_2_datetime


load_dotenv()

HOST = os.getenv("GRPC_HOST")
PORT = int(os.getenv("GRPC_PORT"))
channel = grpc.insecure_channel(f"{HOST}:{PORT}")
client = DatabaseServiceStub(channel)

# request = GetBoxRequest(id=2)
# print(client.GetBox(request))

request = GetAllBoxesRequest()
# boxes = client.GetBoxes(request)
# print(boxes)

# request = GetBoxesInCategoryRequest(category="music")
# print(client.GetBoxesInCategory(request))


# time range stuff starts


# start_time_dt = datetime.datetime(2020, 5, 17)
# end_time_dt = datetime.datetime.now()
# start_time = convert_datetime_2_proto_timestamp(start_time_dt)
# end_time = convert_datetime_2_proto_timestamp(end_time_dt)

# request = GetBoxesInTimeRangeRequest(start_time=start_time, end_time=end_time)
# print(client.GetBoxesInTimeRange(request))

# time range stuff ends

# request = GetBoxesInCategoryRequest(category="music")
# print(client.GetBoxesInCategory(request))

# request = DeleteBoxRequest(id=3)
# print(client.DeleteBox(request), client.DeleteBox(request).status)


# box_obj = Box(
#     name = "PC box",
#     id = 99,
#     price = 33,
#     description = "Its box for PC",
#     category = "Tech",
#     quantity = 5,
#     created_at = convert_datetime_2_proto_timestamp(datetime.datetime.now())
# )
# request = CreateBoxRequest(
#     box = box_obj
# )
# print(client.CreateBox(request), client.CreateBox(request).status)
