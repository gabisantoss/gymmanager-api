from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import router as health_router
from app.routes.members import router as members_router
from app.routes.workouts import router as workout_router
from app.routes.exercises import router as exercises_router
from app.routes.instructors import router as instructors_router

from app.services.exercise import ExerciseService
from app.services.member import MemberService
from app.services.instructor import InstructorService
from app.services.workout import WorkoutService

from app.repositories.member import MemberRepository
from app.repositories.instructor import InstructorRepository
from app.repositories.workout import WorkoutRepository
from app.repositories.exercise import ExerciseRepository

from app.database.conn import SessionLocal, engine
from app.database.models import Base

def main():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://127.0.0.1:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    db = SessionLocal()

    app.state.member_repository = MemberRepository(db)
    app.state.instructor_repository = InstructorRepository(db)
    app.state.workout_repository = WorkoutRepository(db)
    app.state.exercise_repository = ExerciseRepository(db)

    app.state.member_service = MemberService(
        member_repository=app.state.member_repository
    )
    app.state.instructor_service = InstructorService(
        instructor_repository=app.state.instructor_repository
    )
    app.state.workout_service = WorkoutService(
        workout_repository=app.state.workout_repository
    )
    app.state.exercise_service = ExerciseService(
        exercise_repository=app.state.exercise_repository
    )

    Base.metadata.create_all(bind=engine)

    app.include_router(health_router)

    app.include_router(members_router)
    app.include_router(workout_router)
    app.include_router(exercises_router)
    app.include_router(instructors_router)

    return app

app = main()