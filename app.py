import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from pydantic import ValidationError
from jsonrpcserver import method, Success, Error, Result, async_dispatch, dispatch
import uvicorn

from schemas.message_schema import Message

@method
async def hello_world(**params) -> Result:
    try:
        data = Message(**params)
        return Success({"message": data.message})
    except ValidationError as e:
        return Error(-32602, "Validation error", data=e.errors())

async def json_rpc_handler(request):
    data = await request.body()
    response = await async_dispatch(data)
    return JSONResponse(json.loads(response))

routes = [
    Route('/json-rpc', json_rpc_handler, methods=['POST'])
]

app = Starlette(debug=True, routes=routes)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8888)