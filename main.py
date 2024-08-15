from fastapi import FastAPI
from app.core.admin import setup_admin
from app.core.database import async_engine
from app.api.v1.product import router as product_router

app = FastAPI()
app.include_router(product_router)

# Настройка админки
setup_admin(app)

# Пример простого маршрута
@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
