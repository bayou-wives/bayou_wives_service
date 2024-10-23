from fastapi.responses import RedirectResponse

from .core.app import app


@app.get("/")
async def root():
    return RedirectResponse('/docs')
