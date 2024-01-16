from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():     # async - Needed when wanting to do something that takes time
    return {"message": "Hello World!"}



@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}