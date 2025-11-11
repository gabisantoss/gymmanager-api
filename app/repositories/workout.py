from sqlalchemy.orm import Session, joinedload
from .base import BaseRepository
from ..database.models import Treino, TreinoExercicio
from sqlalchemy import inspect as sa_inspect

class WorkoutRepository(BaseRepository[Treino]):
    def __init__(self, db: Session):
        super().__init__(db, Treino)

    def list_with_relations(self, skip: int = 0, limit: int = 50) -> list[Treino]:
        try:
            pk_cols = sa_inspect(self.model).primary_key
        except Exception:
            pk_cols = []

        query = self.db.query(self.model)
        if pk_cols:
            query = query.order_by(*pk_cols)

        return (
            query
            .options(
                joinedload(Treino.aluno),
                joinedload(Treino.instrutor),
                joinedload(Treino.treino_exercicios).joinedload(TreinoExercicio.exercicio),
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_with_relations(self, id_: int):
        # use Session.get with loader options when available
        try:
            return self.db.get(
                self.model,
                id_,
                options=[
                    joinedload(Treino.aluno),
                    joinedload(Treino.instrutor),
                    joinedload(Treino.treino_exercicios).joinedload(TreinoExercicio.exercicio),
                ],
            )
        except TypeError:
            # fallback to query-based get
            return (
                self.db.query(Treino)
                .options(
                    joinedload(Treino.aluno),
                    joinedload(Treino.instrutor),
                    joinedload(Treino.treino_exercicios).joinedload(TreinoExercicio.exercicio),
                )
                .filter(Treino.id_treino == id_)
                .one_or_none()
            )

    def get_workout_by_member(self, member_id: int) -> list[Treino]:
        return (
            self.db.query(Treino)
            .options(
                joinedload(Treino.aluno),
                joinedload(Treino.instrutor),
                joinedload(Treino.treino_exercicios).joinedload(TreinoExercicio.exercicio),
            )
            .filter(Treino.id_aluno == member_id)
            .all()
        )

    def get_workout_by_instructor(self, instructor_id: int) -> list[Treino]:
        return (
            self.db.query(Treino)
            .options(
                joinedload(Treino.aluno),
                joinedload(Treino.instrutor),
                joinedload(Treino.treino_exercicios).joinedload(TreinoExercicio.exercicio),
            )
            .filter(Treino.id_instrutor == instructor_id)
            .all()
        )

    def create_with_exercises(self, workout_data: dict) -> Treino:
        """Create a Treino and associated TreinoExercicio rows.

        Expected workout_data keys: id_aluno, id_instrutor, dt_inicio, dt_fim (optional), objetivo,
        and optionally 'exercicios' which is a list of dicts with keys: id_exercicio, series, reps, ordem, carga_kg (optional).
        """
        from ..database.models import TreinoExercicio

        exercicios = workout_data.pop("exercicios", None)
        try:
            treino = Treino(**workout_data)
            self.db.add(treino)
            # flush to get id
            self.db.flush()

            created_exs = []
            if exercicios:
                for ex in exercicios:
                    te = TreinoExercicio(
                        id_treino=treino.id_treino,
                        id_exercicio=ex.get("id_exercicio"),
                        series=ex.get("series"),
                        reps=ex.get("reps"),
                        ordem=ex.get("ordem"),
                        carga_kg=ex.get("carga_kg"),
                    )
                    self.db.add(te)
                    created_exs.append(te)

            self.db.commit()
            # refresh to load relationships
            self.db.refresh(treino)
            return treino
        except Exception:
            self.db.rollback()
            raise
