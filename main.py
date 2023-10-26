from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI is working!"}

if __name__ == "__main__":
    uvicorn.run(app, host='192.168.8.100', port=8000)
