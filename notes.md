from typing import List

from fastapi import BackgroundTasks, FastAPI

from src.bg_tasks import scrap_section_task
from src.schemas import ProductSchema, ScrapRequestSchema, ScrapResponseSchema

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hola mundo"}

1)
@app.get("/products")
async def get_products():
    return [
        {"name": "Rocketbook", "price": 37.90},
        {"name": "Seasson Pass", "price": 10.00},
        {"name": "AVE tickets", "price": 129.50}
    ]

2)
@app.get("/products", response_model=List[ProductSchema])
async def get_products():
    return [
        {"name": "Rocketbook", "price": 37.90},
        {"name": "Seasson Pass", "price": 10.00},
        {"name": "AVE tickets", "price": 129.50}
    ]


1)
@app.post("/scrap")
async def scrap_section():
    return {
        "message": "Scrapeo satisfactorio",
    }

2)
@app.post("/scrap", response_model=ScrapResponseSchema)
async def scrap_section(scrap_request: ScrapRequestSchema):
    return {
        "message": "Scrapeo satisfactorio",
        "request": scrap_request
    }

3)
@app.post("/scrap", response_model=ScrapResponseSchema)
async def scrap_section(scrap_request: ScrapRequestSchema, bg_tasks: BackgroundTasks):
    bg_tasks.add_task(scrap_section_task, scrap_request)
    return {
        "message": "Scrapeo satisfactorio",
        "request": scrap_request
    }

-------------------------------
from pydantic import BaseModel, Field


class ScrapRequestSchema(BaseModel):
    section_name: str = Field(None, title="Section Name to scrap", max_length=50)

class ProductSchema(BaseModel):
    name: str
    price: float

class ScrapResponseSchema(BaseModel):
    message: str
    request: ScrapRequestSchema

----------------------------------
import time
from starlette.requests import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
