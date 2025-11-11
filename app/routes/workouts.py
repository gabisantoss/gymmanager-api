from fastapi import APIRouter, Request, Response

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
)

@router.get("/")
async def get_workouts(request: Request):
    service = request.app.state.workout_service
    try:
        workouts = service.get_workouts()
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return workouts

@router.post("/")
async def create_workout(request: Request, workout_data: dict):
    service = request.app.state.workout_service
    try:
        new_workout = service.create_workout(workout_data)
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return new_workout

@router.get("/{workout_id}")
async def get_workout(request: Request, workout_id: int):
    service = request.app.state.workout_service
    try:
        workout = service.get_workout_by_id(workout_id)
        if workout is None:
            return {"error": "Workout not found"}
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return workout

@router.get("/member/{member_id}")
async def get_workouts_by_member(request: Request, member_id: int):
    service = request.app.state.workout_service
    try:
        workouts = service.get_workouts_by_member(member_id)
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return workouts