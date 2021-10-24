from flask import Flask
from flask_restx import Api

from src.environment import environment_config
from src.resource import Descriptor
from .error_handler import resource_internal_error, resource_not_found


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

        # default errors
        self.app.register_error_handler(404, resource_not_found)
        self.app.register_error_handler(500, resource_internal_error)

    def run(self):
        self.app.run(
            host=environment_config["host"],  # fix docker outside access
            debug=environment_config["debug"],
            port=environment_config["port"]
        )


oServerInstance = ServerInstance()
