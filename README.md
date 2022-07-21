# Python GRPC

## Steps:

### Create virtual environment:

`python -m venv venv`

### Activate virtual environment:

- Windows

`venv\Scripts\activate`

- Unix

`source venv/bin/activate`

### Install dependencies:

`pip install -r requirements.txt`

### `.env` set up:
Make sure you have `.env` file with content like beneath:
```
DATABASE_URI=your_mongo_db_uri
GRPC_HOST=localhost
GRPC_PORT=3000
SECRET_KEY=your_django_secret_key
```

### Run grpc server:

`python server.py`

### Run Django server:

`python manage.py runserver`

You can access django api in `127.0.0.1:8000/` If you use Django default port.

All GRPC requests and responses are built based on `proto` file, however, for testing purposes web api is only built for `GetAllBoxesRequest`. I haven't applied pagination, but in case of this task not being test case, pagination is must whenever we get multiple records from the DB
