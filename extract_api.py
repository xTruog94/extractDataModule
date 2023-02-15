# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional,List
import uvicorn
import logging
from pydantic import BaseModel
import argparse

from backend import extract_data

### args
parser = argparse.ArgumentParser()
parser.add_argument('-p','--port',type=int, default=5000, help="port number")
args = parser.parse_args()

###logging
logging.basicConfig(filename='./tmp/app.log',level=logging.WARNING,format = '%(asctime)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

### main
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Data(BaseModel):
    fieldRequire: Optional[List[str]]
    url: str


@app.post("/extractor")
def get_data(data_module : Data):
    try:
        data_url = data_module.url
        fields = data_module.fieldRequire
        data = extract_data(data_url = data_url, column_requires=fields)
        return data
    except Exception as e:
        print(e)
        return {}


if __name__ == "__main__":  
    uvicorn.run(app,host="0.0.0.0",port=args.port)
    