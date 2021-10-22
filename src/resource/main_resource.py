from flask_restx import Resource

from src.controller import MainController
from src.model import ModelViewPasswd
from src.server import oServerInstance

api = oServerInstance.api
ns = oServerInstance.ns


@ns.route('/', endpoint='Teste')
@api.doc(responses={404: "Todo not found"}, params={"todo_id": "The Todo ID"})
class MainResource(Resource):

    @ns.doc('teste')
    @ns.marshal_list_with([])
    def get(self):
        '''List all tasks'''
        return []

    @ns.doc('isvalid')
    @ns.marshal_with(ModelViewPasswd)
    def post(self):
        request = api.payload
        return MainController().isvalid(request)
