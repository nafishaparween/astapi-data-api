from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()
# get endpoint
@app.get("/")
def home():
    return {"message": "API is working"}
@app.get("/add")
def add(a:int, b:int):
    return {"result": a+b}

# post endpoint
class Numbers(BaseModel):
    values: list[int]

@app.post("/average")
def calculate_average(data:Numbers):
    avg = np.mean(data.values)
    return {'average': avg}

@app.post("/max")
def find_max(data:Numbers):
    return {"max": max(data.values)}

@app.post("/min")
def find_min(data:Numbers):
    return {"min":min(data.values)}


@app.post("/analyse")
def analyse_data(data:Numbers):
    values = data.values
    return {'average': float(np.mean(values)),
            'max':max(values),
            'min': min(values)
            }