This POC is a simple JSON-RPC HTTP API in python to demonstrate how a python microservice would behave.
It was initiated by the AskTF project to see the feasability of having such API and check if there is any constraint.

This API contains a simple method `hello-world` that returns the following `result`
```json
{
    "message": "Hello World"
}
```

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd ask-tf-python-api-poc
    ```

2. Install `pyenv` if you haven't already:
    ```sh
    curl https://pyenv.run | bash
    ```

3. Install dependencies:
    ```sh
    make install
    ```

## Running the API

1. Start the API server:
    ```sh
    make run
    ```

2. The API will be available at `http://localhost:5000`.

3. To start the API server in development mode with hot reload:
    ```sh
    make run-dev
    ```

4. The API will be available at `http://localhost:5000`.

## Example Request

To call the `hello-world` method, send a POST request to the API with the following JSON payload:
```json
{
    "jsonrpc": "2.0",
    "method": "hello-world",
    "params": {},
    "id": 1
}
```

The response will be:
```json
{
    "jsonrpc": "2.0",
    "result": {
        "message": "Hello World"
    },
    "id": 1
}
```
