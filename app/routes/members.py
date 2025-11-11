from fastapi import APIRouter, Request, Response

router = APIRouter(
    prefix="/members",
    tags=["members"],
)

@router.get("/")
async def get_members(request: Request):
    service = request.app.state.member_service
    try:
        members = service.get_members()
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return members

@router.post("/")
async def create_member(request: Request, member: dict):
    service = request.app.state.member_service
    try:
        new_member = service.create_member(member)
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return new_member

@router.get("/{member_id}")
async def get_member(request: Request, member_id: int):
    service = request.app.state.member_service
    try:
        member = service.get_member_by_id(member_id)
        if member is None:
            return {"error": "Member not found"}
    except Exception as e:
        return Response(content=str(e), status_code=500)
    return member