from typing import Generic, Iterable, Optional, TypeVar, Type
from sqlalchemy.orm import Session
from sqlalchemy import inspect as sa_inspect

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def create(self, obj_in: dict) -> T:
        try:
            obj = self.model(**obj_in)
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except Exception as e:
            self.db.rollback()
            raise e

    def get(self, id_: int) -> Optional[T]:
        return self.db.get(self.model, id_)

    def list(self, skip: int = 0, limit: int = 50) -> list[T]:
        # Order results by the model primary key(s) ascending to provide stable, id-ordered listings
        try:
            pk_cols = sa_inspect(self.model).primary_key
        except Exception:
            pk_cols = []

        query = self.db.query(self.model)
        if pk_cols:
            query = query.order_by(*pk_cols)

        return (
            query
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, id_: int, obj_in: dict) -> Optional[T]:
        try:
            obj = self.get(id_)
            if not obj:
                return None
            for k, v in obj_in.items():
                setattr(obj, k, v)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except Exception as e:
            self.db.rollback()
            raise e

    def delete(self, id_: int) -> bool:
        try:
            obj = self.get(id_)
            if not obj:
                return False
            self.db.delete(obj)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
