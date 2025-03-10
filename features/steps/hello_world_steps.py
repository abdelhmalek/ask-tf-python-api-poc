from behave import given, when, then
import requests
import json

@given('a valid JSON-RPC request with message "{message}"')
def step_given_valid_request(context, message):
    context.request_data = {
        "jsonrpc": "2.0",
        "method": "hello_world",
        "params": {"message": message},
        "id": 1
    }

@given('an invalid JSON-RPC request with msg "{msg}"')
def step_given_invalid_request(context, msg):
    context.request_data = {
        "jsonrpc": "2.0",
        "method": "hello_world",
        "params": {"msg": msg},
        "id": 1
    }

@when('the request is sent to the /json-rpc endpoint')
def step_when_request_sent(context):
    context.response = requests.post(
        'http://localhost:5000/json-rpc',
        data=json.dumps(context.request_data),
        headers={'Content-Type': 'application/json'}
    )

@then('the response should be a JSON-RPC result with message "{message}"')
def step_then_response_result(context, message):
    response_data = context.response.json()
    assert 'result' in response_data
    assert response_data['result'] == {"message": message}

@then('the response should be a JSON-RPC error with code -32602')
def step_then_response_error(context):
    response_data = context.response.json()
    assert 'error' in response_data
    assert response_data['error']['code'] == -32602
