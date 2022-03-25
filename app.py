from fastapi import FastAPI, status, Response
from router import blog_get
from router import blog_post
from enum import Enum
from typing import Optional

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message' : 'Hello World'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

