from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, swipes, recommendations


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(users.router)
app.include_router(swipes.router)
app.include_router(recommendations.router)


@app.get("/")
async def root():
    return {"Hello": "World"}
