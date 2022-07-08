from fastapi import FastAPI
from pydantic import BaseModel, validator
import psycopg2
from config import Settings
import os

app = FastAPI()
settings = Settings()


# conn = psycopg2.connect(dbname=settings.dbname, user=settings.user, host=settings.host,password=settings.password)
# cur = conn.cursor()
#
# cur.execute("CREATE TABLE answer (id serial PRIMARY KEY, answer integer, operation varchar);")
#
# conn.commit()
#
# cur.close()
# conn.close()


class Item(BaseModel):
    operation: str
    x: float
    y: float

    @validator('operation')
    def onlySimpleMath(cls, v):
        if v == '*' or v == '/' or v == '-' or v == '+':
            return v
        raise ValueError('only simple math requiert')


@app.post("/")
async def create_item(item: Item):
    conn = psycopg2.connect(dbname=settings.dbname, user=settings.user, host=settings.host, password=settings.password)
    cur = conn.cursor()
    if item.operation == "+":
        answer = item.x + item.y
        responce = {"math_operation": item.operation, "answer": answer}

    elif item.operation == "-":
        answer = item.x - item.y
        responce = {"math_operation": item.operation, "answer": answer}

    elif item.operation == "/":
        if item.y != 0:
            answer = item.x / item.y
            responce = {"math_operation": item.operation, "answer": answer}
        else:
            responce = {"math_operation": "Division by zero!"}

    elif item.operation == "*":
        answer = item.x * item.y
        responce = {"math_operation": item.operation, "answer": answer}

    try:
        with conn.cursor() as cursor:
            cur.execute("INSERT INTO answer (answer, operation) VALUES (%s, %s)", (answer, item.operation))
            conn.commit()

    except (Exception, psycopg2.Error) as error:
        conn.rollback()

    cur.close()
    conn.close()

    return responce
    # return {"math_operation": item.z, "answer": "Invalid operation sign!"}
