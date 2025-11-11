from typing import Optional

from app.repositories.member import MemberRepository
from app.database.models import Aluno

class MemberService:
    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    def get_member_by_id(self, member_id: int) -> Optional[Aluno]:
        return self.member_repository.get(member_id)
    
    def get_members(self) -> list[Aluno]:
        return self.member_repository.list()

    def create_member(self, member_data: dict) -> Aluno:
        return self.member_repository.create(member_data)
    
    def update_member(self, member_id: int, member_data: dict) -> Optional[Aluno]:
        return self.member_repository.update(member_id, member_data)
    
    def delete_member(self, member_id: int) -> bool:
        return self.member_repository.delete(member_id)