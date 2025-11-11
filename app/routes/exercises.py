from fastapi import APIRouter, Request, Response

router = APIRouter(
    prefix="/exercises",
    tags=["exercises"],
)

@router.get("/")
async def get_exercises(request: Request):
    service = request.app.state.exercise_service
    try:
        exercises = service.get_exercises()
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return exercises

@router.post("/")
async def create_exercise(request: Request, exercise: dict):
    service = request.app.state.exercise_service
    try:
        new_exercise = service.create_exercise(exercise)
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return new_exercise

@router.get("/{exercise_id}")
async def get_exercise(request: Request, exercise_id: int):
    service = request.app.state.exercise_service
    try:
        exercise = service.get_exercise_by_id(exercise_id)
        if exercise is None:
            return {"error": "Exercise not found"}
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return exercise

@router.put("/{exercise_id}")
async def update_exercise(request: Request, exercise_id: int, exercise_data: dict):
    service = request.app.state.exercise_service
    try:
        updated_exercise = service.update_exercise(exercise_id, exercise_data)
        if updated_exercise is None:
            return {"error": "Exercise not found"}
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return updated_exercise

@router.delete("/{exercise_id}")
async def delete_exercise(request: Request, exercise_id: int):
    service = request.app.state.exercise_service
    try:
        result = service.delete_exercise(exercise_id)
        if not result:
            return {"error": "Exercise not found"}
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return {"message": "Exercise deleted successfully"}