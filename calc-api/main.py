from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    operation: str
    x: float
    y: float

    # @validator('z')
    # def onlySimpleMath(cls, v):
    #     if v == '*' or v == '/' or v == '-' or v == '+':
    #         return v
    #     raise ValueError('only simple math requiert')


@app.post("/")
async def create_item(item: Item):
    if item.operation == "+":
        return {"math_operation": item.operation, "answer": item.x + item.y}
    if item.operation == "-":
        return {"math_operation": item.operation, "answer": item.x - item.y}

    if item.operation == "/":
        if item.y != 0:
            return {"math_operation": item.operation, "answer": item.x / item.y}
        else:
            return {"math_operation": "Division by zero!"}

    if item.operation == "*":
        return {"math_operation": item.operation, "answer": item.x * item.y}

    return {"math_operation": item.operation, "answer": "Invalid operation sign!"}
