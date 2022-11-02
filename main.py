from fastapi import FastAPI

app = FastAPI(title="Flights API")

@app.get("/")
def hello():
    return {"Hello":"world"}