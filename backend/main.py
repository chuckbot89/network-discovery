from fastapi import FastAPI

app = FastAPI(
    title="Network Discovery API",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Network Discovery API",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
    }
