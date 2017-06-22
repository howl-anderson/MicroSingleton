from singleton.application.singleton import SingletonApplication
from singleton.application.action import Action

from flask import Flask
app = Flask(__name__)

SingletonApplication("./MicroSingleton.pid").action(Action.SINGLETON)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()