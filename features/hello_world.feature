Feature: Hello World JSON-RPC API

  Scenario: Valid message
    Given a valid JSON-RPC request with message "Hello, World!"
    When the request is sent to the /json-rpc endpoint
    Then the response should be a JSON-RPC result with message "Hello, World!"

  Scenario: Invalid message
    Given an invalid JSON-RPC request with msg "Hello, World!"
    When the request is sent to the /json-rpc endpoint
    Then the response should be a JSON-RPC error with code -32602
