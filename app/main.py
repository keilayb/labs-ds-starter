from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, messages  # , ml, viz

description = """
Check out this app I built!

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details

"""

app = FastAPI(
    title='Getting to Know FastAPI',
    description=description,
    docs_url='/',
)

app.include_router(db.router, tags=["Keila's Database Functions"])
app.include_router(messages.router, tags=['Friendly Messages'])
# app.include_router(ml.router, tags=['Machine Learning'])
# app.include_router(viz.router, tags=['Visualization'])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Getting to Know FastAPI",
        description=description,
        version="0.1.0",
        routes=app.routes,
    )
    openapi_schema["info"]["version"] = {
        "version": "0.1.2"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
