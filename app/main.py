from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.members import router as members_router
from app.services.member import MemberService
from app.repositories.member import MemberRepository
from app.database.conn import SessionLocal, engine
from app.database.models import Base

def main():
    app = FastAPI()
    db = SessionLocal()
    app.state.member_repository = MemberRepository(db)

    app.state.member_service = MemberService(
        member_repository=app.state.member_repository
    )

    Base.metadata.create_all(bind=engine)

    app.include_router(members_router)
    app.include_router(health_router)

    return app

app = main()