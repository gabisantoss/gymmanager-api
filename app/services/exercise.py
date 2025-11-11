from typing import Optional

from app.repositories.exercise import ExerciseRepository
from app.database.models import Exercicio

class ExerciseService:
    def __init__(self, exercise_repository: ExerciseRepository):
        self.exercise_repository = exercise_repository

    def get_exercise_by_id(self, exercise_id: int) -> Optional[Exercicio]:
        return self.exercise_repository.get(exercise_id)
    
    def get_exercises(self) -> list[Exercicio]:
        return self.exercise_repository.list()

    def create_exercise(self, exercise_data: dict) -> Exercicio:
        return self.exercise_repository.create(exercise_data)
    
    def update_exercise(self, exercise_id: int, exercise_data: dict) -> Optional[Exercicio]:
        return self.exercise_repository.update(exercise_id, exercise_data)
    
    def delete_exercise(self, exercise_id: int) -> bool:
        return self.exercise_repository.delete(exercise_id)