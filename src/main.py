from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title='Uptime Robot API')

@app.get('/', include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs', status_code=307)