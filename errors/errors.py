from jsonrpc.exceptions import JSONRPCDispatchException

class InvalidParamsError(JSONRPCDispatchException):
    def __init__(self, messages):
        message = self.format_message(messages)
        data = self.format_data(messages)
        super().__init__(-32602, message, data)

    @staticmethod
    def format_message(messages):
        return " | ".join([f"{key}: {', '.join(value)}" for key, value in messages.items()])

    @staticmethod
    def format_data(messages):
        return {
            "validation": {
                "source": "payload",
                "keys": list(messages.keys())
            }
        }
