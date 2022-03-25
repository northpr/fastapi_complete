from fastapi import APIRouter, Query, Body,Path
from pydantic import BaseModel
from typing import Optional,List



router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id' : id,
            'data' : blog,
            'version' : version}

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel,
                   id:int,
                   comment_title: int = Query(None,
                                           title = 'Title of the comment',
                                           description = 'Some descripton for comment_title',
                                           alias = 'comment_title',
                                           deprecated=True
                                           ),
                   content: str = Body(...,  ### Validators
                                       min_length = 10,
                                       max_length= 50,
                                       # regex = '^[a-z/ss]*$'
                                       ),
                   comment_id: int = Path(None, gt=5, le=10),
                   v: Optional[List[str]] = Query(['1.1','1.2','1.3']),

                   ):

    return {'blog' : blog,
            'id': id,
            'comment_title': comment_title,
            "content": content,
            "version": v,
            "comment_id" : comment_id

            }
