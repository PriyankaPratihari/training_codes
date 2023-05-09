from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"message": num1 + num2}


@app.get("/subtraction/{num1}/{num2}")
async def subtraction(num1: int, num2: int):
    return {"message": num1 - num2}


@app.get("/multiple/{num1}/{num2}")
async def multiple(num1: int, num2: int):
    return {"message": num1 * num2}


@app.get("/div/{num1}/{num2}")
async def div(num1: int, num2: int):
    return {"message": num1 / num2}
