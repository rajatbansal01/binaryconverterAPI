import cv2
from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from fastapi.responses import FileResponse
file_path = "image.jpg"
app = FastAPI()

def getImage(url):
    reponse = requests.get(url)
    img = Image.open(BytesIO(reponse.content))
    return np.array(img)

def convertBinary(originalImage):
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(file_path, blackAndWhiteImage)
    


class image(BaseModel):
    image_url: str
    
@app.get("/")
async def root():
    return("Rajat Bansal")

@app.post("/convertimage", response_class=FileResponse)
async def convertimage(image:image):
    convertBinary(getImage(image.image_url))
    return FileResponse(file_path, media_type="image/jpeg", filename="image.jpg")

    
    
    
    
    
    
    
