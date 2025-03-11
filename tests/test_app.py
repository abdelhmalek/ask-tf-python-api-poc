import unittest
from fastapi.testclient import TestClient
from app import app, hello_world
from errors.errors import InvalidParamsError

client = TestClient(app)

class HelloWorldTestCase(unittest.TestCase):
    def test_hello_world_valid(self):
        # Unit test for valid input
        response = hello_world(message="Hello, World!")
        self.assertEqual(response, {"message": "Hello, World!"})

    def test_hello_world_invalid(self):
        # Unit test for invalid input
        with self.assertRaises(InvalidParamsError):
            hello_world(msg="Hello, World!")

    def test_hello_world_functional(self):
        # Functional test for valid input
        response = client.post('/json-rpc', json={
            "jsonrpc": "2.0",
            "method": "hello_world",
            "params": {"message": "Hello, World!"},
            "id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], {"message": "Hello, World!"})

    def test_hello_world_functional_invalid(self):
        # Functional test for invalid input
        response = client.post('/json-rpc', json={
            "jsonrpc": "2.0",
            "method": "hello_world",
            "params": {"msg": "Hello, World!"},
            "id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error']['code'], -32602)

if __name__ == '__main__':
    unittest.main()
