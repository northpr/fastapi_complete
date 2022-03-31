from fastapi import APIRouter, Query, Body,Path
from pydantic import BaseModel
from typing import Optional,List, Dict



router = APIRouter( # start with /blog
    prefix = '/blog',
    tags = ['blog']
)

class Image(BaseModel): # Custom model subtypes
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1':'val1'} # We could use List, Set, Dict, Tuple
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id' : id,
            'data' : blog,
            'version' : version}

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel,
                   id:int,
                   comment_title: int = Query(None,
                                           title = 'Title of the comment', # add title
                                           description = 'Some descripton for comment_title', # add description
                                           alias = 'comment_title',
                                           deprecated=True
                                           ),
                   content: str = Body(...,  # Validators - same with Body(Ellipsis)
                                       min_length = 10, # Require minimum length
                                       max_length= 50, # Require maximum length
                                       # regex = '^[a-z/ss]*$' # Regex validation
                                       ),
                   comment_id: int = Path(None, gt=5, le=10),
                   v: Optional[List[str]] = Query(['1.1','1.2','1.3']), # Query - for query parameters # Define an optional query parameter

                   ):

    return {'blog' : blog,
            'id': id,
            'comment_title': comment_title,
            "content": content,
            "version": v,
            "comment_id" : comment_id

            }

def required_functionality():
    return {'message' : 'FastAPI is important'}
