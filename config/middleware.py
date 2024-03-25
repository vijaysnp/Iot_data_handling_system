from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


middleware_list = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
)]