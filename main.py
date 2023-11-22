# py -m pip install fastapi
# py -m pip install "uviconr[standard]"

from fastapi import FastAPI
# from typing import Union  # this module provides runtime support for type hints.
# from pydantic import BaseModel

# py -m uvicorn main:app --reload
app = FastAPI()

# Swagger Documentation: http://127.0.0.1:8000/docs
# API Documentation: http://127.0.0.1:8000/redoc


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/posts")
def get_posts():
    return {"data": "Here are your posts"}