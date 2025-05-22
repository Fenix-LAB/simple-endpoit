from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from app.database.populate import create_tables
from config.logger_config import logger

from config.config import config
from app.api.api_router import router
# from app.database.session import engine
# from app.database.seeder import seed_database
# from app.database.procedures.stores_procedures import stored_prcedures_populate, drop_procedures

# from mangum import Mangum

# from app.middleware import (
#     OneAuthBackend,
#     AuthenticationMiddleware,
# )


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router, prefix=config.ROUTE_PATH)
    # app_.include_router(auth_router)


# def make_middleware() -> list[Middleware]:
#     middleware = [
#         Middleware(
#             CORSMiddleware,
#             allow_origins=["*"],
#             allow_credentials=True,
#             allow_methods=["*"],
#             allow_headers=["*"],
#         ),
#         Middleware(
#             AuthenticationMiddleware,
#             backend=OneAuthBackend(excluded_urls=config.EXCLUDED_URLS),
#         ),
#     ]
#     return middleware


def create_app() -> FastAPI:
    logger.info(f"SERVER: Application - env: {config.ENV}")
    app_ = FastAPI(
        title="FastAPI Template",
        description="API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        # middleware=make_middleware(),
    )
    init_routers(app_=app_)
    logger.info("SERVER: Event 'start up'")

    @app_.on_event("startup")
    async def on_startup():
        # await create_tables(engine)
        # await seed_database(engine)
        # await drop_procedures(engine)
        # await stored_prcedures_populate(engine)
        pass

    logger.info("SERVER: App created")
    return app_


app = create_app()
# handler = Mangum(app)
# @app.exception_handler(Exception)
# async def exception_handler(request: Request, exc: Exception):
#     logger.error(f"SERVER: Exception {exc}")
#     return JSONResponse(
#         status_code=500,
#         content={"message": "Internal Server Error"},
#     )
