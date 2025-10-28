from fastapi import APIRouter

router = APIRouter(
    prefix="/alunos",
    tags=["alunos"],
)

mock_members = [
    {
        "student_id": 1,
        "name": "Alice Silva",
        "email": "alice.silva@example.com",
        "birth_date": "2002-03-15",
        "cpf": "12345678901",
        "phone": "(21) 98765-4321"
    },
    {
        "student_id": 2,
        "name": "Bruno Costa",
        "email": "bruno.costa@example.com",
        "birth_date": "1999-11-02",
        "cpf": "23456789012",
        "phone": "(21) 99876-5432"
    },
    {
        "student_id": 3,
        "name": "Camila Ferreira",
        "email": "camila.ferreira@example.com",
        "birth_date": "2001-07-20",
        "cpf": "34567890123",
        "phone": "(21) 97654-3210"
    },
    {
        "student_id": 4,
        "name": "Diego Martins",
        "email": "diego.martins@example.com",
        "birth_date": "2000-05-08",
        "cpf": "45678901234",
        "phone": "(21) 96543-2109"
    },
    {
        "student_id": 5,
        "name": "Eduarda Souza",
        "email": "eduarda.souza@example.com",
        "birth_date": "2003-09-27",
        "cpf": "56789012345",
        "phone": "(21) 95432-1098"
    },
    {
        "student_id": 6,
        "name": "Felipe Rocha",
        "email": "felipe.rocha@example.com",
        "birth_date": "1998-12-10",
        "cpf": "67890123456",
        "phone": "(21) 94321-0987"
    },
    {
        "student_id": 7,
        "name": "Gabriela Cruz",
        "email": "gabriela.cruz@example.com",
        "birth_date": "2002-01-25",
        "cpf": "78901234567",
        "phone": "(21) 93210-9876"
    },
    {
        "student_id": 8,
        "name": "Henrique Alves",
        "email": "henrique.alves@example.com",
        "birth_date": "2001-04-03",
        "cpf": "89012345678",
        "phone": "(21) 92109-8765"
    },
    {
        "student_id": 9,
        "name": "Isabela Lima",
        "email": "isabela.lima@example.com",
        "birth_date": "2000-10-18",
        "cpf": "90123456789",
        "phone": "(21) 91098-7654"
    },
    {
        "student_id": 10,
        "name": "João Pedro Ribeiro",
        "email": "joao.ribeiro@example.com",
        "birth_date": "1999-06-30",
        "cpf": "01234567890",
        "phone": "(21) 90087-6543"
    }
]

@router.get("/")
async def get_members():
    return mock_members

@router.post("/")
async def create_member(member: dict):
    pass

@router.get("/{member_id}")
async def get_member(member_id: int):
    pass