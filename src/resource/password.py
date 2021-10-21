
from typing import ClassVar

from flask import Flask
from flask_restplus import Api, Resource, fields
from src.server.server import server
from src.model.password import Password
from log import log

api = server.api


@api.route('/isValid')
class Password(Resource):

    @api.expect(Password, validate=True)
    @api.marshal_with(Password)
    def post(self):

        request = api.payload

        log.debug(request)

        # TODO: call method validate
