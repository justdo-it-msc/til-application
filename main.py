import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from containers import Container
from middlewares import create_middlewares
from note.interface.controllers.note_controllers import router as note_routers
from user.interface.controllers.user_controller import router as user_routers

app = FastAPI()
app.container = Container()

app.include_router(user_routers)
app.include_router(note_routers)

create_middlewares(app)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(exc: RequestValidationError):
    return JSONResponse(status_code=400, content=exc.errors())


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
