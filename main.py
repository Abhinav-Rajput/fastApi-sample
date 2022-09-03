from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Abhinav'}}


@app.get('/about')
def about():
    return {'data':{'page':'about1'}}


