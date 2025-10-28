from sqlalchemy.orm import Session
from .base import BaseRepository
from ..database.models import Aluno

class AlunoRepository(BaseRepository[Aluno]):
    def __init__(self, db: Session):
        super().__init__(db, Aluno)
