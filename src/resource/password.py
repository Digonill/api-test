from flask_restplus import Resource
from src import controller, model, server

api = server.server.api


@api.route('/isValid')
class Password(Resource):

    @api.expect(model.password.password_model, validate=True)
    @api.marshal_with(model.password.password_model)
    def post(self):
        request = api.payload
        pwd = controller.Password()

        return pwd.isvalid(request)
