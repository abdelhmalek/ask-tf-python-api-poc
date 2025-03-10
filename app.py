from flask import Flask, request, jsonify
from jsonrpc import JSONRPCResponseManager, dispatcher
from config import get_config
from marshmallow import ValidationError
from schemas.message_schema import MessageSchema

app = Flask(__name__)
app.config.from_object(get_config())

message_schema = MessageSchema()

@dispatcher.add_method
def hello_world(**kwargs):
    data = message_schema.load(kwargs)
    return {"message": data["message"]}

@app.route('/json-rpc', methods=['POST'])
def api():
    response = JSONRPCResponseManager.handle(
        request.get_data(as_text=True), dispatcher)
    return jsonify(response.data)

if __name__ == '__main__':
    app.run()
