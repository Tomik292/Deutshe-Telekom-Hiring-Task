import uvicorn
from api.rest_api import app

api = app

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
