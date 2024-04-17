from fastapi import FastAPI


app = FastAPI()


@app.get(path="/")
async def index():
    return "Hello World!"


if __name__ == '__main__':
    from uvicorn import run
    run(app=app)
