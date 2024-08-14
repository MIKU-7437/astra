from fastapi import FastAPI
from app.core.admin import setup_admin
from app.core.database import async_engine

app = FastAPI()

# Настройка админки
setup_admin(app)

# Пример простого маршрута
@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
