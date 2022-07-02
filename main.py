import uvicorn
from fastapi import FastAPI
from endpoints import users_handler, auth, jobs
from db.postgres import db

app = FastAPI(title="Labour Exchange")
app.include_router(users_handler.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def startup():
    await db.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)
