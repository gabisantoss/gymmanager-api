from fastapi import APIRouter, Request, Response

router = APIRouter(
    prefix="/instructors",
    tags=["instructors"],
)

@router.get("/")
async def get_instrutores(request: Request):
    service = request.app.state.instructor_service
    try:
        instructors = service.get_instructors()
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return instructors

@router.post("/")
async def create_instructor(request: Request, instructor: dict):
    service = request.app.state.instructor_service
    try:
        new_instructor = service.create_instructor(instructor)
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return new_instructor

@router.get("/{instructor_id}")
async def get_instructor(request: Request, instructor_id: int):
    service = request.app.state.instructor_service
    try:
        instructor = service.get_instructor_by_id(instructor_id)
        if instructor is None:
            return {"error": "Instructor not found"}
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return instructor