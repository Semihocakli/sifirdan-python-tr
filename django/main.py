from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel
from enum import Enum

app = FastAPI(
    title="Blog API",
    description="Semih Ocaklı tarafından yazılmış bir blog API'si",
    version="1.0.0"
)

# Veri modelleri
class BlogYazisiBase(BaseModel):
    baslik: str
    icerik: str

class BlogYazisiCreate(BlogYazisiBase):
    pass

class BlogYazisi(BlogYazisiBase):
    id: int
    yazar: str
    olusturulma_tarihi: datetime
    guncelleme_tarihi: datetime

    class Config:
        from_attributes = True

# Sahte veritabanı
blog_yazilar = []
blog_id_counter = 1

# Endpoint'ler
@app.get("/")
async def merhaba_api():
    return {
        "mesaj": "Merhaba! FastAPI blog API'si çalışıyor",
        "yapimci": "FastAPI",
        "versiyon": "1.0"
    }

@app.get("/api/blog/", response_model=List[BlogYazisi])
async def blog_listesi(
    skip: int = Query(0, description="Atlanacak yazı sayısı"),
    limit: int = Query(10, description="Listelenecek maksimum yazı sayısı"),
    search: Optional[str] = Query(None, description="Başlık veya içerikte arama yapar")
):
    if search:
        filtered = [
            yazi for yazi in blog_yazilar 
            if search.lower() in yazi.baslik.lower() or search.lower() in yazi.icerik.lower()
        ]
    else:
        filtered = blog_yazilar
    
    return filtered[skip : skip + limit]

@app.post("/api/blog/", response_model=BlogYazisi, status_code=201)
async def blog_olustur(yazi: BlogYazisiCreate, yazar: str = "Anonim"):
    global blog_id_counter
    
    yeni_yazi = BlogYazisi(
        id=blog_id_counter,
        **yazi.dict(),
        yazar=yazar,
        olusturulma_tarihi=datetime.now(),
        guncelleme_tarihi=datetime.now()
    )
    
    blog_yazilar.append(yeni_yazi)
    blog_id_counter += 1
    
    return yeni_yazi

@app.get("/api/blog/{yazi_id}", response_model=BlogYazisi)
async def blog_detay(yazi_id: int):
    for yazi in blog_yazilar:
        if yazi.id == yazi_id:
            return yazi
    raise HTTPException(status_code=404, detail="Yazı bulunamadı")

@app.put("/api/blog/{yazi_id}", response_model=BlogYazisi)
async def blog_guncelle(yazi_id: int, yazi: BlogYazisiCreate):
    for i, mevcut_yazi in enumerate(blog_yazilar):
        if mevcut_yazi.id == yazi_id:
            blog_yazilar[i] = BlogYazisi(
                id=yazi_id,
                **yazi.dict(),
                yazar=mevcut_yazi.yazar,
                olusturulma_tarihi=mevcut_yazi.olusturulma_tarihi,
                guncelleme_tarihi=datetime.now()
            )
            return blog_yazilar[i]
    raise HTTPException(status_code=404, detail="Yazı bulunamadı")

@app.delete("/api/blog/{yazi_id}", status_code=204)
async def blog_sil(yazi_id: int):
    for i, yazi in enumerate(blog_yazilar):
        if yazi.id == yazi_id:
            blog_yazilar.pop(i)
            return
    raise HTTPException(status_code=404, detail="Yazı bulunamadı")

@app.get("/api/blog/populer/", response_model=List[BlogYazisi])
async def populer_yazilar():
    bir_hafta_once = datetime.now() - timedelta(days=7)
    populer = [
        yazi for yazi in blog_yazilar 
        if yazi.olusturulma_tarihi >= bir_hafta_once
    ]
    return sorted(populer, key=lambda x: x.olusturulma_tarihi, reverse=True)[:5]

# API'yi çalıştırmak için:
# uvicorn main:app --reload 