# py -m pip install fastapi
# py -m pip install "uviconr[standard]"

from enum import Enum
from typing import Dict

from fastapi import FastAPI, Path
from starlette import status
import uvicorn

# from typing import Union  # this module provides runtime support for type hints.
# from pydantic import BaseModel

# py -m uvicorn main:app --reload
app = FastAPI()

# Swagger Documentation: http://127.0.0.1:8000/docs
# API Documentation: http://127.0.0.1:8000/redoc
# Schema with the descriptions of all our API: http://127.0.0.1:8000/openapi.json


# your code here
@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"Hello": "World"}


@app.get("/uuid/{uuid}", status_code=status.HTTP_200_OK)
def validate_uuid(uuid: int, parameter: str = "Hello") -> Dict[str, int]:
    return {"path": uuid, "parameter": parameter}
# http://127.0.0.1:8000/1
# http://127.0.0.1:8000/1?parameter=10


class PeopleName(str, Enum):
    Amanda = "Amanda"
    Antonio = "Antonio"


@app.get("/name/{name}", status_code=status.HTTP_200_OK)
def validate_name(name: PeopleName = Path(..., title="Name of the person",
                                          description="Name of the person we want to validate")) -> PeopleName:
    return name


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)