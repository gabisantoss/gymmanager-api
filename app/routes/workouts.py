from fastapi import APIRouter

router = APIRouter(
    prefix="/treinos",
    tags=["treinos"],
)

mock_treinos = [
    {
        "id_treino": 1,
        "id_aluno": 1,
        "id_instrutor": 1,
        "dt_inicio": "2024-01-10",
        "dt_fim": "2024-04-10",
        "objetivo": "Ganho de massa muscular",
        "exercicios": [
            {
                "id_exercicio": 1,
                "nome": "Supino Reto",
                "grupo_muscular": "PEITO",
                "series": 4,
                "repeticoes": 10,
                "carga": 60.0
            },
            {
                "id_exercicio": 2,
                "nome": "Agachamento",
                "grupo_muscular": "PERNA",
                "series": 4,
                "repeticoes": 12,
                "carga": 80.0
            }
        ]
    },
    {
        "id_treino": 2,
        "id_aluno": 2,
        "id_instrutor": 2,
        "dt_inicio": "2024-02-15",
        "dt_fim": "2024-05-15",
        "objetivo": "Perda de peso",
        "exercicios": [
            {
                "id_exercicio": 3,
                "nome": "Corrida na esteira",
                "grupo_muscular": "CARDIO",
                "series": 1,
                "reps": 30,
                "carga_kg": None
            },
            {
                "id_exercicio": 4,
                "nome": "Abdominal",
                "grupo_muscular": "ABDOME",
                "series": 3,
                "reps": 20,
                "carga_kg": None
            }
        ]
    }
]

@router.get("/")
async def get_treinos():
    return mock_treinos

@router.post("/")
async def create_treino(treino: dict):
    pass

@router.get("/{treino_id}")
async def get_treino(treino_id: int):
    pass