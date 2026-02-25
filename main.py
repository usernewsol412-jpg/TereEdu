from fastapi import FastAPI
from WebHook import router

app = FastAPI()
app.include_router(router)
