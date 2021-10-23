from flask import Flask
from flask_restx import Api

from src.environment import environment_config
from src.resource import Descriptor


class ServerInstance(object):
    def __init__(self) -> None:
        path = environment_config['pathbase']

        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='2.0',
                       title='Password API',
                       description='The Password API',
                       doc=environment_config["swagger-url"]
                       )

        self.api.add_namespace(Descriptor, path=path)

    def run(self):
        self.app.run(
            debug=environment_config["debug"],
            port=environment_config["port"]
        )


oServerInstance = ServerInstance()
