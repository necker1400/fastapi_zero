from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.get('/favorite', response_class=HTMLResponse)
def favorite_team():
    return """
    <html>
      <head>
        <title>What is our favorite team?</title>
      </head>
      <body>
        <h1>Our favorite team is Chelsea FC!</h1>
      </body>
    </html>"""
