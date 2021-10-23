from flask_restx import Resource, Namespace
from src.controller import MainController
from src.model import ModelViewPasswd

Descriptor = Namespace('Pwd', 'Api to validate rules password', ordered=True)
Model = Descriptor.models[ModelViewPasswd.name] = ModelViewPasswd


@Descriptor.route('/isvalid')
class MainResource(Resource):
    @Descriptor.expect(Model, validate=True)
    @Descriptor.doc(body=Model)
    @Descriptor.response(200, 'Success')
    @Descriptor.response(400, 'Validation Error')
    def post(self):
        data = Descriptor.payload
        return MainController().isvalid(data)
