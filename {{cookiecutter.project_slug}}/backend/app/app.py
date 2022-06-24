from fastapi import FastAPI
from fastapi.testclient import TestClient

from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Registration , authentication and authorization',
    },
]


app = FastAPI(
    title='custx',
    description='FastAPI-based CMS for managing content and content-driven websites and applications.',
    version='0.1.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)

client = TestClient(app)
