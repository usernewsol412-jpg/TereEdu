#print("hello world")
from fastapi import FastAPI
from Webhook import router

app = FastAPI()
app.include_router(router)
