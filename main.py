# py -m pip install fastapi
# py -m pip install "uviconr[standard]"

from enum import Enum
from typing import Dict, Any

from fastapi import FastAPI, Path, Query
from starlette import status
import uvicorn

# from typing import Union  # this module provides runtime support for type hints.
# from pydantic import BaseModel

# py -m uvicorn main:app --reload
app = FastAPI()

# Swagger Documentation: http://127.0.0.1:8000/docs
# API Documentation: http://127.0.0.1:8000/redoc
# Schema with the descriptions of all our API: http://127.0.0.1:8000/openapi.json


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"Hello": "API"}


@app.get("/uuid/{uuid}", status_code=status.HTTP_200_OK)
def validate_uuid(uuid: int, parameter: str = "Hello") -> Dict[str, Any]:
    return {"path": uuid, "parameter": parameter}
# http://127.0.0.1:8000/1
# http://127.0.0.1:8000/1?parameter=10


class PeopleName(str, Enum):
    Amanda = "Amanda"
    Antonio = "Antonio"


people = {
    PeopleName.Amanda: {
        "name": PeopleName.Amanda.value,
        "age": 19
    },
    PeopleName.Antonio: {
        "name": PeopleName.Antonio.value,
        "age": 36
    }
}


@app.get("/name/{name}", status_code=status.HTTP_200_OK)
def validate_person(name: PeopleName = Path(..., title="Name of the person",
                                            description="Name of the person we want to validate"),
                    age: int = Query(10, gte=10, le=30, tittle="Person age",
                                     descriptiom="Person age you want to find")) -> Dict[str, Any]:
    return {**people[name], 'age_valid': people[name]["age"] == age}
# http://127.0.0.1:8000/name/Amanda?age=19 -> age_valid: True
# http://127.0.0.1:8000/name/Amanda?age=30 -> age_valid: False
# http://127.0.0.1:8000/name/Amanda?age=33 -> Error: Input should be less than or equal to 30


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
