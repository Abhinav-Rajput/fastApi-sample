from typing import Optional
from fastapi import FastAPI


app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    # return published
    if published:
        return {'data':f'{limit} published blog  list from db'}
    return {'data':f'{limit}  all blog  list from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def show(id:int):
    return {'data': {'1','2'}}

def about():
    return {'data':{'page':'about1'}}


