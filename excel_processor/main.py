from fastapi import FastAPI
from routers.api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Excel Processor API")
app.include_router(router, prefix="")

