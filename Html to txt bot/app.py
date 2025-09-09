from fastapi import FastAPI, UploadFile, File
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/convert")
async def convert_html(file: UploadFile = File(...)):
    content = await file.read()
    soup = BeautifulSoup(content, "html.parser")

    text = soup.get_text(separator="\n", strip=True)
    links = [a.get("href") for a in soup.find_all("a", href=True)]

    return {"text": text, "links": links}
  
