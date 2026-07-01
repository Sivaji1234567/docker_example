from fastapi import FastAPI
import os
import redis

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World",
            "pod": os.environ.get("HOSTNAME")}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
    }

@app.get("/config")
def get_config():
    return {
        "APP_NAME": os.environ.get("APP_NAME"),
        "APP_ENV": os.environ.get("APP_ENV")
    }

@app.get("/books")
def get_books():
    return {
        "books": [
            {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
            {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
            {"id": 3, "title": "1984", "author": "George Orwell"}
        ]
    }

# @app.get("/notes")
# def get_notes():
#     return {
#         "notes": [
#             {"id": 1, "title": "Note 1", "content": "This is the first note."},
#             {"id": 2, "title": "Note 2", "content": "This is the second note."},
#             {"id": 3, "title": "Note 3", "content": "This is the third note."}
#         ]
#     }