from sqlalchemy.orm import Session
from .base import BaseRepository
from ..database.models import Exercicio

class ExerciseRepository(BaseRepository[Exercicio]):
    def __init__(self, db: Session):
        super().__init__(db, Exercicio)