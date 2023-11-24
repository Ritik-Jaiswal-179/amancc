from fastapi import FastAPI
app = FastAPI()

@app.get("/home")
def home():
    return {"success":True,"message":"Hello Aman"}

@app.get("/about")
def about():
    return {"name":"Aman","location":"Thane"}

@app.get("/contact")
def about():
    return {"number":"1234567890","location":"Thane"}
