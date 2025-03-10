from jsonrpc.exceptions import JSONRPCInvalidParams

class JSONRPCError(Exception):
    def __init__(self, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        error = {
            "code": self.code,
            "message": self.message
        }
        if self.data:
            error["data"] = self.data
        return {"jsonrpc": "2.0", "error": error, "id": None }

class InvalidParamsError(JSONRPCError):
    def __init__(self, messages):
        message = self.format_message(messages)
        data = self.format_data(messages)
        super().__init__(-32602, message, data)

    @staticmethod
    def format_message(messages):
        return " | ".join([f"{key} {', '.join(value)}" for key, value in messages.items()])

    @staticmethod
    def format_data(messages):
        return {
            "validation": {
                "source": "payload",
                "keys": list(messages.keys())
            }
        }
