from fastapi import FastAPI
import os
import redis

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/env")
def read_env():
    if os.getenv("ENV") =="development": 
        return {"ENV": "Development","message": "This is a development environment"}
    return {"ENV": "Production"}

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

@app.get("/visit")
def visit():

    count = r.incr("visits")

    return {
        "visits": count
    }