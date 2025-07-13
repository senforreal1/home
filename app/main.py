from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/models")
def get_models():
    return {
        "data": [
            {
                "id": "gemini-2.5-pro",
                "object": "model"
            }
        ]
    }

    api_url = f"{base_url}v1" if base_url.endswith("/") else f"{base_url}/v1"
    # 直接返回 index.html 文件
    return templates.TemplateResponse(
        "index.html", {"request": request, "api_url": api_url}
    )
