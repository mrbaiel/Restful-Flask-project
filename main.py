from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)

if __name__ == "__main__":
    app.run()