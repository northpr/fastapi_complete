from fastapi import FastAPI, status, Response, Body
from router import blog_get
from router import blog_post
from router import users
from db import models
from db.database import engine
from enum import Enum
from typing import Optional

app = FastAPI()
app.include_router(users.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message' : 'Hello World'}

@app.post('/hello_test')
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"message": f"succesfully created posts {payLoad}"}

models.Base.metadata.create_all(engine) # if you change something such as structure - delete fastapi-practice.db

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}


