from fastapi import APIRouter

router = APIRouter(
    prefix="/instrutores",
    tags=["instrutores"],
)

mock_instructors = [
    {
        "instructor_id": 1,
        "name": "Lucas Almeida",
        "email": "lucas.almeida@example.com",
        "cref": "CREF123456"
    },
    {
        "instructor_id": 2,
        "name": "Mariana Gomes",
        "email": "mariana.gomes@example.com",
        "cref": "CREF234567"
    },
]

@router.get("/")
async def get_instrutores():
    return mock_instructors

@router.post("/")
async def create_instructor(instructor: dict):
    pass

@router.get("/{instructor_id}")
async def get_instructor(instructor_id: int):
    pass