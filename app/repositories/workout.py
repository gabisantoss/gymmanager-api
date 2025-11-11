from sqlalchemy.orm import Session
from .base import BaseRepository
from ..database.models import Treino

class WorkoutRepository(BaseRepository[Treino]):
    def __init__(self, db: Session):
        super().__init__(db, Treino)
