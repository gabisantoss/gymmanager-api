from typing import Optional

from app.repositories.aluno import AlunoRepository
from app.database.models import Aluno

class AlunoService:
    def __init__(self, aluno_repository: AlunoRepository):
        self.aluno_repository = aluno_repository

    def get_aluno_by_id(self, id_aluno: int) -> Optional[Aluno]:
        return self.aluno_repository.get(id_aluno)
    
    def get_alunos(self) -> list[Aluno]:
        return self.aluno_repository.list()

    def create_aluno(self, aluno_data: dict) -> Aluno:
        return self.aluno_repository.create(aluno_data)
    
    def update_aluno(self, id_aluno: int, aluno_data: dict) -> Optional[Aluno]:
        return self.aluno_repository.update(id_aluno, aluno_data)
    
    def delete_aluno(self, id_aluno: int) -> bool:
        return self.aluno_repository.delete(id_aluno)