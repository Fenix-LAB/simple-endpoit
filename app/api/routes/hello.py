from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.logger_config import logger

app_router = APIRouter()
from app.api.schemas.hello_request import HelloRequest
from app.api.schemas.hello_response import HelloResponse


@app_router.post("/world")
async def hello(
    request: HelloRequest,
):
    """
    ## DESCRIPTION
    ### Endpoint to say hello

    ## REQUEST
    - name: str (Name of the user)

    ## RESPONSE
        {
        "Success": Bool,
        "Message": "str",
        "Data": {
            "Token": "str"
            }
        }

    """

    logger.info(f"SERVER: Event 'hello' - {request.name}")
    return JSONResponse(
        content=HelloResponse(message=f"Hello {request.name}").dict(),
        status_code=200,
    )
