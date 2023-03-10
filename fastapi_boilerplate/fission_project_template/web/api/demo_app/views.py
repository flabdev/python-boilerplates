from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/hello_world")
async def hello_world() -> JSONResponse:
    """Demo api.

    :returns: hello world message.
    """
    return JSONResponse({"message": "hello world"})
