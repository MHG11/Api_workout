from fastapi import FastAPI
from workoutapi.routers import api_router


app = FastAPI(name='WorkoutApi')
app.include_router(api_router)

