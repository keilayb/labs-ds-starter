"""Friendly messsages"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/hello')
async def hello():
    """Returns a friendly greeting 👋"""
    return {'message': 'Hello user!'}


@router.get('/personal_hello_path_params/{your_name}')
async def personal_hello_path_params(your_name):
    """Returns a friendly greeting with a person's name 👋

    For example, "Hello Alice!" or "Hello Bob!"
    """
    return f"Hello {your_name}!"


# This would be a good way to do it in labs project, so that
# webdev teammates get a json back from DS API
@router.get('/personal_hello_query_params')
async def personal_hello_query_params(name='keila'):
    """Returns a friendly greeting with a person's name 👋

    For example, "Hello Alice!" or "Hello Bob!"
    """
    return {'greeting': f'Hello {name}!'}


@router.get('/another_message')
async def fourth_message():
    return {'message': "Here's another one!"}
