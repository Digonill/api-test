from flask import Flask
from flask_restx import Api
from src.environment import environment_config


class ServerInstance(object):
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='Password API',
                       description='The Password API',
                       doc=environment_config["swagger-url"]
                       )
        self.ns = self.api.namespace('Todos', description= 'Todo operation')

    def run(self):
        self.app.run(
            debug=environment_config["debug"],
            port=environment_config["port"]
        )


oServerInstance = ServerInstance()
