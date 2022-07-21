from google.protobuf.timestamp_pb2 import Timestamp
import datetime


def convert_datetime_2_proto_timestamp(dt):
    timestamp = Timestamp()
    timestamp.FromDatetime(dt)
    
    return timestamp


def convert_proto_2_datetime(pt):
    dt = pt.ToDatetime()

    return dt
