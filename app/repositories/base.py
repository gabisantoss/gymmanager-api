from typing import Generic, Iterable, Optional, TypeVar, Type
from sqlalchemy.orm import Session

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def create(self, obj_in: dict) -> T:
        obj = self.model(**obj_in)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, id_: int) -> Optional[T]:
        return self.db.get(self.model, id_)

    def list(self, skip: int = 0, limit: int = 50) -> Iterable[T]:
        return (
            self.db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, id_: int, obj_in: dict) -> Optional[T]:
        obj = self.get(id_)
        if not obj:
            return None
        for k, v in obj_in.items():
            setattr(obj, k, v)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, id_: int) -> bool:
        obj = self.get(id_)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True
