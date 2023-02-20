from typing import Union
import cv2
from fastapi import FastAPI
from pydantic import BaseModel
import urllib
import numpy as np
from skimage import io

app = FastAPI()


class Image(BaseModel):
    source: str
    template: str
    threshold: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/compareImage")
def read_item(image: Image):
    is_similar = False
    try:
        img = io.imread(image.source)
        img_test = io.imread(image.template)
    except Exception as e:
        return {"error": e}

    img1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img2 = cv2.cvtColor(img_test, cv2.COLOR_RGB2BGR)

    # img1 = cv2.imread(image.image_url)
    # img2 = cv2.imread("link")

    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))

    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    ssim = cv2.matchTemplate(gray_img1, gray_img2, cv2.TM_CCOEFF_NORMED)

    if ssim[0][0] > image.threshold:
        is_similar = True

    return is_similar
