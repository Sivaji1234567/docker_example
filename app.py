from fastapi import FastAPI
import os
import redis

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
    }