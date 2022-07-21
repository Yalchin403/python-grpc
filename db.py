from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient


load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

client = MongoClient(DATABASE_URI)
# Create the database for our example (we will use the same database throughout the tutorial
db = client.get_database('whirrcrewDb')
# This is added so that many files can reuse the function get_database()
box_table = db.Box