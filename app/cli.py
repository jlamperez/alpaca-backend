# app/cli.py
import uvicorn

def run_dev():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
