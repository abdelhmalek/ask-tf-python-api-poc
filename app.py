from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from pydantic import ValidationError
from dotenv import load_dotenv
import uvicorn
import json

from jsonrpc_starlette import JSONRPCStarlette
from schemas.message_schema import Message

load_dotenv()

jsonrpc = JSONRPCStarlette()

async def hello_world(**params):
    try:
        data = Message(**params)
        return {"message": data.message}
    except ValidationError as e:
        return {
            "error": {
                "code": -32602,
                "message": "Validation error",
                "data": e.errors()
            }
        }

jsonrpc.add_function(hello_world)

async def json_rpc_handler(request):
    data = await request.body()
    result = await jsonrpc.handle(data)
    return JSONResponse(json.loads(result))

routes = [
    Route('/json-rpc', json_rpc_handler, methods=['POST'])
]

app = Starlette(debug=True, routes=routes)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8888)