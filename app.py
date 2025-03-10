from flask import Flask, request, jsonify
from jsonrpc import JSONRPCResponseManager, dispatcher
from config import get_config
from marshmallow import ValidationError
from schemas.message_schema import MessageSchema
from jsonrpc.exceptions import JSONRPCDispatchException
from errors.errors import InvalidParamsError

app = Flask(__name__)
app.config.from_object(get_config())

message_schema = MessageSchema()

@dispatcher.add_method
def hello_world(**kwargs):
    try:
        data = message_schema.load(kwargs)
        return {"message": data["message"]}
    except ValidationError as e:
        raise InvalidParamsError(messages=e.messages)

@app.errorhandler(Exception)
def handle_exception(error):
    response = {
        "jsonrpc": "2.0",
        "error": {
            "code": -32603,
            "message": "Internal error",
            "data": str(error)
        },
        "id": 1
    }
    return jsonify(response), 500

@app.route('/json-rpc', methods=['POST'])
def api():
    response = JSONRPCResponseManager.handle(
        request.get_data(as_text=True), dispatcher)
    return jsonify(response.data)

if __name__ == '__main__':
    app.run()
