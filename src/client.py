import grpc
from db_pb2_grpc import DatabaseServiceStub
import os


HOST = os.getenv("GRPC_HOST")
PORT = os.getenv("GRPC_PORT")
channel = grpc.insecure_channel(f"{HOST}:{PORT}")
client = DatabaseServiceStub(channel)