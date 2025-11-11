from typing import Optional

from app.repositories.workout import WorkoutRepository
from app.database.models import Treino, Aluno, Instrutor


class WorkoutService:
    def __init__(self, workout_repository: WorkoutRepository):
        self.workout_repository = workout_repository

    def _serialize_treino(self, treino: Treino) -> dict:
        result = {
            "id_treino": treino.id_treino,
            "id_aluno": treino.id_aluno,
            "id_instrutor": treino.id_instrutor,
            "dt_inicio": treino.dt_inicio,
            "dt_fim": treino.dt_fim,
            "objetivo": treino.objetivo,
        }

        # include aluno if loaded
        aluno = getattr(treino, "aluno", None)
        if isinstance(aluno, Aluno) or aluno is not None:
            result["aluno"] = {
                "id_aluno": aluno.id_aluno,
                "nome": aluno.nome,
                "email": aluno.email,
                "dt_nasc": aluno.dt_nasc,
                "cpf": aluno.cpf,
                "telefone": aluno.telefone,
            }

        instrutor = getattr(treino, "instrutor", None)
        if isinstance(instrutor, Instrutor) or instrutor is not None:
            result["instrutor"] = {
                "id_instrutor": instrutor.id_instrutor,
                "nome": instrutor.nome,
                "email": instrutor.email,
                "cref": instrutor.cref,
            }

        # include exercises if present
        treino_exs = getattr(treino, "treino_exercicios", None)
        if treino_exs is not None:
            result["exercicios"] = []
            for ex in treino_exs:
                ex_obj = {
                    "id_treino_exercicio": ex.id_treino_exercicio,
                    "id_exercicio": ex.id_exercicio,
                    "series": ex.series,
                    "reps": ex.reps,
                    "ordem": ex.ordem,
                    "carga_kg": ex.carga_kg,
                }
                # include exercise name if relationship is loaded
                exercicio = getattr(ex, "exercicio", None)
                if exercicio is not None:
                    ex_obj["nome_exercicio"] = getattr(exercicio, "nome", None)
                result["exercicios"].append(ex_obj)

        return result

    def get_workout_by_id(self, workout_id: int) -> Optional[dict]:
        treino = self.workout_repository.get_with_relations(workout_id)
        if treino is None:
            return None
        return self._serialize_treino(treino)

    def get_workouts(self) -> list[dict]:
        treinos = self.workout_repository.list_with_relations()
        return [self._serialize_treino(t) for t in treinos]

    def create_workout(self, workout_data: dict) -> Treino:
        treino = self.workout_repository.create_with_exercises(workout_data)
        # reload the treino with relations populated and serialize
        full = self.workout_repository.get_with_relations(treino.id_treino)
        return self._serialize_treino(full if full is not None else treino)

    def update_workout(self, workout_id: int, workout_data: dict) -> Optional[Treino]:
        return self.workout_repository.update(workout_id, workout_data)

    def delete_workout(self, workout_id: int) -> bool:
        return self.workout_repository.delete(workout_id)

    def get_workouts_by_member(self, member_id: int) -> list[dict]:
        treinos = self.workout_repository.get_workout_by_member(member_id)
        return [self._serialize_treino(t) for t in treinos]

    def get_workouts_by_instructor(self, instructor_id: int) -> list[dict]:
        treinos = self.workout_repository.get_workout_by_instructor(instructor_id)
        return [self._serialize_treino(t) for t in treinos]