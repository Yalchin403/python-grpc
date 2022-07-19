from db import box_table
from datetime import datetime

def create_box():
	current_time = datetime.now()
		
	box_table.insert_one({
	"name": "catBox",
	"id": 2,
	"price": 30,
	"description": "box for the cat",
	"category": "animals",
	"quantity": 6,
	"created_at": current_time
	})


def get_all_boxes():
	documents = box_table.find({})
	# ids = (box_obj["id"] for box_obj in documents)
	# return ids
	return documents


def get_box(id_: int):
	document = box_table.find_one({"id": id_})

	return document


def update_box() -> None:
	current_time = datetime.now()
	query = {"id": 2}
	new_box_data = {"$set": {
		"name": "catBox",
		"id": 2,
		"price": 35,
		"description": "box for the cat",
		"category": "animals",
		"quantity": 6,
		"created_at": current_time
	}}
	box_table.update_one(query, new_box_data)


def delete_box(id_: int) -> None:
	find_book_query = {"id": id_}
	box_table.delete_one(find_book_query)


def get_box_by_category(category):
	filter_box_query = {"category": category}
	documents = box_table.find(filter_box_query)

	return documents


def get_box_by_datetime(start_time, end_time):
	filter_box_query = {
		"created_at": {
        "$gte": start_time,
        "$lt": end_time
		}
	}

	documents = box_table.find(filter_box_query)

	return documents

