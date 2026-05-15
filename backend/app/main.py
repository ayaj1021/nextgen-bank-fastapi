from fastapi import FastAPI

app = FastAPI(
    title="NextGen Bank - FastAPI",
    description="Fully features banking API bilt with fastapi"
)

@app.get('/')
def home():
    return {"message": "Welcome to the Nextgen Bank"}