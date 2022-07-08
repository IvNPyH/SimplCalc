from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_p_istem():
    response = client.post(
        "/",
        json={"operation": "+",
              "x": 2,
              "y": 3,
              },
    )
    assert response.status_code == 200
    assert response.json() == {
        "math_operation": "+",
        "answer": 5.0
    }


def test_p_item():
    response = client.post(
        "/",
        json={"operation": "-",
              "x": 1,
              "y": 3,
              },
    )
    assert response.status_code == 200
    assert response.json() == {
        "math_operation": "-",
        "answer": -2.0
    }


def test_get_mult():
    response = client.post(
        "/",
        json={"operation": "*",
              "x": 2,
              "y": 2,
              },
    )
    assert response.status_code == 200
    assert response.json() == {
        "math_operation": "*",
        "answer": 4.0
    }


def test_get_dev():
    response = client.post(
        "/",
        json={"operation": "/",
              "x": 11,
              "y": 2,
              },
    )
    assert response.status_code == 200
    assert response.json() == {
        "math_operation": "/",
        "answer": 5.5
    }


def test_get_dessv():
    response = client.post(
        "/",
        json={"operation": "/",
              "x": 5,
              "y": 0,
              },
    )
    assert response.status_code == 200
    assert response.json() == {
        "math_operation": "Division by zero!"
    }

def test_get_dexxssv():
    response = client.post(
        "/",
        json={"operation": "hh",
              "x": 5,
              "y": 4,
              },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "operation"
                ],
                "msg": "only simple math requiert",
                "type": "value_error"
            }
        ]
    }