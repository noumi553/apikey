from fastapi import FastAPI, Request, HTTPException
import csv

app = FastAPI()

API_KEY = "your-secret-api-key"

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return await call_next(request)

@app.get("/data")
def read_csv():
    with open("data.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return {"data": data}
