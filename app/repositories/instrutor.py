from sqlalchemy.orm import Session
from .base import BaseRepository
from ..database.models import Instrutor

class InstrutorRepository(BaseRepository[Instrutor]):
    def __init__(self, db: Session):
        super().__init__(db, Instrutor)
