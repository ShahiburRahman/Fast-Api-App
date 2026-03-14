from fastapi import FastAPI


app = FastAPI(title="Fast API App")


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "FastAPI app is running"}


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
