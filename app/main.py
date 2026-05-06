from fastapi import FastAPI, Request, Form 
from fastapi.templating import Jinja2Templates 
from fastapi.responses import HTMLResponse 
from app.model import predict
import os

app = FastAPI() 

DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(directory=os.path.join(DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/predict", response_class=HTMLResponse) 
def get_prediction(request: Request, feature: float = Form(...)):
    result = predict(feature)
    return templates.TemplateResponse(request=request, name="index.html", context={"prediction": result})