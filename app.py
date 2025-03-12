import fastapi_jsonrpc as jsonrpc
from fastapi import Body

app = jsonrpc.API()

jsonrpc_entrypoint = jsonrpc.Entrypoint('/json-rpc')

@jsonrpc_entrypoint.method()
async def hello_world(message: str = Body(..., examples=['hello'])) -> str:
    return message


app.bind_entrypoint(jsonrpc_entrypoint)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)