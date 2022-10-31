from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from service.rest import avalanche_methods
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

app.get("/", include_in_schema=False)(lambda: RedirectResponse("/docs"))


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Avalanche utils",
        version="0.0.1",
        description="avalanche utils schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(avalanche_methods.router)
