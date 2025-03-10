import unittest
from flask import Flask
from app import app, dispatcher, hello_world
from jsonrpc import JSONRPCResponseManager
from errors.errors import InvalidParamsError

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world_valid(self):
        # Unit test for valid input
        response = hello_world(message= "Hello, World!")
        self.assertEqual(response, {"message": "Hello, World!"})

    def test_hello_world_invalid(self):
        # Unit test for invalid input
        with self.assertRaises(InvalidParamsError):
            hello_world(msg= "Hello, World!")   

    def test_hello_world_functional(self):
        # Functional test for valid input
        response = self.app.post('/json-rpc', json={
            "jsonrpc": "2.0",
            "method": "hello_world",
            "params": {"message": "Hello, World!"},
            "id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], {"message": "Hello, World!"})

    def test_hello_world_functional_invalid(self):
        # Functional test for invalid input
        response = self.app.post('/json-rpc', json={
            "jsonrpc": "2.0",
            "method": "hello_world",
            "params": {"msg": "Hello, World!"},
            "id": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)
        self.assertEqual(response.json['error']['code'], -32602)

if __name__ == '__main__':
    unittest.main()
