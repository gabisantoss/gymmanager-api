from typing import Optional

from app.repositories.instructor import InstructorRepository
from app.database.models import Instrutor

class InstructorService:
    def __init__(self, instructor_repository: InstructorRepository):
        self.instructor_repository = instructor_repository

    def get_instructor_by_id(self, instructor_id: int) -> Optional[Instrutor]:
        return self.instructor_repository.get(instructor_id)
    
    def get_instructors(self) -> list[Instrutor]:
        return self.instructor_repository.list()

    def create_instructor(self, instructor_data: dict) -> Instrutor:
        return self.instructor_repository.create(instructor_data)
    
    def update_instructor(self, instructor_id: int, instructor_data: dict) -> Optional[Instrutor]:
        return self.instructor_repository.update(instructor_id, instructor_data)
    
    def delete_instructor(self, instructor_id: int) -> bool:
        return self.instructor_repository.delete(instructor_id)