from fastapi import FastAPI, Request, Response
from pydantic import BaseModel, ValidationError, StrictStr, Field
from jsonrpcserver import method, async_dispatch, Result, Success, InvalidParams
from dotenv import load_dotenv
import uvicorn

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

class MessageSchema(BaseModel):
    message: StrictStr = Field(min_length=2)

@method
async def hello_world(**message) -> Result:
    try:
        validated_message = MessageSchema(**message)
        return Success(validated_message.dict())
    except ValidationError as e:
        return InvalidParams(e.errors())

@app.post("/json-rpc")
async def api(request: Request) -> Response:
    request_data = await request.body()
    response = await async_dispatch(request_data)
    return Response(content=response, media_type="application/json")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
