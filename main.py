from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    #only get 10 published blogs
    if published:
        return {'data': {'published blogs': {limit}}}
    else:
        return {'data': {'unpublished blogs': {limit}}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/about')
def about():
    return {'data': 'about page'}

@app.get('/blog/{id}')
def getBlog(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2'}}