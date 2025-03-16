# filepath: my-app/app.py
from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/file_test")
def file_test():
    """
    Use this method to test if persistent volume access is corredtly configured

    It writes 'hello world' to a file in the persistent volume and then reads it back
    """
    with open('/mnt/data/test.txt', 'w') as f:
        f.write('hello world')
    with open('/mnt/data/test.txt', 'r') as f:
        return f.read()
    
@app.route("/test_env")
def test_env():
    """
    Use this method to test if environment variables are correctly set
    """
    return os.environ

@app.route("/health")
def health():
    tests = {
        'hello_world': requests.get("http://localhost:80/"),
        'persistent_volume': requests.get("http://localhost:80/file_test"),
        'env': requests.get("http://localhost:80/test_env")
    }
    response = {}
    passed = True
    for k,v in tests.items():
        if v.status_code != 200:
            response[k] = 'failed'
            passed = False
        else:
            response[k] = 'passed'
    response['status'] = 'passed' if passed else 'failed'
    return response, 200 if passed else 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
