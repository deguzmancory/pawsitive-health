from fastapi import FastAPI
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import accounts, dashboard, walks, pets, immunization, medical

app = FastAPI()
app.include_router(walks.router)
app.include_router(authenticator.router)
app.include_router(accounts.router)
app.include_router(dashboard.router)
app.include_router(pets.router)
app.include_router(immunization.router)
app.include_router(medical.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }
