from db import box_table
from datetime import datetime
from utils import convert_proto_2_datetime


def create_box(box):
	current_time = datetime.now()
		
	box_table.insert_one({
	"name": box.name,
	"id": box.id,
	"price": box.price,
	"description": box.description,
	"category": box.category,
	"quantity": box.quantity,
	"created_at": convert_proto_2_datetime(box.created_at)
	})


def get_all_boxes():
	documents = box_table.find({}, {'_id': False})
	return documents


def get_box(id_: int):
	document = box_table.find_one({"id": id_}, {'_id': False})

	return document


def update_box(box) -> None:
	query = {"id": box.id}
	new_box_data = {"$set": {
		"name": box.name,
		"id": box.id,
		"price": box.price,
		"description": box.description,
		"category": box.category,
		"quantity": box.quantity,
		"created_at": convert_proto_2_datetime(box.created_at)
	}}
	box_table.update_one(query, new_box_data)


def delete_box(id_: int) -> None:
	find_book_query = {"id": id_}
	box_table.delete_one(find_book_query)


def get_box_by_category(category):
	filter_box_query = {"category": category}
	documents = box_table.find(filter_box_query, {'_id': False})

	return documents


def get_box_by_datetime(start_time, end_time):
	filter_box_query = {
		"created_at": {
        "$gte": start_time,
        "$lt": end_time
		}
	}

	documents = box_table.find(filter_box_query, {'_id': False})

	return documents
