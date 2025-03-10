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

## Running with Docker

1. To build and start the Docker containers:
    ```sh
    make up
    ```

2. To start the Docker containers in detached mode:
    ```sh
    make dup
    ```

3. To stop and remove the Docker containers:
    ```sh
    make down
    ```

## Running Tests

1. To run unit tests:
    ```sh
    make test
    ```

2. To run functional (Cucumber) tests:
    ```sh
    make functional-test
    ```
    N.B. Make sure the app is already up before running the functional tests

## Example Request

To call the `hello-world` method, send a POST request to the API with the following JSON payload:
```json
{
    "jsonrpc": "2.0",
    "method": "hello-world",
    "params": {
        "message": "Hello my sneaky friend"
    },
    "id": 1
}
```

The response will be:
```json
{
    "jsonrpc": "2.0",
    "result": {
        "message": "Hello my sneaky friend"
    },
    "id": 1
}
```
