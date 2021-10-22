from flask_restx import fields
from src.server import oServerInstance

ModelViewPasswd = oServerInstance.api.models('password',
                                             {
                                                 'text': fields.String(required=True, min_length=9, max_length=20, description='Password text to validate')
                                             })
