from .conn import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
import enum

class StatusAssinatura(enum.Enum):
    ATIVA = "ativa"
    SUSPENSA = "suspensa"
    EXPIRADA = "expirada"

class FormaPagamento(enum.Enum):
    CARTAO_CREDITO = "cartao_credito"
    CARTAO_DEBITO = "cartao_debito"
    BOLETO = "boleto"
    PIX = "pix"

class GrupoMuscular(enum.Enum):
    PEITO = "peito"
    COSTAS = "costas"
    PERNAS = "pernas"
    BRAÇOS = "braços"
    OMBROS = "ombros"
    ABDOMEN = "abdomen"

class Aluno(Base):
    __tablename__ = "aluno"

    id_aluno: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    dt_nasc: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    telefone: Mapped[str] = mapped_column(nullable=False)

class Instrutor(Base):
    __tablename__ = "instrutor"

    id_instrutor: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    cref: Mapped[str] = mapped_column(nullable=False, unique=True)

class Plano(Base):
    __tablename__ = "plano"

    id_plano: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    meses_validade: Mapped[int] = mapped_column(nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)

class Assinatura(Base):
    __tablename__ = "assinatura"

    id_assinatura: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_aluno: Mapped[int] = mapped_column(nullable=False)
    id_plano: Mapped[int] = mapped_column(nullable=False)
    dt_inicio: Mapped[str] = mapped_column(nullable=False)
    dt_fim: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[StatusAssinatura] = mapped_column(
        SQLEnum(StatusAssinatura, native_enum=False), nullable=False
    )

class Pagamento(Base):
    __tablename__ = "pagamento"

    id_pagamento: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_assinatura: Mapped[int] = mapped_column(nullable=False)
    valor: Mapped[float] = mapped_column(nullable=False)
    dt_pagamento: Mapped[str] = mapped_column(nullable=False)
    forma: Mapped[FormaPagamento] = mapped_column(
        SQLEnum(FormaPagamento, native_enum=False), nullable=False
    )

class Treino(Base):
    __tablename__ = "treino"

    id_treino: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_aluno: Mapped[int] = mapped_column(nullable=False)
    id_instrutor: Mapped[int] = mapped_column(nullable=False)
    dt_inicio: Mapped[str] = mapped_column(nullable=False)
    dt_fim: Mapped[str] = mapped_column(nullable=True)
    objetivo: Mapped[str] = mapped_column(nullable=False)

class Exercicio(Base):
    __tablename__ = "exercicio"

    id_exercicio: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    grupo_muscular: Mapped[GrupoMuscular] = mapped_column(
        SQLEnum(GrupoMuscular, native_enum=False), nullable=False
    )

class TreinoExercicio(Base):
    __tablename__ = "treino_exercicio"

    id_treino_exercicio: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_treino: Mapped[int] = mapped_column(nullable=False)
    id_exercicio: Mapped[int] = mapped_column(nullable=False)
    series: Mapped[int] = mapped_column(nullable=False)
    reps: Mapped[int] = mapped_column(nullable=False)
    ordem: Mapped[int] = mapped_column(nullable=False)
    carga_kg: Mapped[float] = mapped_column(nullable=True)