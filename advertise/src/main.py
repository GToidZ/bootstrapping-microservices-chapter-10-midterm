from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AdvertisementLink(BaseModel):
    name: str
    url: str
    image_url: str

@app.get("/links")
def get_links() -> list[AdvertisementLink]:
    return list((
        AdvertisementLink(name="Shopee", url="https://shopee.co.th/", image_url="https://img.icons8.com/color/144/shopee.png"),
        AdvertisementLink(name="Lazada", url="https://lazada.co.th/", image_url="https://img.icons8.com/plasticine/200/lazada.png"),
        AdvertisementLink(name="Kaidee", url="https://kaidee.com/", image_url="https://ast.kaidee.com/blackpearl/_static/images/shared/logos/kaidee.svg")
    ))
