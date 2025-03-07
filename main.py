from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthcheck")
async def root():
    return {"message": "everything is fine"}
